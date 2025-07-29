from flask import Blueprint, jsonify
import requests
from .credit_calculator import calculate_credits

bp = Blueprint("main", __name__)

MESSAGES_URL = "https://owpublic.blob.core.windows.net/tech-task/messages/current-period"
REPORTS_URL_TEMPLATE = "https://owpublic.blob.core.windows.net/tech-task/reports/{}"

@bp.route("/usage", methods=["GET"])
def usage():
    response = requests.get(MESSAGES_URL)
    response.raise_for_status()
    data = response.json()
    messages = data["messages"]

    usage_data = []

    for msg in messages:
        msg_id = msg["id"]
        timestamp = msg["timestamp"]
        report_id = msg.get("report_id")
        report_name = None

        if report_id:
            report_url = REPORTS_URL_TEMPLATE.format(report_id)
            report_response = requests.get(report_url)
            if report_response.status_code == 200:
                report = report_response.json()
                report_name = report["name"]
                credits = float(report["credit_cost"])
            else:
                credits = calculate_credits(msg["text"])
        else:
            # breakpoint()
            credits = calculate_credits(msg["text"])

        usage_entry = {
            "message_id": msg_id,
            "timestamp": timestamp,
            "credits_used": round(credits, 2),
        }
        if report_name:
            usage_entry["report_name"] = report_name

        usage_data.append(usage_entry)

    return jsonify({"usage": usage_data})
