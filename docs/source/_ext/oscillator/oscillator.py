import ctypes
import numpy as np
from numpy.ctypeslib import ndpointer
import matplotlib.pyplot as plt
from scipy import signal

# import C function
lib = ctypes.cdll.LoadLibrary("./my_lib.so")
oscillator = lib.oscillator
oscillator.restype = None
oscillator.argtypes = [ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                ctypes.c_double,
                ctypes.c_size_t,
                ctypes.POINTER(ctypes.c_double),
                ctypes.c_size_t]

# parameter
fs = 44100
f0 = 134.23

# create oscillator
t = np.arange(0, 0.02, 1/fs)
x = np.sin(2*np.pi*f0*t)

# allocate arguments and call the C function
N = len(t)
y = np.zeros(N)
currentIndex = ctypes.c_double(0.0)
oscillator(y, f0, fs, ctypes.pointer(currentIndex), N)

# plot the result
plt.plot(t, x, label="Python")
plt.plot(t, y, "--", label="C")
plt.grid()
plt.xlabel("$t$")
plt.ylabel("$y_l[n]$")
plt.xlim([0,t[-1]])
plt.legend()
plt.show()
