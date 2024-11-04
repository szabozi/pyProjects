from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory(host='192.168.0.86')

button = Button(2, pin_factory=factory)

while True:
    button.wait_for_press()
    print("You pushed me!")
