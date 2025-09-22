# Application Health Checker

A simple Python script to check the uptime of a web application by verifying its HTTP status code. It determines if the application is **up** (working correctly) or **down** (unavailable or not responding).

## Features
- Checks if a website/application is reachable.
- Determines status based on HTTP response codes.
- Automatically prepends `http://` if the protocol is missing.
- Handles connection errors and timeouts.

## Requirements
- Python 3.x
- `requests` library

Install `requests` if you don’t have it:

```bash
pip install requests

```bash
git clone https://github.com/arifansari10027/app-health-checker.git

```bash
python app.py <APPLICATION_URL>