import signal
import sys
from datetime import datetime, timezone
import random

from flask import Flask, request, jsonify, Response

app = Flask(__name__)

@app.route('/temperature', methods=['GET'])
def get_temperature_by_location():
    location = request.args.get('location')
    return measure_temperature(None, location), 200

@app.route('/temperature/<sensor_id>', methods=['GET'])
def get_temperature_by_sensor_id(sensor_id):
    return measure_temperature(sensor_id, None), 200


def measure_temperature(sensor_id, location) -> Response:
    return jsonify({
        'value': round(random.uniform(-30.0, 30.0), 1),
        'unit': 'C',
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'location': location or 'Living Room',
        'status': 'online',
        'sensor_id': sensor_id or '1',
        'sensor_type': 'temperature',
        'description': 'Temperature in Living Room'
    })

def handle_signal(signum, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, handle_signal)   # Ctrl+C / docker stop -> SIGINT/SIGTERM
signal.signal(signal.SIGTERM, handle_signal)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
