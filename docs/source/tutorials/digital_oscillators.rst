Digital Oscillators
===================

In this tutorial, we shows how to generate a digital waveform using a lookup table.
Specifically, we focus on the generation of a sine waveform, but this tutorial can be easily extended to 
other waveforms such as triangle or sawtooth waveforms.

Sine Wave Waveform 
------------------

A sine wave can be mathematically described as 

.. math ::

    x(t) = \sin(2\pi f_0 t)

* :math:`f_0` corresponds to the fundamental frequency. 

In the digital domain, the sine wave can be obtained by evaluating 
:math:`x(t)` for :math:`t=n/fs` with :math:`n \in \mathbb{N}`. For the C language, the function :math:`x(n/fs)` can be evaluated 
naively using the :code:`sin` function of the library :code:`math.h`. Nevertheless, the evaluation of trigonometric functions increases the 
computational complexity of your program. In this tutorial, we describe an alternative low-complexity implementation based on a wavetable.

Wavetable 
---------

To reduce the computational complexity, we can store in memory a full cycle of a sine waveform.

.. math ::

    x[n] = \sin(2\pi n/N)

* :math:`N\in \mathbb{N}` corresponds to the length of the wavetable.

.. plot :: 
    :include-source: false

    import numpy as np 
    import matplotlib.pyplot as plt

    from scipy import signal

    N = 128
    n = np.arange(N)
    x = np.sin(2*np.pi*n/N)     
    plt.stem(n, x)
    plt.grid()
    plt.xlabel("$n$")
    plt.ylabel("$x[n]$")
    plt.xlim([0, N-1])

Controlling the Fundamental Frequency
-------------------------------------

Reading each sample of the wavetable with a sampling frequency :code:`f_s` allows to synthesize a sinewave with frequency 
:math:`f_{0}=N/f_s` Hz. To modify the fundamental frequency to :math:`f_0` Hz, one solution is to change the rate at which the samples are 
read in the wavetable. If :math:`y[n]` corresponds to the nth output sample and  :math:`y[n] = x[m]`, the (n+1)th output signal can be computed from the wavetable as follows :

.. math ::

    y[n+1] = x[m+\Delta]

* :math:`\Delta=N\frac{f_0}{f_s}` corresponds to the phase delta between two adjacent samples.

It is important to note that the index :math:`k=m+\Delta` is not always an integer. To address this issue, two solutions can be implemented.

0th order Interpolation 
+++++++++++++++++++++++

The index can be rounded to the  greatest integer less than or equal to :math:`k`. The output sample is then given by :

.. math ::

    y[n+1] = x[\lfloor k \rfloor]

Linear Interpolation
++++++++++++++++++++

The interpolated sample :math:`y[n+1]` can be obtained as :

.. math ::

    y[n+1] = x_l + \alpha (x_r-x_l)

* :math:`\alpha = k-\lfloor k \rfloor`,
* :math:`x_l=x[k]` and :math:`x_r = x[k+1]` corresponds to two adjacent samples.


C Implementation 
----------------

The following code shows a possible C implementation for the wavetable synthesizer. 


