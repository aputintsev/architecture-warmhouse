import signal
import sys
from datetime import datetime, timezone
import random

from flask import Flask, request, jsonify, Response

app = Flask(__name__)

@app.get('/temperature')
def get_temperature_by_location():
    location = request.args.get('location')
    sensor_id: str | None = None
    match location:
        case 'Living Room':
            sensor_id = '1'
        case 'Bedroom':
            sensor_id = '2'
        case 'Kitchen':
            sensor_id = '3'
        case _:
            sensor_id = '0'

    return measure_temperature(sensor_id, location), 200

@app.get('/temperature/<sensor_id>')
def get_temperature_by_sensor_id(sensor_id):
    location = request.args.get('location')
    if location is None or location == '':
        match sensor_id:
            case '1':
                location = 'Living Room'
            case '2':
                location = 'Bedroom'
            case '3':
                location = 'Kitchen'
            case _:
                location = 'Unknown'

    return measure_temperature(sensor_id, location), 200


def measure_temperature(sensor_id, location) -> Response:
    return jsonify({
        'value': round(random.uniform(-30.0, 30.0), 1),
        'unit': 'C',
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'location': location or 'Unknown',
        'status': 'active',
        'sensor_id': sensor_id or '0',
        'sensor_type': 'temperature',
        'description': f'Temperature in {location}',
    })

def handle_signal(signum, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, handle_signal)   # Ctrl+C / docker stop -> SIGINT/SIGTERM
signal.signal(signal.SIGTERM, handle_signal)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
