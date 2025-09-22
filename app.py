import requests
import sys

def check_application_status(url, timeout=5):
    
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    try:
        response = requests.get(url, timeout=timeout)
        if 200 <= response.status_code < 300:
            return 'up'
        else:
            return 'down'
    except requests.exceptions.RequestException:
        return 'down'

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <application_url>")
        sys.exit(1)

    app_url = sys.argv[1]
    status = check_application_status(app_url)
    print(f"Application '{app_url}' is {status}.")
