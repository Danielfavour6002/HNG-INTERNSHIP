from flask import Flask, json, request
import requests
from datetime import datetime

app = Flask(__name__)
today = datetime.now()

@app.route('/api', methods=['GET'])

def user_page():

    slack_name = str(request.args.get('slack_name'))  # slack_name=Favour Daniel
    track = str(request.args.get('track'))  # track=backend

    data_set = {"slack_name": f"{slack_name}",
    "slack_name" : "Favour Daniel",
    "current_day": today.strftime('%A'),
    "utc_time": today.strftime('%Y-%m-%dT%H:%M:%SZ'),
    "track": f"{track}",
    "github_file" : "https://github.com/Danielfavour6002/HNG-INTERNSHIP/blob/SOURCE/main.py",
    "github_repo" : "https://github.com/Danielfavour6002/HNG-INTERNSHIP",
    "status_code": 200}

    json_dump = json.dumps(data_set)

    return json_dump

if __name__ == '__main__':
    app.run(port=7070)