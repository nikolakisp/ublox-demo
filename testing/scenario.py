import time
import Spanner
from Testboard import Testboard

testboard = Testboard("myd")

INPUT_PIN = "D7"    #led of device => input pin of testboard
OUTPUT_PIN = "D5"   #input of device => output pin of testboard
def led_on():
    # check PIN state
    status = testboard.digitalRead(INPUT_PIN)
    Spanner.assertEqual(status,1)

def button_press():
    # check PIN state
    status = testboard.digitalWrite(OUTPUT_PIN,'LOW')
    Spanner.assertEqual(status,1)
    
    
def button_release():
    # check PIN state
    status = testboard.digitalWrite(OUTPUT_PIN,'HIGH')
    Spanner.assertEqual(status,1)



if __name__ == "__main__":
    start_time = time.time()%60     #time start to seconds
    i=0
    while 1:
        i=i+1
        button_press()             #button is pressed
        time.sleep(2)
        led_on()                    #after 2 seconds led is on
        time.sleep(4)
        button_release()            #after 4 second button is released and led is off
        time.sleep(4)
        end_time = time.time()%60   
        stop = int(end_time - start_time)
        print (stop)
#         if stop == 20 :             #after 60 second stop 
#             break
        break
    print("blue")
