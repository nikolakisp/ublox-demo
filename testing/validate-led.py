import time
import Spanner
from Testboard import Testboard

testboard = Testboard("testboard-ublox")

# Our device's Input (GPIO2 - SW2) will be connected the Testboard's Pin D5, making it our
# output Pin
OUTPUT_PIN = "D5"

# Our device's Output Pin (GPIO11 - Led D1) will be connected to the Testboard's D6, making it
# our Input Pin
INPUT_PIN = "D6"

def validate_led_on_button_press():

        # button press
        status = testboard.digitalWrite(OUTPUT_PIN,'LOW')
        #Spanner.assertEqual(status,1)
        
        # is LED on?
        status = testboard.digitalRead(INPUT_PIN)
        Spanner.assertEqual(status,1)

        time.sleep(3)

        # button release
        status = testboard.digitalWrite(OUTPUT_PIN,'HIGH')
        #Spanner.assertEqual(status,1)

        # is LED off?
        status = testboard.digitalRead(INPUT_PIN)
        #Spanner.assertEqual(status,0)
        
        time.sleep(3)

if __name__ == "__main__":
    for i in range(5):
        print("### Testing retry %d of 5 ###" % (i+1))
        validate_led_on_button_press()
