# Orbital Copilot Usage API

A Flask API to calculate and return usage credit data for messages processed by Orbital Copilot.

## How to Run

First, clone the repository:

```bash
git clone https://github.com/komalwaman/Orbital_assignment.git
# or
git clone git@github.com:komalwaman/Orbital_assignment.git
```

Then, follow these steps to set up and start the application:

```bash
cd Orbital_assignment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask run
```

Troubleshooting: Port 5000 in Use
If you see an error like:

```bash
Address already in use
Port 5000 is in use by another program. Either identify and stop that program, or start the server with a different port.
On macOS, try disabling the 'AirPlay Receiver' service from System Preferences -> General -> AirDrop & Handoff.
```

You have two options:

1. Disable AirPlay Receiver in System Preferences > General > AirDrop & Handoff on macOS.
2. Or run the app on a different port:

```bash
flask run --port=5001
```

Finally, open your browser and visit: `http://localhost:{port}/usage` 
Replace `{port}` with the port number you used (default is 5000).

## Project Structure

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

## Design Decisions

- Clear separation of concerns: calculation, routing, utilities.
- Tests added for main edge cases (palindrome, bonus, penalties).
- Followed exact contract for `/usage` endpoint output.
- Handles fallback in case of invalid `report_id`.

## Tests

Run with:
```bash
python -m unittest discover tests
```

## Time Constraints/Future enhancement

Due to the time limit:
- Did not add async/concurrent fetch for reports: The solution fetches reports sequentially from the remote URL https://owpublic.blob.core.windows.net/tech-task/reports/{report_id}. In a real-world scenario, to improve performance especially when multiple reports need to be fetched, it would be beneficial to implement asynchronous or concurrent HTTP requests. This would allow the app to fetch multiple reports in parallel rather than waiting for each request to finish before starting the next one.
- Basic test coverage: The provided tests cover the main calculation rules and typical edge cases. However, full branch testing (covering every possible conditional path, including error cases or unusual inputs) would be ideal for production readiness, but was not feasible within the short timeframe.
- API endpoint tests not included: The test suite currently focuses only on the core calculation logic. Tests for the API layer itself (such as HTTP response codes, JSON structure, error handling on endpoints) were not added due to time constraints.

Some basic improvements to consider for production readiness:

- Basic input validation and error handling implemented; more robust handling (e.g., timeouts, retries) recommended.
- No authentication or rate limiting included; essential for securing a real-world API.
- The /usage endpoint requires a valid report_id parameter; detailed input/output documentation would help integration.
- Future work includes API validation, integration tests, caching to reduce repeated fetches, and improved logging.

## Confidence in Accuracy

- Calculation rules implemented directly from spec with clear comments.
- Logic validated with unit tests and manual data samples.
