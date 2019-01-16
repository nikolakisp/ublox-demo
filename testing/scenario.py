import time
import Spanner
from Testboard import Testboard

testboard = Testboard("testboard_name")
# Our device's Input (GPIO2 - SW2) will be connected the Testboard's Pin D5, making it our
# Output Pin
OUTPUT_PIN = "D5"

# Our device's Output Pin (GPIO11 - Led D1) will be connected to the Testboard's D6, making it
# our Input Pin
INPUT_PIN = "D6"
def button_press():
    # check PIN state
    status = testboard.digitalWrite(OUTPUT_PIN,'LOW')
    Spanner.assertEqual(status,1)

def button_release():
    # check PIN state
    status = testboard.digitalWrite(OUTPUT_PIN,'HIGH')
    Spanner.assertEqual(status,1)

def is_led_on():
    # check PIN state
    status = testboard.digitalRead(INPUT_PIN)
    Spanner.assertEqual(status,1)

def is_led_off():
    # check PIN state
    status = testboard.digitalRead(INPUT_PIN)
    Spanner.assertEqual(status,0)

def validate_led_on_button_press():
    for i in range(10):
        button_press()
        is_led_on()
        time.sleep(3)
        button_release()
        is_led_off()
        time.sleep(3)

if __name__ == "__main__":
    validate_led_on_button_press()
