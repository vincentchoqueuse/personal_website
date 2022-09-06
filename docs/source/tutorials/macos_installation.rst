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

Si tout s'est bien passé, la commande doit renvoyer la documentation de `conda` dans le terminal.

Librairies Python
`````````````````

De base miniconda ne contient qu'un ensemble réduit de librairies Python (lancer la commande :code:`pip list` pour connaître les paquets installés).
Il est possible d'installer les librairies scientifiques facilement en utilisant la commande :

.. code ::

    $ conda install numpy scipy matplotlib jupyter seaborn

Pour vérifier que l'installation est correcte, il suffit de lister les paquets python installés sur votre système. 

.. code ::

    $ pip list

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


Verification
````````````

Une fois l'installation réalisée, il est possible de verifier que l'installation est bien fonctionnelle en lançant la commande suivante

.. code ::

    $ 