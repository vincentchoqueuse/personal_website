Call C function in Python
=========================

In this tutorial, I show how to create a C function and how to call it from Python. More specifically, I create a function 
to compute the cosine value for each element of a :code:`numpy` array.

C Code 
------

First, we need to create a :code:`my_lib.c` file with a single function called :math:`my_cos`.

.. code :: c

    #include <math.h>

    void my_cos(double *in_array, double *out_array, int size){
        int i;
        for(i=0; i<size; i++){
            out_array[i] = cos(in_array[i]);
        }
    }

Then, we need to create a share library by running the following command in your terminal

.. code ::

    $ gcc -fPIC -shared my_lib.c -o my_lib.so 

This command must create a file called :code:`my_lib.so`

Calling your function 
---------------------

To call your function, we need to import the library / function using the module :code:`ctypes`. In the following code, I 
create a instantaneous phase vector and call the C function :code:`my_cos` to compute the cosinus for each element.
The output array is then plotted using matplotlib.

.. code :: c

    import ctypes
    import numpy as np
    from numpy.ctypeslib import ndpointer
    import matplotlib.pyplot as plt

    # import C function
    lib = ctypes.cdll.LoadLibrary("./my_lib.so")
    my_cos = lib.my_cos
    my_cos.restype = None
    my_cos.argtypes = [ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                    ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                    ctypes.c_size_t]

    # create a nd array  
    Fe = 1000
    t = np.arange(0, 1, 1/Fe)
    phase = 2*np.pi*t

    # allocate arguments and call the C function
    N = len(t)
    out_data = np.zeros(N)
    my_cos(phase, out_data, N)

    # plot the result
    plt.plot(t, out_data)
    plt.xlabel("time [s]")
    plt.show()