.. code :: c

    #include <math.h>

    int N = 128;
    double wavetable[128]={0.000000000000000000e+00, 4.906767432741801493e-02, 9.801714032956060363e-02, 1.467304744553617479e-01, 1.950903220161282481e-01, 2.429801799032638709e-01, 2.902846772544623311e-01, 3.368898533922200511e-01, 3.826834323650897818e-01, 4.275550934302820849e-01, 4.713967368259976420e-01, 5.141027441932216613e-01, 5.555702330196021776e-01, 5.956993044924333569e-01, 6.343932841636454878e-01, 6.715589548470183301e-01, 7.071067811865474617e-01, 7.409511253549589949e-01, 7.730104533627368824e-01, 8.032075314806448318e-01, 8.314696123025451246e-01, 8.577286100002721181e-01, 8.819212643483549385e-01, 9.039892931234433382e-01, 9.238795325112867385e-01, 9.415440651830208063e-01, 9.569403357322089354e-01, 9.700312531945439742e-01, 9.807852804032304306e-01, 9.891765099647810144e-01, 9.951847266721968177e-01, 9.987954562051724050e-01, 1.000000000000000000e+00, 9.987954562051724050e-01, 9.951847266721969287e-01, 9.891765099647810144e-01, 9.807852804032304306e-01, 9.700312531945439742e-01, 9.569403357322089354e-01, 9.415440651830208063e-01, 9.238795325112867385e-01, 9.039892931234434492e-01, 8.819212643483550496e-01, 8.577286100002721181e-01, 8.314696123025454577e-01, 8.032075314806449429e-01, 7.730104533627371044e-01, 7.409511253549589949e-01, 7.071067811865475727e-01, 6.715589548470185521e-01, 6.343932841636454878e-01, 5.956993044924334679e-01, 5.555702330196021776e-01, 5.141027441932217723e-01, 4.713967368259978086e-01, 4.275550934302820294e-01, 3.826834323650898373e-01, 3.368898533922202732e-01, 2.902846772544623311e-01, 2.429801799032640375e-01, 1.950903220161285812e-01, 1.467304744553618034e-01, 9.801714032956083955e-02, 4.906767432741797330e-02, 1.224646799147353207e-16, -4.906767432741772350e-02, -9.801714032956058975e-02, -1.467304744553615814e-01, -1.950903220161283591e-01, -2.429801799032638154e-01, -2.902846772544621645e-01, -3.368898533922201066e-01, -3.826834323650896708e-01, -4.275550934302818074e-01, -4.713967368259976420e-01, -5.141027441932215503e-01, -5.555702330196019556e-01, -5.956993044924332459e-01, -6.343932841636452657e-01, -6.715589548470184411e-01, -7.071067811865474617e-01, -7.409511253549587728e-01, -7.730104533627366603e-01, -8.032075314806450539e-01, -8.314696123025452357e-01, -8.577286100002720071e-01, -8.819212643483549385e-01, -9.039892931234431162e-01, -9.238795325112865164e-01, -9.415440651830208063e-01, -9.569403357322088244e-01, -9.700312531945439742e-01, -9.807852804032303196e-01, -9.891765099647809034e-01, -9.951847266721969287e-01, -9.987954562051724050e-01, -1.000000000000000000e+00, -9.987954562051724050e-01, -9.951847266721969287e-01, -9.891765099647809034e-01, -9.807852804032304306e-01, -9.700312531945439742e-01, -9.569403357322089354e-01, -9.415440651830209173e-01, -9.238795325112866275e-01, -9.039892931234433382e-01, -8.819212643483550496e-01, -8.577286100002722291e-01, -8.314696123025455687e-01, -8.032075314806452759e-01, -7.730104533627368824e-01, -7.409511253549592169e-01, -7.071067811865476838e-01, -6.715589548470186632e-01, -6.343932841636459319e-01, -5.956993044924332459e-01, -5.555702330196021776e-01, -5.141027441932218833e-01, -4.713967368259979196e-01, -4.275550934302825290e-01, -3.826834323650903924e-01, -3.368898533922199956e-01, -2.902846772544624421e-01, -2.429801799032641763e-01, -1.950903220161287199e-01, -1.467304744553623863e-01, -9.801714032956052036e-02, -4.906767432741809126e-02};

    void oscillator(double *buffer, double f0, int fs, double *currentIndex, int size)
    {
        double coef; 
        float index = *currentIndex;
        int index_l, index_r;
        int n;

        for(n=0; n<size; n++)
        {
            index_l = (int)index;
            index_r = (index_l == (N-1)) ? 0 : index_l+1;
            coef = index - index_l;
            buffer[n] = wavetable[index_l]+ coef*(wavetable[index_r]-wavetable[index_l]);
            //update increment
            index += N*(f0/(1.0*fs));
            index = fmod(index, 1.0*N);
        }

        //export index 
        *currentIndex = index;
    }

Verification 
------------

I recommend to check the validity of the C code by comparing the output of the C and Python implementation.

* First, compile the C code as a shared library 
.. code ::

    $ gcc -fPIC -shared my_lib.c -o my_lib.so 

* Then, run the following python code.

.. code ::

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

.. image:: img/sinewave.png
  :width: 100%
  :alt: Comparison of Python and C implementation



References
----------

* JUCE C++ implementation: https://docs.juce.com/master/tutorial_wavetable_synth.html