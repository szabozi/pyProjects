from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Device
import socket


"""
To make the remote GPIO connection there are a few steps that need to be done:

1 - Install pigpio on the rPi, using the following commands:
    sudo apt update
    sudo apt install pigpio python3-pigpio
    sudo systemctl enable pigpiod  # Enable pigpio daemon to start on boot
    sudo systemctl start pigpiod   # Start pigpio daemon immediately

2 - Install pigpio on the pc, using the following command
    pip install pigpio
    
3 - Run this script to check if connection is established correctly
"""

# Raspberry Pi's IP address
rPi_ip = "192.168.0.227"

try:
    # Setting up remote GPIO connection
    Device.pin_factory = PiGPIOFactory(host=rPi_ip)

    # Trying to access a GPIO pin
    pin = Device.pin_factory.pin(17)

    print("\033[92m\nRemote GPIO connection is successful and ready for use.\n\033[0m")

except ImportError as error:
    print("\033[91mImport error: Required library not found.\033[0m")
    print(error)
except socket.error as error:
    print("\033[91mNetwork error: Unable to connect to the Raspberry Pi.\033[0m")
    print(error)
except Exception as error:
    print("\033[91mAn unexpected error occured:\033[0m")
    print(error)



