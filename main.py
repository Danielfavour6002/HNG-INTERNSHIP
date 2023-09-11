from flask import Flask, request, jsonify
import datetime
import pytz
import os

app = Flask(__name__)

@app.route('/get_info', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    return f'slack_name: {slack_name} , track: {track}'

    # Get current UTC time
    utc_time = datetime.datetime.now(pytz.utc)

    # Get the current time offset in hours
    time_offset_hours = utc_time.astimezone(pytz.timezone('UTC+2')).utcoffset().total_seconds() / 3600

    # Check if the time offset is within +/-2 hours
    if -2 <= time_offset_hours <= 2:
        status = 'Success'
    else:
        status = 'Time Offset Error'

    # GitHub URLs
    github_url_file = "https://github.com/your-username/your-repo/blob/main/app.py"
    github_url_source = "https://github.com/your-username/your-repo"

    # Format the UTC time as "YYYY-MM-DDTHH:MM:SSZ"
    formatted_utc_time = utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Return the information in JSON format
    info = {
        'Slack_name': slack_name,
        'Current_day_of_week': utc_time.strftime('%A'),
        'Current_UTC_time': formatted_utc_time,
        'Time_Offset_Hours': time_offset_hours,
        'Track': track,
        'GitHub_URL_of_file': github_url_file,
        'GitHub_URL_of_source_code': github_url_source,
        'Status_Code': status
    }

    return jsonify(info)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
