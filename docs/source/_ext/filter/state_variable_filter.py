import ctypes
import numpy as np
from numpy.ctypeslib import ndpointer
import matplotlib.pyplot as plt
from scipy import signal

# import C function
lib = ctypes.cdll.LoadLibrary("./my_lib.so")
state_variable_filter = lib.state_variable_filter
state_variable_filter.restype = None
state_variable_filter.argtypes = [ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                ctypes.c_size_t, 
                ctypes.c_double,
                ctypes.c_double,
                ctypes.c_size_t
                ]

# parameter
fs = 44100
fc = 1000
Q = 2

# create oscillator
t = np.arange(0, 0.01, 1/fs)
x = signal.sawtooth(2*np.pi*200*t)

# python code
alpha1 = 2*np.sin(np.pi*fc/fs)
alpha2 = 1/Q

b = [alpha1**2]
a = [1, alpha1**2+alpha1*alpha2-2, 1-alpha1*alpha2]
y_out = signal.lfilter(b, a, x)

# allocate arguments and call the C function
N = len(t)
zi = np.zeros(2)
buffer = x
state_variable_filter(buffer, zi, N, Q, fc, fs)

# plot the result
plt.plot(y_out, label="Python")
plt.plot(buffer, "--", label="C")
plt.grid()
plt.xlabel("$n$")
plt.ylabel("$y_l[n]$")
plt.legend()
plt.show()