import time
import sys
import RPi.GPIO as GPIO

power_on = '1001100000001000111111101'
mode_increment = '1001100000001000111110101'
speed_decrement = '1001100000001000111110001'
demo = '1001100000001000111101111'
speed_increment = '1001100000001000111101101'
color_increment = '1001100000001000111101011'
mode_decrement = '1001100000001000111101001'
bright_increment = '1001100000001000111100111'
color_decrement = '1001100000001000111100101'
white_button = '1001100000001000111100011'
bright_decrement = '1001100000001000111100001'
red_button = '1001100000001000111011111'
green_button = '1001100000001000111011101'
purple_button = '1001100000001000111011011'
yellow_button = '1001100000001000111011001'
blue_button = '1001100000001000111010111'
pink_button = '1001100000001000111010101'

short_delay = 0.00034
long_delay = 0.00115
extended_delay = 0.01221

NUM_ATTEMPTS = 2
TRANSMIT_PIN = 23

def transmit_code(code):
    '''Transmit a chosen code string using the GPIO transmitter'''
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRANSMIT_PIN, GPIO.OUT)
    for t in range(NUM_ATTEMPTS):
        for i in code:
            if i == '1':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(short_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(long_delay)
            elif i == '0':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(long_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(short_delay)
            else:
                continue
        GPIO.output(TRANSMIT_PIN, 0)
        time.sleep(extended_delay)
    GPIO.cleanup()

if __name__ == '__main__':
    for argument in sys.argv[1:]:
        exec('transmit_code(' + str(argument) + ')')

