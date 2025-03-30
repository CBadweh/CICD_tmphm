#  Run with: python -m unittest test_tmphm
# This will run the tests in the file test_tmphm.py. The output will look like this:

import time
import unittest

# Mock or import the tmphm C module interface
# In a real setup, these would come from a Python binding (like cffi or ctypes), or serial commands to target
from mock_tmphm_interface import (
    tmphm_init,
    tmphm_start,
    tmphm_get_last_meas,
    inject_crc_error,
    reset_sensor_state,
)

class TestTmphmUnit(unittest.TestCase):
    def test_state_reset_after_fault(self):
        reset_sensor_state()
        inject_crc_error(True)
        tmphm_start(0)
        time.sleep(0.1)  # wait for state machine
        meas = tmphm_get_last_meas(0)
        self.assertIsNone(meas, "Measurement should fail after CRC error")
        inject_crc_error(False)

class TestTmphmIntegration(unittest.TestCase):
    def test_get_meas_valid(self):
        reset_sensor_state()
        tmphm_init(0)
        tmphm_start(0)
        time.sleep(1.0)  # wait for at least one polling cycle
        meas = tmphm_get_last_meas(0)
        self.assertIsNotNone(meas, "Expected a valid measurement")
        self.assertTrue(0 < meas['temp'] < 500, "Temp range sanity check")
        self.assertTrue(0 <= meas['hum'] <= 1000, "Humidity range sanity check")

class TestTmphmSystem(unittest.TestCase):
    def test_sensor_reads_correctly(self):
        reset_sensor_state()
        tmphm_init(0)
        tmphm_start(0)
        results = []
        for _ in range(3):
            time.sleep(1)
            meas = tmphm_get_last_meas(0)
            results.append(meas)

        for meas in results:
            self.assertIsNotNone(meas)
            self.assertTrue(0 < meas['temp'] < 500)
            self.assertTrue(0 <= meas['hum'] <= 1000)

if __name__ == '__main__':
    unittest.main()
