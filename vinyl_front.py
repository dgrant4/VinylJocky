import info_get as api_get
import pi_interface
import RPi.GPIO as GPIO
import sys
import os


def start_up():
    print("Welcome to the Vinyl Jocky")
    print("Press the Load Button to get Record Info")

def load_callback(channel):
    print("Looking for tag")
    record_id=pi_interface.get_nfc()
    record_id_clean = record_id.rstrip()
    record_info= api_get.get_label(record_id_clean)
    print("%s - %s" %(record_info.artists[0].name, record_info.title))

def write_callback(channel):
    print("Time to write")
    record_id = input("Enter record ID# :")
    pi_interface.write_nfc(record_id)

def main():
    pi_interface.GPIO_init()
    start_up()
    GPIO.add_event_detect(10, GPIO.RISING, callback = load_callback, bouncetime =500 )
    GPIO.add_event_detect(8, GPIO.RISING, callback = write_callback, bouncetime =300 )
    while True:
        pass

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print('Interupted')
        try:
            sys.exit(1)
        except SystemExit:
            os._exit(1)
