import numpy as np
import pylab as pyl
import matplotlib.pyplot as plt

# load data
t, V = pyl.loadtxt('../data/2Hz500_2.txt',unpack=True)  #t is given in microseconds
                                                     #V is given in bit

#data 'reduction'
t = t *1e-6         #convert time in seconds
V = V * 5 / 1023    #convert V in Volt
V = V[15:]          #cut first data
t = t[15:]          #cut first data
print(t[52]-t[51])


# let's see data: scatter plot
plt.rc('font',size=10)
plt.figure(figsize=(12,6))
plt.title("Arduino sine wave generator")
plt.xlabel("time [s]")
plt.ylabel("V[V]")
plt.grid(color='gray',linewidth='0.2')
plt.minorticks_on()

plt.plot(t,V, linestyle = '-', linewidth = '0.5', marker = '.', color = 'black', label = 'f=2Hz, f$_s$=500Hz')
plt.legend(loc = 'lower right')

#save the plot
#plt.savefig("TcontrolArduino1.png")
plt.show()