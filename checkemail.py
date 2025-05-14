import requests
import os
import time

def check_email_availability(email):
    url = "https://login.live.com/GetCredentialType.srf"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "Username": email,
        "uaid": "",
        "scid": "100118",
        "flowToken": ""
    }
    try:
        response = requests.post(url, json=data, headers=headers, timeout=5)
        if response.status_code == 200:
            result = response.json().get("IfExistsResult", None)
            return result == 5  # 5 means email is available
        return False
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return False

# Get desktop path
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
input_file_path = os.path.join(desktop, "generated_emails.txt")
output_file_path = os.path.join(desktop, "available_emails.txt")

# Read emails from file
if not os.path.exists(input_file_path):
    print("Email file not found!")
    exit()

with open(input_file_path, "r") as file:
    emails = file.read().splitlines()

available_emails = []

for email in emails:
    if check_email_availability(email):
        available_emails.append(email)
    time.sleep(0.5)  # Prevent rate limiting

# Save available emails to a new file
with open(output_file_path, "w") as file:
    file.write("\n".join(available_emails))

print(f"Checked {len(emails)} emails. Available ones saved to {output_file_path}!")
