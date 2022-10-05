import RPi.GPIO as GPIO
import time
LED = 40
GPIO.setwarnmings(Flase)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)

while True:
    GPIO.output(lED, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED,GPIO,LOW)
    time.sleep(1)
    
    
    
    from gpiozero import BUtton, TrafficLights, Buzzer
    from time import sleep
    
    buzzer = Buzzer(15)
    button = Button(21)
    lights = TrafficLights(25,8,7)
    
    while True:
        button.wait_for_press()
        buzzer.on()
        light.green.on()
        sleep(1)
        lights.amber.on()
        sleep(1)
        light.red.on()
        sleep(1)
        lights.off()
        buzzer.off()
    
