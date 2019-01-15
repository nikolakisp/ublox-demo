import time
from datetime import datetime
import Spanner
from Testboard import Testboard

testboard = Testboard("myd")

OUTPUT_PIN = "D5"   #input of device => output pin of testboard
def button_press():
    # check PIN state
    status = testboard.digitalWrite(OUTPUT_PIN,'LOW')
    Spanner.assertEqual(status,1)
    
    
def button_release():
    # check PIN state
    status = testboard.digitalWrite(OUTPUT_PIN,'HIGH')
    Spanner.assertEqual(status,1)



if __name__ == "__main__":
    start_time = datetime.now()     #time start to seconds
    while 1:
        button_press()             #button is pressed
        time.sleep(4)
        button_release()            #after 4 second button is released and led is off
        time.sleep(4)
        end_time = datetime.now()   
        stop = end_time - start_time
        print (stop.seconds)
        button_press()             #button is pressed
        time.sleep(4)
        button_release()            #after 4 second button is released and led is off
        time.sleep(4)
        end_time = datetime.now()  
        stop = end_time - start_time
        print (stop.seconds)
        if stop.seconds >= 15 :             #after 60 second stop 
            break
