Tikz 
====

Electrical Circuits 
-------------------

RC filter 
+++++++++

.. code ::

    \usepackage{circuitikz}

    ...

    \begin{tikzpicture}
        \draw (0,0) 
        to[R, l=$R$,-] (3,0) 
        to[C, l=$C$, *-] (3,-2) 
        to[short](3,-2)   node [ground] {};
        %input
        \draw (-0.5,0)
        to[short, l_=$V_{in}$](-0.5,-2)   node [ground] {};
        \draw (-0.5,0) coordinate[inputarrow,rotate=90];
        % output
        \draw (4,0)
        to[short, l=$V_{out}$](4,-2)   node [ground] {};
        \draw (4,0) coordinate[inputarrow,rotate=90];
    \end{tikzpicture}

* List of circuits: https://github.com/vincentchoqueuse/analog_circuits_tikz

Plot
----

Bode Diagram
++++++++++++

.. code ::

    \usepackage{tikz}
    \usepackage{pgfplots}
    \usepackage{caption}
    \usepackage{subcaption}

    ...

    \begin{figure}
    \centering
        \begin{subfigure}{.5\textwidth}
            \centering
            \begin{tikzpicture}
                \begin{loglogaxis}[xlabel=$\omega$, ylabel={$|H(j\omega)|$},xmin=1, xmax=100000,ymin=0.01, grid=both]
                \addplot[domain=1:100000, red, thick]{0.333*(sqrt(4e-06*x*x +1))/sqrt(4.444e-07*x*x +1)};
                \end{loglogaxis}
            \end{tikzpicture}
            \caption{Module}
        \end{subfigure}%
        \begin{subfigure}{.5\textwidth}
            \centering
            \begin{tikzpicture}
                \begin{semilogxaxis}[xlabel=$\omega$, ylabel={$\arg[H(j\omega)]$},xmin=1, xmax=100000,ymin=0, ymax=60, grid=both]
                \addplot[domain=1:100000, red, thick]{atan(0.002*x)-atan(0.00066*x)};
                \end{semilogxaxis}
            \end{tikzpicture}
            \caption{Argument}
        \end{subfigure}
    \caption{Diagramme de Bode}
    \end{figure}
