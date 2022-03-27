import RPi.GPIO as GPIO 
from mfrc522 import SimpleMFRC522

def GPIO_init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(10,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(8,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    
def get_nfc():
    reader = SimpleMFRC522()
    try:
        id, text = reader.read()
        return text
    except:
        return -1

def write_nfc(record_id):
    reader  =SimpleMFRC522()
    try:
        print("Place tag to write")
        reader.write(record_id)
        print("Written")
    except:
        print("Error has occured")

