Installation MacOS 
==================

Installation Python
-------------------

Miniconda
+++++++++

Pour l'installation de Python, je recommande l'utilisation de Miniconda

* Téléchargez le fichier pkg adapté à votre processeur: https://docs.conda.io/en/latest/miniconda.html
* Installez miniconda.

Par défaut miniconda est installé dans le path. Pour vérifier que l'installation est correcte, vous pouvez procéder de la manière suivante :

* Lancez un terminal,
* Exécutez la commande 

.. code ::

    $ conda 

Si l'installation s'est bien passée, le lancement de la commande :code:`conda --version` doit vous afficher la version de conda installée dans le système.

Librairies Python
`````````````````

De base miniconda ne contient qu'un ensemble réduit de librairies Python (lancer la commande :code:`pip list` pour connaître les paquets installés).
Il est possible d'installer les librairies scientifiques facilement en utilisant la commande :

.. code ::

    $ conda install numpy scipy matplotlib seaborn jupyter

Si l'installation s'est bien passée, le lancement de la commande :code:`pip list` doit vous afficher la liste des paquets python installés.


Editeur de Code 
---------------

Pour éditer du code, je recommande l'utilisation de Vscode 

* Téléchargez Vscode et installez le: https://code.visualstudio.com/download 


Installation des outils de développement
----------------------------------------

Brew
++++

Brew est un gestionnaire de paquet pour macOS. Il permet d'installer rapidement des outils à partir du terminal 

Installation 
`````````````

.. code ::

    $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

L'installation vous demandera probablement d'installer les `command line tools` de xcode (valider la demande).

Programmation en C 
++++++++++++++++++

Pour coder en C, il faut un compilateur comme `gcc`. Pour voir si `gcc` est installé sur votre système, lancez simplement la commande 

.. code ::

    $ gcc


Si le compilateur n'est pas trouvé, macOS vous proposera d'installer les Command Line Tools de XCode (contenant gcc) automatiquement. Si l'installation n'est pas proposée automatiquement, 
vous pouvez les installer en lançant la commande 

.. code ::

    $ xcode-select --install

Programmation sur STM32 
+++++++++++++++++++++++

GCC ARM Embedded Toolchain 
``````````````````````````

Pour pouvoir compiler du code pour les STM32, il faut installer le GCC ARM Embedded Toolchain. 

.. code ::

    $ brew install homebrew/cask/gcc-arm-embedded

Si l'installation s'est bien passée, le lancement de la commande :code:`arm-none-eabi-gcc --version` doit afficher le message suivant :

.. code ::

    $ arm-none-eabi-gcc --version
    arm-none-eabi-gcc (GNU Tools for Arm Embedded Processors 7-2017-q4-major) 7.2.1 20170904 (release) [ARM/embedded-7-branch revision 255204]
    Copyright (C) 2017 Free Software Foundation, Inc.
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Open OCD 
````````

Pour pouvoir debugger les programmes, il faut installer un debugger comme OpenOCD.

.. code ::

    $ brew install openocd

Si l'installation s'est bien passée, le lancement de la commande :code:`openOCD --version` doit afficher le message suivant :

.. code ::

    $ openOCD --version
    Open On-Chip Debugger 0.10.0
    Licensed under GNU GPL v2
    For bug reports, read
        http://openocd.org/doc/doxygen/bugs.html

