# Sohith Sai Akkala created this file with SMTP method on 12/19/23

import os
from datetime import datetime
from ISOEngLogger import ISOEngLogger
import duo_client
import requests
import smtplib
from email.mime.text import MIMEText

# Configuration
api_host = "api-a4b09f6a.duosecurity.com"
integration_key = "DIAQM0EUCUUQYLPYL2O6"
secret_key = "Wzh4aLvSeEoHp1Pi5YJdxTG5KoDmtPzpAU8a1sTH"
user_id_to_monitor = "user_id"
telephony_credits_threshold = 500
webhook_url = ""  # Change webhook URL # Only use if you use Slack or teams 
smtp_host = "your_smtp_server"
smtp_port = 465  # Adjust the port accordingly (Encrypted email transmissions) or 587 # default port for SMTP
smtp_username = "your_email@example.com"
smtp_password = "your_email_password"
sender_email = "your_email@example.com"
receiver_email = "matt.willoughby@utdallas.edu"

# Get the current script path
script_path = os.path.dirname(os.path.realpath(__file__))
current_datetime = datetime.today().strftime('%Y%m%d_%H%M%S')
log_file_name = f'{current_datetime}_output.log'
log_file_path = os.path.join(script_path, log_file_name)
logger = ISOEngLogger(log_file_path, test_run=True)  # Adjust test_run as needed

def get_telephony_credits(api_host, integration_key, secret_key, user_id):
    # Set up Duo API client
    admin_api = duo_client.Admin(
        ikey="DIAQM0EUCUUQYLPYL2O6",
        skey="Wzh4aLvSeEoHp1Pi5YJdxTG5KoDmtPzpAU8a1sTH",
        host="api-a4b09f6a.duosecurity.com"
    )

    # Replace the following line with the actual API call to get telephony credits
    telephony_credits = 500
    return telephony_credits

def check_telephony_credits(api_host, integration_key, secret_key, user_id, threshold):
    # Function to check Telephony Credits and send alert if low
    # Get current Telephony Credits
    telephony_credits = get_telephony_credits(api_host, integration_key, secret_key, user_id)

    # Check if Telephony Credits are below the threshold
    if telephony_credits < threshold:
        send_alert(f"Telephony Credits for user {user_id} are running low. Current credits: {telephony_credits}")

def send_alert(message):
    # Function to send alert (you may need to customize this based on your alerting system)
    # Use your preferred method to send an alert (e.g., email, Slack, etc.)
    # For example, you can use a simple HTTP request to a webhook
    payload = {"text": message}
    requests.post(webhook_url, json=payload)

    # Uncomment the following line if you want to send an email alert as well
    # send_alert_email(message)

def send_alert_email(message):
    # Function to send an email alert
    email_message = MIMEText(message)
    email_message['Subject'] = "Telephony Credits Alert"
    email_message['From'] = sender_email
    email_message['To'] = receiver_email

    smtp_server = smtplib.SMTP(smtp_host, smtp_port)
    smtp_server.starttls()
    smtp_server.login(smtp_username, smtp_password)
    smtp_server.send_message(email_message)
    smtp_server.quit()

def main():
    try:
        logger.info('Script Started')
        check_telephony_credits(api_host, integration_key, secret_key, user_id_to_monitor, telephony_credits_threshold)
    except Exception:
        logger.exception('Script failed with exception')

if __name__ == '__main__':
    main()
