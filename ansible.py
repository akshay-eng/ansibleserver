import json
from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)
# Enable CORS for all routes

@app.route('/', methods=['GET'])
def getappstatus():
    return "Success!"

@app.route('/triggerjobtemplate', methods=['POST'])
def trigger_job_template():
    api_endpoint = 'https://172.17.80.167/api/v2/job_templates/15/launch/'
    headers = {'Content-Type': 'application/json'}
    auth = ('admin', 'Wipro@123')

    # Get extra_vars from the request payload
    extra_vars = request.get_json().get('extra_vars', {})
    print(extra_vars)
    # Construct the payload with extra_vars
    payload = {
        'extra_vars': extra_vars
    }
    print(payload)
    # Convert payload to JSON string
    json_payload = json.dumps(payload)
    print(json_payload)
    data1="'" + json_payload + "'"
    print(data1)

    # Make the POST request
    response = requests.post(api_endpoint, headers=headers, auth=auth, data=json_payload, verify=False)

    if response.status_code == 201:
        return 'Success'
    else:
        return f'Error triggering job template. Status code: {response.status_code}, Response: {response.text}'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)