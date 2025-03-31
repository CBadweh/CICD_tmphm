# This file contains a mock implementation of the tmphm_interface module.
# It is intended to be used in the CI/CD pipeline to test the application
# without the need of a real sensor.

import random

_state = {
    "crc_error": False,
    "meas_ready": False,
    "meas": {"temp": None, "hum": None}
}

def reset_sensor_state():
    _state["crc_error"] = False
    _state["meas_ready"] = False
    _state["meas"] = {"temp": None, "hum": None}

def inject_crc_error(enable):
    _state["crc_error"] = enable

def tmphm_init(instance_id):
    # Simulate init process
    return 0

def tmphm_start(instance_id):
    # Simulate timer starting and polling cycle
    if _state["crc_error"]:
        _state["meas_ready"] = False
        _state["meas"] = {"temp": None, "hum": None}
    else:
        temp = random.randint(200, 300)  # 20.0 to 30.0 °C
        hum = random.randint(400, 600)   # 40.0 to 60.0 %
        _state["meas"] = {"temp": temp, "hum": hum}
        _state["meas_ready"] = True

def tmphm_get_last_meas(instance_id):
    if _state["meas_ready"]:
        return _state["meas"]
    return None
