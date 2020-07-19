#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

from functools import wraps
import math
import random
import time
from neopixel import *
import argparse

# LED strip configuration:
LED_COUNT      = 240     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 50     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def musicServer(strip):
    host = '10.0.0.37'
    port = 8268
    address = (host, port)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(address)
    server_socket.listen(5)

    print("Listening for client . . .")
    conn, address = server_socket.accept()
    print("Connected to client at ", address)
    buffer_list = []
    offset = 0
    while True:
        output = conn.recv(4096);
        decoded = output.decode("utf-8")
        cava_values = decoded.split("\n")
        for x in range(len(cava_values)):
            bars = cava_values[x].split(";")
            if (len(bars) == 241):
                buffer_list.append(bars)
        # num_bars = LED_COUNT / len(cava_values)
        while len(buffer_list) > 0:
            total = 0
            for i in range(240):
                if (buffer_list[0][i] != ''):
                    val = int(buffer_list[0][i])
                    strip.setPixelColor(i, wheel((int(i * 256 / LED_COUNT) + val) & 255))
                    total += int(buffer_list[0][i])
            strip.setBrightness(total / 240)
            strip.show()
            buffer_list.pop(0)

def handleServerFIFO():
    print("Opening FIFO for reading")
    path = "/home/pi/alaunus/fifopipes/testpipe"
    try:
        os.remove(path)
        os.mkfifo(path)
        os.chmod(path, 0o777)
    except:
        print("FIFO already exists")
    with open(path) as fifo:
        print("FIFO opened")
        while True:
            data = fifo.read().decode(encoding='UTF-8')
            if len(data) != 0:
                global timeDelay 
                global redSlider
                global greenSlider
                global blueSlider

                global fadeColorFrom
                global fadeColorTo

                # Check boxes
                global customColorActive
                global fadeActive
                global simpleWaveActive
                global spreadoutActive
                global theaterChaseRainbowActive
                global rainbowActive
                global rainbowCycleActive
                vals = data.split()
                print(vals)
                try:
                    if (vals[0] == "timeSlider" and int(vals[1]) <= 2000):
                        timeDelay = int(vals[1])
                    else:
                        if vals[0] == "redSlider":
                            redSlider = int(vals[1])
                        elif vals[0] == "blueSlider":
                            blueSlider = int(vals[1])
                        elif vals[0] == "greenSlider":
                            greenSlider = int(vals[1])
                        elif vals[0] == "fadeColorFrom":
                            blueSlider = int(vals[1])
                        elif vals[0] == "fadeColorTo":
                            greenSlider = int(vals[1])
                        elif vals[0] == "customColorCheckBox":
                            customColorActive = bool(int(vals[1]))
                        elif vals[0] == "fadeCheckBox":
                            fadeActive = bool(int(vals[1]))
                        elif vals[0] == "simpleWaveCheckBox":
                            simpleWaveActive = bool(int(vals[1]))
                        elif vals[0] == "spreadoutCheckBox":
                            spreadoutActive = bool(int(vals[1]))
                        elif vals[0] == "theaterChaseRainbowCheckBox":
                            theaterChaseRainbowActive = bool(int(vals[1]))
                        elif vals[0] == "rainbowCheckBox":
                            rainbowActive = bool(int(vals[1]))
                        elif vals[0] == "rainbowCycleCheckBox":
                            rainbowCycleActive = bool(int(vals[1]))
                except:
                    print ""
                print 'Read: "{0}"'.format(data)


import os
import socket
import sys
import threading
import fileinput

timeDelay = 1000

customColorActive = False
fadeActive = True
simpleWaveActive = True
spreadoutActive = True
theaterChaseRainbowActive = True
rainbowActive = True
rainbowCycleActive = True

redSlider = 255
greenSlider = 0
blueSlider = 0


# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    parser.add_argument('-m', '--music', action='store_true', help='start server for sync to music')
    parser.add_argument('-k', '--kill', action='store_true', help='start server for sync to music')
    args = parser.parse_args()

    if args.kill:
        print "Performing colorwipe"
        colorWipe(strip, Color(0,0,0))
        sys.exit()
    elif args.music:
        serverThread = threading.Thread(target=musicServer, args=(strip,))
        serverThread.start()
    print ('Press Ctrl-C to quit.')
    fifoThread = threading.Thread(target=handleServerFIFO, args=())
    fifoThread.start()
    if not args.clear:
        print ('Use "-c" argument to clear LEDs on exit')

    try:
        while not args.music:
            # Check boxes
            if (customColorActive):
                customColor(strip)
            print (customColorActive, fadeActive, simpleWaveActive, spreadoutActive, theaterChaseRainbowActive, rainbowActive, rainbowCycleActive)
            if (fadeActive):
                fade(strip, 20)
            if (simpleWaveActive):
                simpleWave(strip, 0.01,5, 20, 10)
            if (spreadoutActive):
                spreadout(strip)
            if (theaterChaseRainbowActive):
                theaterChaseRainbow(strip)
            if (rainbowActive):
                rainbow(strip)
            if (rainbowCycleActive):
                rainbowCycle(strip)
                
    except KeyboardInterrupt:
        socket.close()
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)

