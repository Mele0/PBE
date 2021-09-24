#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)

class Rfid_rc522:
    def scan_uid(self):
        reader = SimpleMFRC522()
        uid = reader.read()
        return uid[0]
    
if __name__ == "__main__":
        print('Please insert a student card')
        while True:
            try:    
                    rf = Rfid_rc522()
                    uid = rf.scan_uid()
                    print(hex(uid).upper())
                    time.sleep(2)
            finally:
                    GPIO.cleanup()
                
