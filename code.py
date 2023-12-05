import duo_client
import requests

# Function to get Telephony Credits information from Duo API
def get_telephony_credits(api_host, integration_key, secret_key, user_id):
    # Set up Duo API client
    admin_api = duo_client.Admin(
        ikey="DIAQM0EUCUUQYLPYL2O6", 
        skey="Wzh4aLvSeEoHp1Pi5YJdxTG5KoDmtPzpAU8a1sTH",
        host="api-a4b09f6a.duosecurity.com"
    )

    # Get user details, including Telephony Credits information
    user_details = admin_api.get_user(user_id)

    # Extract Telephony Credits information from the user details
    telephony_credits = user_details.get('telephony_credits', 0)

    return telephony_credits

# Function to check Telephony Credits and send alert if low
def check_telephony_credits(api_host, integration_key, secret_key, user_id, threshold):
    # Get current Telephony Credits
    telephony_credits = get_telephony_credits(api_host, integration_key, secret_key, user_id)

    # Check if Telephony Credits are below the threshold
    if telephony_credits < threshold:
        send_alert(f"Telephony Credits for user {user_id} are running low. Current credits: {telephony_credits}")

# Function to send alert (you may need to customize this based on your alerting system)
def send_alert(message):
    # Use your preferred method to send an alert (e.g., email, Slack, etc.)
    # For example, you can use a simple HTTP request to a webhook
    webhook_url = "YOUR_ALERT_WEBHOOK_URL"  -> need to change webhook url
    payload = {"text": message}
    requests.post(webhook_url, json=payload)

# Set your Duo API information
api_host = "api-a4b09f6a.duosecurity.com"
integration_key = "DIAQM0EUCUUQYLPYL2O6"
secret_key = "Wzh4aLvSeEoHp1Pi5YJdxTG5KoDmtPzpAU8a1sTH"

# Set the user ID and the Telephony Credits threshold
user_id_to_monitor = "USER_ID_TO_MONITOR"  -> need to change userid
telephony_credits_threshold = 20  # Adjust this threshold based on your needs

# Check Telephony Credits and send alert if low
check_telephony_credits(api_host, integration_key, secret_key, user_id_to_monitor, telephony_credits_threshold)
