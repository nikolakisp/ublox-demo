import time
import Spanner
from Testboard import Testboard

testboard = Testboard("myd")

INPUT_PIN = "D7"    #led of device => input pin of testboard
OUTPUT_PIN = "D5"   #input of device => output pin of testboard
def led_on():
    # check PIN state
    value = testboard.digitalRead(INPUT_PIN)

def button_press():
    # check PIN state
    value = testboard.digitalWrite(OUTPUT_PIN,'LOW')
    Spanner.assertTrue(value)
    
    
def button_release():
    # check PIN state
    value = testboard.digitalWrite(OUTPUT_PIN,'HIGH')
    Spanner.assertFalse(value)



if __name__ == "__main__":
    start_time = time.time()%60     #time start to seconds
    i=0
    while 1:
        i++
        button_press()             #button is pressed
        time.sleep(2)
        led_on()                    #after 2 seconds led is on
        time.sleep(4)
        button_release()            #after 4 second button is released and led is off
        time.sleep(4)
        end_time = time.time()%60   
        stop = int(end_time - start_time)
        print (i)
        if stop == 60 :             #after 60 second stop 
            break
    print("blue")
