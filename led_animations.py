from led_animation import LEDAnimation
from neopixel import *
import time
# LED strip configuration:
LED_COUNT      = 240     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 50     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()
# Define functions which animate LEDs in various ways.
def colorWipe(color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) +j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    # Rainbow movie theater light style chaser animation.
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def spreadout(strip, wait_ms=20, iterations=5):
    middle = strip.numPixels()/2
    for j in range(iterations):
        for i in range(middle):
            strip.setPixelColor(middle + i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
            strip.setPixelColor(middle - i, wheel((int(i * 256 / strip.numPixels()) - j) & 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
        for x in range(middle):
            strip.setPixelColor(x, wheel((int(x * 256 / strip.numPixels()) + j) & 255))
            strip.setPixelColor(strip.numPixels() - x, wheel((int(strip.numPixels() - x * 256 / strip.numPixels()) + j) & 255))
            strip.show()
            time.sleep(wait_ms/1000.0)

def randColor():
    return Color(random.randint(0,255),random.randint(0,255), random.randint(0, 255)) 

# Define functions which animate LEDs in various ways.
def customColor(strip, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for c in range(250):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(greenSlider, redSlider, blueSlider))
        strip.show()
        time.sleep(wait_ms/1000.0)

def simpleWave(strip, rate, cycles, scale, wait):
    pos=0.0;
    for x in range(strip.numPixels() * cycles):
        pos = pos+rate
        for i in range(strip.numPixels()):
            level = math.sin(i+pos * scale) * 127 + 128
            strip.setPixelColor(i, wheel(int(level)))
        strip.show()
        time.sleep(wait/1000.0)

def fade(strip, cycles, wait_ms=5):
    cRedVal = random.randint(0,255)
    cGreenVal = random.randint(0,255)
    cBlueVal = random.randint(0,255)

    dRedVal = random.randint(0,255)
    dGreenVal = random.randint(0,255)
    dBlueVal = random.randint(0,255)
    for c in range(cycles):
        while ((cRedVal, cGreenVal, cBlueVal) != (dRedVal, dGreenVal, dBlueVal)):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, Color(cGreenVal, cRedVal, cBlueVal))
            if (cRedVal > dRedVal):
                cRedVal -= 1
            elif (cRedVal < dRedVal):
                cRedVal += 1
            if (cGreenVal > dGreenVal):
                cGreenVal -= 1
            elif (cGreenVal < dGreenVal):
                cGreenVal += 1
            if (cBlueVal > dBlueVal):
                cBlueVal -= 1
            elif (cBlueVal < dBlueVal):
                cBlueVal += 1
            strip.show()
            time.sleep(timeDelay/100000.0)
        dRedVal = random.randint(0,255)
        dGreenVal = random.randint(0,255)
        dBlueVal = random.randint(0,255)

test = LEDAnimation('colorWipe', colorWipe)
print(test.name)
test.run(Color(255, 0, 0))
