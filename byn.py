from machine import Pin
import time
pin_a0 = Pin(15, Pin.IN)
pin_d0 = Pin(14, Pin.IN)

read_ana = 0
read_dig = 0

while True:
    print(f'Analog_r = {read_ana}')
    print(f'Digita_r = {read_dig}')
    
    read_ana = pin_a0.value()
    read_dig = pin_d0.value()
    time.sleep(1)