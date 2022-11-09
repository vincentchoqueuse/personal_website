import numpy as np

N = 128
n = np.arange(N)
x = np.sin(2*np.pi*n/N)

np.savetxt("data.txt", x, newline=", ")