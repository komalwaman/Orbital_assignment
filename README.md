# Orbital Copilot Usage API

A Flask API to calculate and return usage credit data for messages processed by Orbital Copilot.

## 🚀 How to Run

```bash
git clone <your-repo-url>
cd orbital_usage
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

Visit `http://localhost:5000/usage` to get the usage data in JSON.

## 📦 Project Structure

```
orbital_usage/
├── app/                # Core logic
│   ├── credit_calculator.py
│   ├── routes.py
│   ├── utils.py
│   └── __init__.py
├── tests/              # Unit tests
│   └── test_credit_calculator.py
├── run.py              # App entry point
├── requirements.txt    # Dependencies
└── README.md
```

## 🧠 Design Decisions

- Clear separation of concerns: calculation, routing, utilities.
- Tests added for main edge cases (palindrome, bonus, penalties).
- Followed exact contract for `/usage` endpoint output.
- Handles fallback in case of invalid `report_id`.

## 🧪 Tests

Run with:
```bash
python -m unittest discover tests
```

## ⏱ Time Constraints

Due to the 2–3 hour limit:
- Did not add async/concurrent fetch for reports (could be done for perf)
- Basic test coverage, full branch testing would be next

## ✅ Confidence in Accuracy

- Calculation rules implemented directly from spec with clear comments.
- Logic validated with unit tests and manual data samples.

---
Ready for deployment or extension.
