from flask import Flask, jsonify, render_template
import requests
import os

app = Flask(__name__)

# Read backend URL from environment or default to localhost
BACKEND_URL = os.environ.get('BACKEND_URL', 'http://localhost:5001')


@app.route('/')
def index():
    """Render the main dashboard HTML page."""
    return render_template('index.html')


@app.route('/api/measurements', methods=['GET'])
def api_get_measurements():
    """Proxy measurement requests to the backend service."""
    try:
        resp = requests.get(f'{BACKEND_URL}/measurements', timeout=5)
        resp.raise_for_status()
        return jsonify(resp.json())
    except Exception as exc:
        return jsonify({'error': str(exc)}), 502


@app.route('/api/start', methods=['POST'])
def api_start_system():
    """Proxy start requests to the backend service."""
    try:
        resp = requests.post(f'{BACKEND_URL}/start', timeout=5)
        resp.raise_for_status()
        return jsonify(resp.json())
    except Exception as exc:
        return jsonify({'error': str(exc)}), 502


@app.route('/api/stop', methods=['POST'])
def api_stop_system():
    """Proxy stop requests to the backend service."""
    try:
        resp = requests.post(f'{BACKEND_URL}/stop', timeout=5)
        resp.raise_for_status()
        return jsonify(resp.json())
    except Exception as exc:
        return jsonify({'error': str(exc)}), 502


@app.route('/api/emergency_stop', methods=['POST'])
def api_emergency_stop_system():
    """Proxy emergency stop requests to the backend service."""
    try:
        resp = requests.post(f'{BACKEND_URL}/emergency_stop', timeout=5)
        resp.raise_for_status()
        return jsonify(resp.json())
    except Exception as exc:
        return jsonify({'error': str(exc)}), 502


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
