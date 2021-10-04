#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)

class Rfid_rc522:
    def scan_uid(self):
        reader = SimpleMFRC522()
        uid = reader.read()
        return uid[0]
    
if __name__ == "__main__":
        print('Please insert your card')
        try:    
               rf = Rfid_rc522()
               uid = rf.scan_uid()
               print(hex(uid).upper()[2:10])
                
        finally:
               GPIO.cleanup()
