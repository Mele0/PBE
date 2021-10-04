import RPi.GPIO as GPIO
from mfrc522 import MFRC522
GPIO.setwarnings(False)

class Rfid_rc522:
    def read_uid(self):
        MIFAREReader = MFRC522()
        while True:
            (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
            (status,uid) = MIFAREReader.MFRC522_Anticoll()
            
            if status == MIFAREReader.MI_OK:
                return "%s%s%s%s" % (hex(uid[0]).upper()[2:], hex(uid[1]).upper()[2:], hex(uid[2]).upper()[2:], hex(uid[3]).upper()[2:])

if __name__ == "__main__":
    print('Enter your University card')
    uid = Rfid_rc522().read_uid()
    print('Welcome', uid)
