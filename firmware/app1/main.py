# GPIOs Example - Showcase the GPIO module
from time import sleep
from hardware import gpio
import led

## Create a new led object using the pin 11
led1 = led.LED(11,1)

# Set GPIO 2 as input
sw2 = gpio(2, gpio.GPIO_MODE_INPUT_PULLUP)

while True:
    # Toggle Led based on SW2 Button
    if (str(sw2.read()) == "1"):
        led1.OFF()
    else:
        led1.ON()
    sleep(3)
    
