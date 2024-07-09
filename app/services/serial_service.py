import serial
from threading import Thread

def read_serial():
    ser = serial.Serial(9600)  
    while True:
        line = ser.readline()
        print(line)

def start_serial_thread():
    serial_thread = Thread(target=read_serial)
    serial_thread.start()
