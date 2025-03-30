
import unittest
import time
from tmphm_serial_interface import TmphmSerialInterface

def extract_age(response):
    try:
        line = next(line for line in response.splitlines() if 'age=' in line)
        age_str = line.split('age=')[1].split('ms')[0].strip()
        return int(age_str)
    except:
        return None

class TestTmphmAgeReset(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.interface = TmphmSerialInterface(port='COM4')  # adjust if needed

    @classmethod
    def tearDownClass(cls):
        cls.interface.close()

    def test_tmphm_meas_age_resets(self):
        print("Testing: Measurement age resets after new sensor reading...")
        self.interface.status()
        time.sleep(1.0)

        # First read (expect older age)
        r1 = self.interface.get_last_meas(0)
        age1 = extract_age(r1)
        print(f"First read age: {age1} ms")
        self.assertIsNotNone(age1)
        time.sleep(1.5)

        # Second read (age continues to grow)
        r2 = self.interface.get_last_meas(0)
        age2 = extract_age(r2)
        print(f"Second read age: {age2} ms")
        self.assertGreater(age2, age1)

        # Wait for next polling cycle (meas_time = 100ms, so wait >1s)
        time.sleep(1.5)

        # Third read (expect fresh reading with low age)
        r3 = self.interface.get_last_meas(0)
        age3 = extract_age(r3)
        print(f"Third read age (after refresh): {age3} ms")
        self.assertLess(age3, age2)

if __name__ == "__main__":
    unittest.main()
