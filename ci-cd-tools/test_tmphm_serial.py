
import unittest
import time
from tmphm_serial_interface import TmphmSerialInterface

def extract_temp(response):
    try:
        line = next(line for line in response.splitlines() if 'Temp=' in line)
        temp_str = line.split('Temp=')[1].split('C')[0].strip().replace('.', '')
        return int(temp_str)
    except:
        return None

def extract_humidity(response):
    try:
        line = next(line for line in response.splitlines() if 'Hum=' in line)
        hum_str = line.split('Hum=')[1].split('%')[0].strip().replace('.', '')
        return int(hum_str)
    except:
        return None

class TestTmphmSerial(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.interface = TmphmSerialInterface(port='COM4')  # Change as needed

    @classmethod
    def tearDownClass(cls):
        cls.interface.close()

    def test_get_meas_valid(self):
        self.interface.status()
        time.sleep(1.0)
        response = self.interface.get_last_meas(0)
        temp = extract_temp(response)
        hum = extract_humidity(response)
        self.assertIsNotNone(temp, "Temperature not found in output")
        self.assertIsNotNone(hum, "Humidity not found in output")
        self.assertTrue(200 <= temp <= 350, f"Temp out of range: {temp}")
        self.assertTrue(200 <= hum <= 900, f"Humidity out of range: {hum}")

    def test_sensor_reads_consistently(self):
        results = []
        for _ in range(3):
            time.sleep(1)
            response = self.interface.get_last_meas(0)
            temp = extract_temp(response)
            hum = extract_humidity(response)
            results.append((temp, hum))
        for temp, hum in results:
            self.assertIsNotNone(temp)
            self.assertTrue(200 <= temp <= 350)
            self.assertIsNotNone(hum)
            self.assertTrue(200 <= hum <= 900)

if __name__ == "__main__":
    unittest.main()
