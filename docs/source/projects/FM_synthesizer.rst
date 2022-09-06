STM32 FM Synthesizer 
====================

The goal of this project is to implement a FM (Frequency Modulation) sound synthesizer using the STM32F4 Discovery and/or the STM32L476G Discovery

Context 
-------

The foundation of the FM synthesis has been patented by John Chowning at Stanford University in 1974 (see `Patent <https://patents.google.com/patent/US4018121A/en>`_ )
One of the most famous synthesizer using this technique is the Yamaha DX7, that was manufactured by the Yamaha Corporation from 1983 to 1989. The DX7 is one of the best-selling synthesizers in history, selling more than 200,000 units.

.. image:: img/DX7.jpg
    :alt: The DX7 Synthesizer

Specifications
++++++++++++++

* Six phase-modulated oscillators : 

.. math :: 

    x_p(t) = a_p \sin(2\pi f_p t + \varphi_p + I_p x_q(t) ) 

In musical application, this signal model has the advantage of generating complex sounds. While the 
addition of two sine waves only contains 4 frequency components (positive and negative frequencies), a FM modulated sine wave can generate 
many frequency components whose amplitudes are determined by Bessel functions.

* Oscillators can be combined in different ways (32 algorithms). Each algorithm specify is an oscillator acts like a carrier or modulated signal.


.. image:: img/DX7_algorithms.jpg
    :alt: The DX7 Algorithms


* Seven 6-points envelopes (one for each sine and one for the pitch)


.. plot :: 
    :include-source: false

    import numpy as np 
    import matplotlib.pyplot as plt

    t = [0, 0.1, 0.2, 0.3, 0.8, 1]
    y = [0, 1, 0.6, 0.5, 0.5, 0]
    y_ticks_labels = ['0', 'L4','L1','L2','L3','L4']
    x_ticks_labels = ['0', 'T1','T2','T3', 'T4','T5']

    plt.plot(t,y)
    plt.yticks(y, y_ticks_labels)
    plt.xticks(t, x_ticks_labels)
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.grid()
    plt.xlabel('Time')
    plt.ylabel('Level')
    plt.annotate("",
            xy=(0.0, 0.2), xycoords='data',
            xytext=(0.8, 0.2), textcoords='data',
            arrowprops=dict(arrowstyle="<->"),
            )
    plt.annotate("",
            xy=(0.8, 0.2), xycoords='data',
            xytext=(1.0, 0.2), textcoords='data',
            arrowprops=dict(arrowstyle="<->"),
            )
    plt.text(0.35, 0.3, "Note On", fontsize=12)
    plt.text(0.85, 0.3, "Note Off", fontsize=12)


Methodology
-----------

* Communication between a MIDI keyboard and one of the USB port of the STM32F4
    * Extraction of the note ON / note OFF messages
    * Extraction of the Control Change messages.

* Implementation of the sound synthesizer
    * Generation of a sine wave oscillator, implementation of phase modulation,

    * Generation of the signal enveloppe (see `Video <https://youtu.be/Awju9PI8Spc?t=368>`_ ),
    * Implementation of the 32 DX7 algorithms.

* Implementation of some presets
    * Reverse engineering of some classical DX7 presets (pad sounds, bass sounds, rhodes sounds).
    * Integration of preset selection features (communications ? Midi message ?)
    * (Create a simple app to easily edit the DX7 parameters.)

References
----------

- A sound synthesizer STM32 project: https://github.com/MrBlueXav/Dekrispator_v2
- DX7 Manual: http://dxsysex.com/doc/DX7SE.pdf
- Origin of the DX7 and FM Synthesis: https://youtu.be/sXt_NXjc7oY
- List of classical super Kitch DX7 presets: https://www.youtube.com/watch?v=BCwn26FePAo
- Top Gun Music using the DX7: https://fr.audiofanzine.com/synthetiseur-rack/editorial/dossiers/on-refait-le-son-de-top-gun.html