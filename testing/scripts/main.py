import time
from hardware import gpio

print ("Wubby Project")
print ("GPIO Example")

## Create a new gpio object
led = gpio(11,gpio.GPIO_MODE_OUTPUT_PULLDOWN)

led.write(0)

## Read Value
while True:
        led.toggle()
        time.sleep(1000)
