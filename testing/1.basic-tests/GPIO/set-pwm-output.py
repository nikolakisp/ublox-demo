# This example will set one of our Testboard's outputs, and the pwmWrite
# function, to drive a PWM signal.
#
# The goal of this example is to show you how you can drive a digital input on
# your device that expects a PWM signal from the Testboard.
#
# In our particular example, we are only setting a value and not asserting
# anything. Of course this would never be a real world example, it's only for
# educational purposes

import time
import spanner
import Testboard

# Our Product's Input will be connected the Testboard's Pin D0, making it our
# Output Pin
OUTPUT_PIN = "D0"

testboard = Testboard("Wubby_Test")

def set_pwm_output():
    # In this example, we'll give it a 50% duty cycle. Our pwmWrite takes values
    # from 0 to 4095, so a 50% duty cycle would be 2047.
    value=testboard.pwmWrite(OUTPUT_PIN, 2047)
    # See also pwmWrite(pin, value, frequency)
    
    spanner.assertFalse(value)

if __name__ == "__main__":

    spanner.runTest(set_pwm_output())

# NOT READY
