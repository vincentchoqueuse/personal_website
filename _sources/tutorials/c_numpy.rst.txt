Calling a C function from Python
==============================

In this tutorial, I show how to create a C function and how to call it from Python. 
This case arises in situations where we want to analyse the output of a C function using python modules such as Numpy or 
matplotlib. In particular, this approach can help you to debug your signal processing algorithms. 

In this tutorial, I consider a simple case where we want to compute the cosine value for each element of a :code:`numpy` array.
Note that this computation can be performed using the numpy function :code:`cos` directly, but for the sake of illustration, we will implement 
the cos function in pure C.

C Code 
------

First, we need to create a :code:`my_lib.c` file with a single function called :math:`my_cos`. The 
:math:`my_cos` function contains a for loop function to compute the cosine for each element of an input array :code:`*in_array`.

.. code :: c

    #include <math.h>

    void my_cos(double *in_array, double *out_array, int size){
        int i;
        for(i=0; i<size; i++){
            out_array[i] = cos(in_array[i]);
        }
    }

Then, we need to create a shared library by running the following command in your terminal

.. code ::

    $ gcc -fPIC -shared my_lib.c -o my_lib.so 

This command creates a file called :code:`my_lib.so`

Calling your function 
---------------------

To call our function, we need to create a python script called :code:`show_sine.py`. In this python script, we import the C library / function using the module :code:`ctypes`. 
Specifically, this script creates an instantaneous phase vector :code:`phase`, and calls the C function :code:`my_cos` to compute the cosinus for each element of this vector.
The output array is then plotted using the :code:`matplotlib` module.

.. code ::

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

Finally, we can run our python script using the following command :

.. code ::

    $ python show_sine.py

.. image:: img/c_numpy.png
  :width: 100%
  :alt: Output of the show_sine.py script