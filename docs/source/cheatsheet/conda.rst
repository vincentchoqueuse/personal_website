Conda
=====

* Source: https://education.github.com/git-cheat-sheet-education.pdf

Basics 
------

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - :code:`conda info`
     - verify conda installation, check version number
   * - :code:`conda update conda`
     - update conda to the current version
   * - :code:`conda install {{PACKAGENAME}}`
     - install a package included in Anaconda

Using environments
------------------

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - :code:`conda create --name py35 python=3.5`
     - create a new environment named py35, install Python 3.5
   * - :code:`conda activate py35`
     - activate the new environment to use it
   * - :code:`conda deactivate py35`
     - deactivate the current environment
   * - :code:`conda env list`
     - get a list of all my environments
   * - :code:`conda list`
     - list all packages and versions installed in active environment
   * - :code:`conda env remove --name py35`
     - Delete an environment and everything in it
