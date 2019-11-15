from gpiozero import LED # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
import random


led1 = LED(14)
led2 = LED(15)
led3 = LED(18)
led4 = LED(23)
led5 = LED(24)
led6 = LED(25)


for x in range(0, 1000, 1):
    k = random.randint(1, 6)
    if k == 1:
        led1.on()
        sleep(0.2)
        led1.off()
        sleep(0.2)
    if k == 2:
        led2.on()
        sleep(0.2)
        led2.off()
        sleep(0.2)
    if k == 3:
        led3.on()
        sleep(0.2)
        led3.off()
        sleep(0.2)
    if k == 4:
        led4.on()
        sleep(0.2)
        led4.off()
        sleep(0.2)
    if k == 5:
        led5.on()
        sleep(0.2)
        led5.off()
        sleep(0.2)
    if k == 6:
        led6.on()
        sleep(0.2)
        led6.off()
        sleep(0.2)