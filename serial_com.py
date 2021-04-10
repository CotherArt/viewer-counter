# Importing Libraries
import serial
from time import sleep
arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)
mesage = ''
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    sleep(0.05)
    data = arduino.readline()
    return data

# code to test
def main():
    while True:
        num = input("Enter a number: ") # Taking input from user
        value = write_read(num)
        print(value) # printing the value

if __name__ == "__main__":
    main()