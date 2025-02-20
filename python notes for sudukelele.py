#code to read from pin for mic? will need to test cause this will be pwm


#!/usr/bin/env python

from time import sleep  # Allows us to call the sleep function to slow down our loop
import RPi.GPIO as GPIO # Allows us to call our GPIO pins and names it just GPIO
 
GPIO.setmode(GPIO.BCM)  # Set's GPIO pins to BCM GPIO numbering
INPUT_PIN = 4           # Sets our input pin, in this example I'm connecting our button to pin 4. Pin 0 is the SDA pin so I avoid using it for sensors/buttons
GPIO.setup(INPUT_PIN, GPIO.IN)  # Set our input pin to be an input

# Create a function to run when the input is high
def inputLow(channel):
    print('0');

GPIO.add_event_detect(INPUT_PIN, GPIO.FALLING, callback=inputLow, bouncetime=200) # Wait for the input to go low, run the function when it does

# Start a loop that never ends
while True:
    print('3.3');
    sleep(1);           # Sleep for a full second before restarting our loop



#end code to read from mic pin

#to output audio it seems we need to use an audio card so lets not worry about that or input quite yet
# we can just gather noises and get button code

import RPi.GPIO as GPIO
import time

# Set up GPIO numbering mode
GPIO.setmode(GPIO.BCM)

# Set up button pins //TODO figure out tf you actually want to use
sockeye = 1
king = 2
silver = 3
pink = 4
chum = 5
sockeyeLight = 6
kingLight = 7
silverLight = 8
pinkLight = 9
chumLight = 10
10
GPIO.setup(sockeye, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sockeyeLight,GPIO.OUT)

def sockeye_callback(channel):#will eventually need functions to light up all of em and whatnot, might be able to pass pin as a parameter
    GPIO.output(sockeye,GPIO.HIGH)#turn light on
    time.sleep(0.5)
    GPIO.output(sockeye,GPIO.HIGH)

# Add event detection
GPIO.add_event_detect(sockeye, GPIO.FALLING, callback=sockeye_callback, bouncetime=200)

try:
    print("Waiting for button press...")
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
