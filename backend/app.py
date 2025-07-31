"""
Backend service for the RTB Bush inspection system.

This Flask application exposes a simple REST API for controlling an imagined
piece of hardware used to inspect RTB bushes. The API provides three
endpoints for starting, stopping, and emergency stopping the machine, and a
fourth endpoint to fetch the latest measurement data. The hardware control
functions are implemented as placeholders that can be extended to
communicate with real hardware in the future.

Endpoints:
  POST /start           – start the inspection system.
  POST /stop            – gracefully stop the inspection system.
  POST /emergency_stop  – immediately halt the system.
  GET  /measurements    – retrieve current height, ID and OD measurements.

The application tracks whether the system is running and generates random
measurement values when running. When stopped, it returns zeroes.

To run the backend locally (outside of Docker) install the dependencies and
execute this script:

    pip install -r requirements.txt
    python app.py

The service will listen on all interfaces on port 5000. In a Docker
deployment the port will be mapped to the host by docker-compose.
"""

from flask import Flask, jsonify, request
import random
import threading


app = Flask(__name__)

# State indicating whether the system is currently running. When running,
# measurement values are randomly generated to simulate sensor readings.
system_running = False
state_lock = threading.Lock()



def start_system() -> None:
    """Placeholder function to start the hardware.

    In a real-world system this function would contain the logic to
    initialise and begin operation of the inspection hardware. For
    demonstration purposes it simply flips a flag and logs to stdout.
    """
    global system_running
    with state_lock:
        system_running = True
    print("Hardware start invoked.")



def stop_system() -> None:
    """Placeholder function to gracefully stop the hardware.

    Any required cleanup or safe shutdown operations should be implemented
    here. For demonstration it just resets the running flag.
    """
    global system_running
    with state_lock:
        system_running = False
    print("Hardware stop invoked.")



def emergency_stop_system() -> None:
    """Placeholder for an immediate hardware shutdown.

    This should execute whatever procedures are necessary to instantly
    halt the machinery in unsafe conditions. In this example we simply
    reset the flag and log the event.
    """
    global system_running
    with state_lock:
        system_running = False
    print("Hardware emergency stop invoked!")



@app.route('/start', methods=['POST'])
def api_start():
    """Start the inspection system.

    Returns a JSON object confirming the operation.
    """
    start_system()
    return jsonify({'status': 'started'})



@app.route('/stop', methods=['POST'])
def api_stop():
    """Gracefully stop the inspection system.

    Returns a JSON object confirming the operation.
    """
    stop_system()
    return jsonify({'status': 'stopped'})



@app.route('/emergency_stop', methods=['POST'])
def api_emergency_stop():
    """Immediately stop the inspection system.

    Returns a JSON object confirming the operation.
    """
    emergency_stop_system()
    return jsonify({'status': 'emergency_stopped'})



@app.route('/measurements', methods=['GET'])
def get_measurements():
    """Return simulated measurement data.

    When the system is running this endpoint produces random height, ID,
    and OD values to mimic sensor output. When the system is not running
    all values are zero. This pattern can be replaced with actual sensor
    integration in a real deployment.
    """
    with state_lock:
        running = system_running
    if running:
        # Generate plausible measurement values with two decimal places
        height = round(random.uniform(10.0, 12.0), 2)
        inner_diameter = round(random.uniform(4.0, 6.0), 2)
        outer_diameter = round(random.uniform(6.0, 8.0), 2)
    else:
        height = inner_diameter = outer_diameter = 0.0
    return jsonify({'height': height, 'id': inner_diameter, 'od': outer_diameter})



if __name__ == '__main__':
    # Bind to all interfaces so Docker can map the port.
    app.run(host='0.0.0.0', port=5000, debug=True)
