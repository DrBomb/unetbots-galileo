import time
from threading import Thread
from wiringx86 import GPIOGalileo as gpio

GPIO = gpio(debug=True)
pin = 8
GPIO.pinMode(pin,GPIO.INPUT)

start = 0
finish = 0
state = 0

def worker():
  print "HI!"
  prevState = GPIO.digitalRead(pin)
  stage = 0
  while True:
   if(GPIO.digitalRead(pin) ==0):
    print "Low edge"
    if(stage == 0):
     start = time.time()
     while(GPIO.digitalRead(pin) 
==0):
      pass
     time.sleep(0.2)
     stage = 1
    else:
     finish = time.time()
     diff = finish - start
     print "{}".format(repr(diff))
     while(GPIO.digitalRead(pin) == 
0):
      pass
     time.sleep(0.2)
     stage = 0

if (__name__=="__main__"):
 print "Comienzo del programa"
 t = Thread(target=worker)
 t.daemon = True
 t.start()
 while True:
  pass
