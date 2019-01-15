import time
import led

## Create a new led object using the pin 11
led1 = led.LED(11,1)

while True:
    # Change LED state
    led1.ON()

    time.sleep(4000)

    led1.OFF()

    time.sleep(1000)
