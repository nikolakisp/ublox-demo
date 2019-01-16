import time
import Spanner
from Testboard import Testboard

testboard = Testboard("myd")

OUTPUT_PIN = "D5"   #input of device => output pin of testboard
INPUT_PIN = "D6"    #led of device => input pin of testboard
def button_press():
    # check PIN state
    status = testboard.digitalWrite(OUTPUT_PIN,'LOW')
    Spanner.assertEqual(status,1)
    
    
def button_release():
    # check PIN state
    status = testboard.digitalWrite(OUTPUT_PIN,'HIGH')
    Spanner.assertEqual(status,1)

def led(value):
    # check PIN state
    status = testboard.digitalRead(INPUT_PIN)
    Spanner.assertEqual(status,value)

if __name__ == "__main__":
    for i in range(10):
        button_press()             #button is pressed -> led is on
        led(1)
        time.sleep(3)
        button_release()            #after 3 second button is released -> led is off
        led(0)
        time.sleep(3)
