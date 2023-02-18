"""Server Side FCM sample.
Firebase Cloud Messaging (FCM) can be used to send messages to clients on iOS,
Android and Web.
This sample uses FCM to send two types of messages to clients that are subscribed
to the `news` topic. One type of message is a simple notification message (display message).
The other is a notification message (display notification) with platform specific
customizations. For example, a badge is added to messages that are sent to iOS devices.

Refer official firebase module: https://github.com/firebase/quickstart-python/tree/2c68e7c5020f4dbb072cca4da03dba389fbbe4ec/messaging
"""
import json
import requests
import google.auth.transport.requests

from google.oauth2 import service_account
from django.conf import settings
from django.http import JsonResponse

PROJECT_ID = settings.FIREBASE_PROJECT_ID
BASE_URL = 'https://fcm.googleapis.com'
FCM_ENDPOINT = 'v1/projects/' + PROJECT_ID + '/messages:send'
FCM_URL = BASE_URL + '/' + FCM_ENDPOINT
SCOPES = ['https://www.googleapis.com/auth/firebase.messaging']


# [START retrieve_access_token]
def _get_access_token():
    """Retrieve a valid access token that can be used to authorize requests.
    :return: Access token.
    """
    credentials = service_account.Credentials.from_service_account_file(
        settings.GOOGLE_APPLICATION_CREDENTIALS, scopes=SCOPES)
    request = google.auth.transport.requests.Request()
    credentials.refresh(request)
    return credentials.token
# [END retrieve_access_token]


def _send_fcm_message(device_token):
    """Send HTTP request to FCM with given message.
    
    :param device_token: firebase app token for specific device
    :type device_token: str

    :return: JSON Response
    """
    message = {
        'message': {
            # 'topic': 'news',
            'token': device_token,
            'notification': {
                'title': 'FCM Notification - title',
                'body': 'Notification from FCM - body'
            }
        }
    }

    # [START use_access_token]
    headers = {
        'Authorization': 'Bearer ' + _get_access_token(),
        'Content-Type': 'application/json; UTF-8',
    }
    # [END use_access_token]
    resp = requests.post(FCM_URL, data=json.dumps(
        message), headers=headers)

    if resp.status_code == 200:
        print('Message sent to Firebase for delivery, response:')
        print(resp.text)
        return JsonResponse({
            "status": 200,
            "message":"sent_successfully"},
            status = 200
        )
    else:
        print('Unable to send message to Firebase')
        print(resp.text)
        return JsonResponse({
            "status": 500,
            "message":"sent_successfully"
        }, status=500)