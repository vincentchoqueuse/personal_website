Course Website with Sphinx 
==========================

Sphinx is a powerful documentation generator based on the reStructuredText markup language. It can be used to generate website in html or documentation in pdf from :code:`rst` files.
This tool is perfect to publish course content on the internet since it works well with latex, code, matplotlib figure, ...

* Example: https://github.com/vincentchoqueuse/cheatsheet_elec

Getting Started
---------------

Installation 
++++++++++++

First, sphinx need to be installed on your system. Furthermore, I recommend to also install the `pydata sphinx theme <https://pydata-sphinx-theme.readthedocs.io/en/stable/>`_ . This theme is super clean and 
it is used by many data science python librairies such as numpy, scipy and matplotlib. 

.. code ::

    $ conda install sphinx
    $ pip install pydata-sphinx-theme

Creating a Documentation
++++++++++++++++++++++++

* To create a documentation, run the following command :

.. code ::

    $ sphinx-quickstart docs

Project Structure 
+++++++++++++++++

The :code:`sphinx-quickstart` command creates a new folder docs and populates the folder with specific files.

* Add the following files to your project

.. code ::

    Makefile
    build/
    make.bat
    requirements.txt    # add this
    source/
        _ext/
        _static/
            custom.css  # add this
        conf.py
        courses/        # add this
            index.rst   # add this
            course1.rst # add this
        index.rst       


File :code:`requirements.txt`
`````````````````````````````

The `requirements.txt` file is important if you want to deploy your documentation automatically on github or collaborate with others. It specifies the python
librairies used to build your doc. 

* Edit the `requirements.txt` file as below

.. code ::

    Jinja2 < 3.1
    pydata-sphinx-theme < 0.7.3
    numpy   # if needed
    scipy   # if needed
    matplotlib  # if needed


File :code:`index.rst`
``````````````````````
The `index.rst` files specify the structure of your documentation. 

* For the `index.rst` file located in the root folder, add the following content.

.. code ::

    .. cheatsheet documentation master file, created by
        sphinx-quickstart on XXX
        You can adapt this file completely to your liking, but it should at least
        contain the root `toctree` directive.

    Course
    ======


    .. toctree::
        :maxdepth: 1
        :caption: Contents:

        courses/index

* Edit the other `index.rst` file similarly.


File :code:`conf.py`
````````````````````

* Customize the `conf.py` file as specified below

.. code ::

    # conf.py 

    ...

    html_logo = "_static/logo.svg"

    ...

    html_theme = "pydata_sphinx_theme"

    ... 

    html_css_files = ['css/custom.css',]

    ... 

    html_theme_options = {
        "icon_links": [
                {
                    "name": "GitHub",
                    "url": "{{my_github_url}}",
                    "icon": "fab fa-github-square",
                }
                ]
        }

Build
+++++

* Tu build your documentation, run the following command :

.. code ::

    $ make html

Github Deployment
-----------------

In the following, I show how to use github workflow to automatically build and host your documentation.

Project Structure 
+++++++++++++++++

* Create a folder with the following structure

.. code ::

    .git        # add by git init
    .github/   
        workflows/
            sphinx.yml  # add this
    .gitignore  # add this
    LICENSE     # add this
    README.md   # add this
    docs/       # add your sphinx project here


File :code:`.gitignore`
```````````````````````

* Add a `.gitignore` file in the root folder of your project with the following content

.. code ::

    # sphinx build folder
    build
    docs/build

    # tests
    tests

    # Compiled source #
    ###################
    *.com
    *.class
    *.dll
    *.exe
    *.o
    *.so
    *.c

    # Packages #
    ############
    # it's better to unpack these files and commit the raw source
    # git has its own built in compression methods
    *.7z
    *.dmg
    *.gz
    *.iso
    *.jar
    *.rar
    *.tar
    *.zip

    # Logs and databases #
    ######################
    *.log
    *.sql
    *.sqlite

    # OS generated files #
    ######################
    .DS_Store?
    ehthumbs.db
    Icon?
    Thumbs.db


File :code:`sphinx.yml` 
```````````````````````

* In your `sphinx.yml` file, add the following content. This content allows github to run a new build each time a new push is detected.

.. code ::

    name: Sphinx build

    on: push

    jobs:
        build:
            runs-on: ubuntu-latest
            steps:
            - uses: actions/checkout@v2
            - name: Build HTML
            uses: ammaraskar/sphinx-action@0.4
            - name: Upload artifacts
            uses: actions/upload-artifact@v1
            with:
                name: html-docs
                path: docs/build/html/
            - name: Deploy
            uses: peaceiris/actions-gh-pages@v3
            if: github.ref == 'refs/heads/main'
            with:
                github_token: ${{ secrets.GITHUB_TOKEN }}
                publish_dir: docs/build/html