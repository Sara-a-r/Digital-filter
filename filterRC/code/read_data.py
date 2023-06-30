import serial
import time
import numpy as np

# declare variables to be used
n_data = 578  # number of data to get from Arduino
single_read = []
list_data = []

# ----------------Read data from Arduino---------------- #

# establish serial connection to Arduino
arduino = serial.Serial('COM4', 9600)
time.sleep(5)

print('Start acquisition...')

for i in range(0, n_data):
    # read all data until EOL ('\n')
    arduino_data = arduino.readline()
    # convert data (bytes) in str
    decoded_values = str(arduino_data[0:len(arduino_data)].decode())
    # split values (heater's state x Troom)
    single_read = decoded_values.split('x')
    # extract values
    for data in single_read:
        list_data.append(float(data)) #it was float

arduino.close()

# reshape list of data in a matrix (n_data, 2)
matrix_data = (np.array(list_data)).reshape(n_data, 2)

# save arduino data in a file txt
np.savetxt('../data/10Hz500_3.txt',matrix_data, fmt='%d')