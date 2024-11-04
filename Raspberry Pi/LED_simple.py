from gpiozero import LED
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory(host='192.168.0.86')

led = LED(25, pin_factory=factory)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
