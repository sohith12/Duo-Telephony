import os
from datetime import datetime
from ISOEngLogger import ISOEngLogger
import duo_client
import requests

# Configuration
api_host = "api-a4b09f6a.duosecurity.com"
integration_key = "DIAQM0EUCUUQYLPYL2O6"
secret_key = "Wzh4aLvSeEoHp1Pi5YJdxTG5KoDmtPzpAU8a1sTH"
user_id_to_monitor = "USER_ID_TO_MONITOR"
telephony_credits_threshold = 500
webhook_url = "matt.willoughby@utdallas.edu"  # Change webhook URL

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

def check_telephony_credits(api_host, integration_key, secret_key, user_id, threshold):
    # Function to check Telephony Credits and send alert if low
    # Get current Telephony Credits
    telephony_credits = get_telephony_credits(api_host, integration_key, secret_key, user_id)

    # Check if Telephony Credits are below the threshold
    if telephony_credits < threshold:
        send_alert(f"Telephony Credits for user {user_id} are running low. Current credits: {telephony_credits}")


def send_alert(message):
    Function to send alert (you may need to customize this based on your alerting system)
    # Use your preferred method to send an alert (e.g., email, Slack, etc.)
    # For example, you can use a simple HTTP request to a webhook
    webhook_url = "matt.willoughby@utdallas.edu"  
    payload = {"text": message}
    requests.post(webhook_url, json=payload)

# Set your Duo API information
api_host = "api-a4b09f6a.duosecurity.com"
integration_key = "DIAQM0EUCUUQYLPYL2O6"
secret_key = "Wzh4aLvSeEoHp1Pi5YJdxTG5KoDmtPzpAU8a1sTH"

# Set the user ID and the Telephony Credits threshold
user_id_to_monitor = "USER_ID_TO_MONITOR"   # DUO USER ID"
telephony_credits_threshold = 500  # Adjust this threshold based on your needs

def main():
    try:
        logger.info('Script Started')
        check_telephony_credits(api_host, integration_key, secret_key, user_id_to_monitor, telephony_credits_threshold)
    except Exception:
        logger.exception('Script failed with exception')

if __name__ == '__main__':
    main()
