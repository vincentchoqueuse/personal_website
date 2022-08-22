Latex 
=====

Preamble
--------

French Document 
+++++++++++++++

.. code ::

    \documentclass[french]{article}

    \usepackage{lmodern}
    \usepackage[T1]{fontenc}
    \usepackage{babel}

Text
----

Heading
+++++++

.. list-table::
   :widths: 25 75
   :header-rows: 0

   * - Chapter
     - :code:`\chapter{}`
   * - Section
     - :code:`\section{}`
   * - Subsection
     - :code:`\subsection{}`
   * - SubSubSection
     - :code:`\subsubsection{}`

Mathematical symbols
++++++++++++++++++++

.. list-table::
   :widths: 25 75
   :header-rows: 0

   * - :math:`\leq`
     - :code:`$\leq$`
   * - :math:`\geq`
     - :code:`$\geq$`
   * - :math:`\neq`
     - :code:`$\neq$`
   * - :math:`\approx`
     - :code:`$\approx$`
   * - :math:`\times`
     - :code:`$\times$`
   * - :math:`\div`
     - :code:`$\div$`
   * - :math:`\pm`
     - :code:`$\pm$`
   * - :math:`\cdot`
     - :code:`$\cdot$`
   * - :math:`^{\circ}`
     - :code:`$^{\circ}$`
   * - :math:`\circ`
     - :code:`$\circ$`
   * - :math:`\prime`
     - :code:`$\prime$`
   * - :math:`\cdots`
     - :code:`$\cdots$`
   * - :math:`\infty`
     - :code:`$\infty$`
   * - :math:`\neg`
     - :code:`$\neg$`
   * - :math:`\wedge`
     - :code:`$\wedge$`
   * - :math:`\vee`
     - :code:`$\vee$`
   * - :math:`\supset`
     - :code:`$\supset$`
   * - :math:`\forall`
     - :code:`$\forall$`
   * - :math:`\in`
     - :code:`$\in$`
   * - :math:`\rightarrow`
     - :code:`$\rightarrow$`
   * - :math:`\subset`
     - :code:`$\subset$`
   * - :math:`\exists`
     - :code:`$\exists$`
   * - :math:`\notin`
     - :code:`$\notin$`
   * - :math:`\Rightarrow`
     - :code:`$\Rightarrow$`
   * - :math:`\cap`
     - :code:`$\cap$`
   * - :math:`\cup`
     - :code:`$\cup$`
   * - :math:`\mid`
     - :code:`$\mid$`
   * - :math:`\Leftrightarrow`
     - :code:`$\Leftrightarrow$`
   * - :math:`\dot a`
     - :code:`$\dot a$`
   * - :math:`\hat a`
     - :code:`$\hat a$`
   * - :math:`\bar a`
     - :code:`$\bar a$`
   * - :math:`\tilde a`
     - :code:`$\tilde a$`
   * - :math:`\alpha`
     - :code:`$\alpha$`
   * - :math:`\beta`
     - :code:`$\beta$`
   * - :math:`\gamma`
     - :code:`$\gamma$`
   * - :math:`\delta`
     - :code:`$\delta$`
   * - :math:`\epsilon`
     - :code:`$\epsilon$`
   * - :math:`\zeta`
     - :code:`$\zeta$`
   * - :math:`\eta`
     - :code:`$\eta$`
   * - :math:`\varepsilon`
     - :code:`$\varepsilon$`
   * - :math:`\theta`
     - :code:`$\theta$`
   * - :math:`\iota$`
     - :code:`$\iota$$`
   * - :math:`\kappa`
     - :code:`$\kappa$`
   * - :math:`\vartheta`
     - :code:`$\vartheta$`
   * - :math:`\lambda`
     - :code:`$\lambda$`
   * - :math:`\mu`
     - :code:`$\mu`
   * - :math:`\nu`
     - :code:`$\nu$`
   * - :math:`\xi`
     - :code:`$\xi$`
   * - :math:`\pi`
     - :code:`$\pi$`
   * - :math:`\rho`
     - :code:`$\rho`
   * - :math:`\sigma`
     - :code:`$\sigma$`
   * - :math:`\tau`
     - :code:`$\tau$`
   * - :math:`\upsilon`
     - :code:`$\upsilon$`
   * - :math:`\phi`
     - :code:`$\phi$`
   * - :math:`\chi`
     - :code:`$\chi`
   * - :math:`\psi`
     - :code:`$\psi$`
   * - :math:`\omega`
     - :code:`$\omega$`
   * - :math:`\Gamma`
     - :code:`$\Gamma$`
   * - :math:`\Delta`
     - :code:`$\Delta$`
   * - :math:`\Theta`
     - :code:`$\Theta`
   * - :math:`\Lambda`
     - :code:`$\Lambda$`
   * - :math:`\Xi`
     - :code:`$\Xi$`
   * - :math:`\Pi`
     - :code:`$\Pi$`
   * - :math:`\Sigma`
     - :code:`$\Sigma`
   * - :math:`\Upsilon`
     - :code:`$\Upsilon$`
   * - :math:`\Phi`
     - :code:`$\Phi$`
   * - :math:`\Psi`
     - :code:`$\Psi`
   * - :math:`\Omega`
     - :code:`$\Omega$`

Table 
-----

Basic Usage 
+++++++++++

.. code ::
    
    \begin{table}[ht]
      \centering
      \begin{tabular}{cc}
          \hline
          & \\
          \hline
      \end{tabular}
      \caption{}
      \label{}
    \end{table}



Multi Column
++++++++++++

.. code ::
    
    \begin{table}[ht]
      \centering
      \begin{tabular}{cc}
          \hline
          \multicolumn{2}{c}{}\\
          & \\
          \hline
      \end{tabular}
      \caption{}
      \label{}
    \end{table}


Figures
-------

Basic Usage 
+++++++++++

.. code ::

    \begin{figure}
      \centering
      \includegraphics[width=1.\linewidth]{}
      \caption{}
      \label{}
    \end{figure}

Side by Side 
++++++++++++

.. code ::

    \usepackage{caption}
    \usepackage{subcaption}

    ...

    \begin{figure}
      \centering
      \begin{subfigure}{.5\textwidth}
        \centering
        \includegraphics[width=.45\linewidth]{}
        \caption{}
        \label{}
      \end{subfigure}%
      \begin{subfigure}{.5\textwidth}
        \centering
        \includegraphics[width=.45\linewidth]{}
        \caption{}
        \label{}
      \end{subfigure}
      \caption{}
      \label{}
    \end{figure}
