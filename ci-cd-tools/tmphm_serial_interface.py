
import serial
import time

class TmphmSerialInterface:
    def __init__(self, port='COM4', baudrate=115200, timeout=2):
        self.ser = serial.Serial(port, baudrate, timeout=timeout)
        time.sleep(2)  # allow time for board to reboot/reset if needed
        self._flush_startup()

    def _flush_startup(self):
        '''Flush initial messages from the board'''
        if self.ser.in_waiting:
            print("Flushing:", self.ser.read(self.ser.in_waiting).decode(errors='ignore'))

    def send_command(self, command):
        self.ser.write((command + '\r\n').encode())
        time.sleep(0.1)
        return self.read_response()

    def read_response(self):
        response = b''
        start = time.time()
        while (time.time() - start) < 1.5:
            if self.ser.in_waiting:
                response += self.ser.read(self.ser.in_waiting)
            if b'> ' in response:
                break
            time.sleep(0.05)
        return response.decode(errors='ignore')

    def get_last_meas(self, instance_id=0):
        resp = self.send_command(f"tmphm test lastmeas {instance_id}")
        print(resp)
        return resp

    def status(self):
        resp = self.send_command("tmphm status")
        print(resp)
        return resp

    def set_meastime(self, instance_id=0, ms=50):
        resp = self.send_command(f"tmphm test meastime {instance_id} {ms}")
        print(resp)
        return resp

    def close(self):
        self.ser.close()


if __name__ == "__main__":
    interface = TmphmSerialInterface(port='COM4')  # Change COM port as needed
    print("=== TMPHM Sensor CLI Interface ===")
    interface.status()
    time.sleep(1)
    interface.get_last_meas()
    interface.set_meastime(0, 100)
    interface.close()
