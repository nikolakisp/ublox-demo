# GPIOs Example - Showcase the GPIO module
import time
from hardware import gpio
## Create a new led object using the pin 11
# wait for Testboard's input
pin1 = gpio(2, gpio.GPIO_MODE_INPUT_PULLUP)
while 1:
    if str(pin1.read()) == "1":
        gpio.gpioWrite(12,1)    # led
        time.sleep(3000)
    else :
        gpio.gpioWrite(12,0)
        time.sleep(1000)
