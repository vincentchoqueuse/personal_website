Utilisation de Conda 
====================

Conda est un utilitaire très pratique pour installer et gérer des environnements Python. Cet utilitaire se révèle indispensable
si vous souhaitez utiliser Python dans différents projets avec des environnements utilisant des librairies différentes.

Installation
------------

* Téléchargez le fichier pkg adapté à votre processeur: https://docs.conda.io/en/latest/miniconda.html
* Installez :code:`miniconda`

MacOS et Linux 
++++++++++++++

Sur macOS ou Linux, le programme d'installation vous demandera si vous souhaitez ajouter `conda` au `PATH`. 
En ajoutant `conda` au `PATH`, l'interpréteur `python` utilisé par votre terminal deviendra le `python` installé avec `conda` (recommandé).
Pour vérifier que le `python` de votre terminal est bien celui de `conda`, il suffit de lancer dans votre terminal la commande `$ which python
` ou la commande `$ python`

.. note ::

    Il est possible d'ajouter `conda` au `PATH` à posteriori en lançant dans votre terminal, la commande :code:`$ conda init`

Windows 
+++++++

Sur Windows, `conda` installera un nouveau terminal appelé `Anaconda Prompt`. 


Utilisation 
-----------

L'utilitaire `conda` permet de gérer différents environnements isolés. Il est possible de connaître la liste des environnements 
en lançant la commande :code:`$ conda env list`. A titre d'illustration, cette commande me renvoie plusieurs environnements:

.. code ::

    base                  *  /opt/anaconda3
    py2                      /opt/anaconda3/envs/py2

L'environnement indiqué avec un :code:`*` correspond à l'environnement actif. Sur mon ordinateur, je possède également en environnement 
nommé :code:`py2` permettant de lancer des codes en `python 2.7`.

Changement d'environnement
++++++++++++++++++++++++++

Pour changer d'environnement, il faut utiliser la commande :code:`$ conda activate {nom_environnement}`

Par exemple, en lançant les commandes

.. code ::
    
    $ conda activate py2
    $ conda env list
    
j'obtiens le listing suivant :

.. code ::

    base                     /opt/anaconda3
    py2                   *  /opt/anaconda3/envs/py2

Création d'un environnement 
+++++++++++++++++++++++++++

Pour créer en environnement, il faut lancer la commande :code:`$ conda create --name {nom_environnement} python={version_python}`. 

Par exemple, il est possible de créer en environnement :code:`py_enib` utilisant python `3.9` en lançant la commande :

.. code ::
    
    $ conda create --name py_enib python=3.9

Pour activer l'environnement nouvellement créé, il faut ensuite lancer la commande :

.. code ::
    
    $ conda activate py_enib

Installation des paquets
++++++++++++++++++++++++

Pour connaître la liste des paquets installés dans l'environnement python actif, il faut lancer la commande :

.. code ::
    
    $ pip list 

A titre d'exemple, la liste des paquets installés dans l'environnement :code:`py_enib` est donné ci-dessous :

.. code ::

    Package    Version
    ---------- ---------
    certifi    2022.9.14
    pip        22.2.2
    setuptools 63.4.1
    wheel      0.37.1

Il est possible d'installer de nouveaux paquets en utilisant la commande :code:`$ conda install {mon_package}` (recommandé) ou via :code:`pip`. 
A titre d'exemple, la commande suivante montre comment installer les paquets numpy, scipy, matplotlib, seaborn et jupyter.

.. code ::

    conda install numpy scipy matplotlib seaborn jupyter


Retour à l'environnement de base
++++++++++++++++++++++++++++++++

Pour retourner à l'environnement de base, il faut lancer la commande :

.. code ::

    conda deactivate




