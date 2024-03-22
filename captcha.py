import requests
import json

def solver_captcha(base64_data):
    url = 'https://api.capsolver.com/createTask'
    headers = {
        'Host': 'api.capsolver.com',
        'Content-Type': 'application/json'
    }

    data = {
    "clientKey": "CAI-CA8F5D78B888FEB049BE5444950CAA9F",
    "task": {
        "type": "ImageToTextTask",
        "websiteURL": "https://keliauk.urm.lt/en/user/login",
        "module": "common",
        "body": base64_data
    }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Print the response
    return response.json()['solution']['text']