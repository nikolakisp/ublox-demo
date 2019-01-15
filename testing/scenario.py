import time
from datetime import datetime
import Spanner
from Testboard import Testboard

testboard = Testboard("myd")

OUTPUT_PIN = "D5"   #input of device => output pin of testboard
INPUT_PIN = "D7"    #led of device => input pin of testboard
def button_press():
    # check PIN state
    status = testboard.digitalWrite(OUTPUT_PIN,'LOW')
    Spanner.assertEqual(status,1)
    
    
def button_release():
    # check PIN state
    status = testboard.digitalWrite(OUTPUT_PIN,'HIGH')
    Spanner.assertEqual(status,1)

def led_on(is_on):
    # check PIN state
    value = testboard.digitalRead(INPUT_PIN)
    Spanner.assertEqual(value,is_on)

if __name__ == "__main__":
    start_time = datetime.now()     #time start to seconds
    while 1:
        button_press()             #button is pressed -> led is on
        led_on(1)
        time.sleep(3)
        button_release()            #after 3 second button is released -> led is off
        led_on(0)
        time.sleep(3)
        end_time = datetime.now()   
        stop = end_time - start_time
        
        if stop.seconds >= 18 :            
            break
