Python 3
========

* Source: https://www.pythoncheatsheet.org/cheatsheet/basics

Basics 
------

Data Types
++++++++++

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Data Type	
     - Examples
   * - Integers
     - :code:`-2, -1, 0, 1, 2, 3, 4, 5`
   * - Floating-point numbers
     - :code:`-1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25`
   * - Strings 
     - :code:`'a', 'aa', 'aaa', 'Hello!', '11 cats'`
   * - Lists 
     - :code:`['John', 'Peter', 'Debora', 'Charles']`
   * - Tuples 
     - :code:`('table', 'chair', 'rack', 'shelf')`
   * - Dictionaries 
     - :code:`{'color': 'red', 'age': 42}`

Control Flow
------------

:code:`if` statements
+++++++++++++++++++++

.. code ::

    if name != 'George':
        print('You are not George')

.. code ::

    if name != 'George':
        print('You are not George')
    else:
        print('You are not George')

.. code :: 

    if name == 'Debora':
        print('Hi Debora!')
    elif name == 'George':
        print('Hi George!')
    else:
        print('Who are you?')

:code:`while` Loop statements
+++++++++++++++++++++++++++++

.. code ::

    spam = 0
    while spam < 5:
        print('Hello, world.')
        spam = spam + 1

:code:`for` loop
++++++++++++++++

.. code :: 

    pets = ['Bella', 'Milo', 'Loki']
    for pet in pets:
        print(pet)

.. code ::

    for i in range(5):
        print(f'Will stop at 5! or 4? ({i})')

Operators 
---------

Math Operators
++++++++++++++

.. list-table::
   :widths: 25 50 25
   :header-rows: 1

   * - Operators 
     - Operation
     - Example 
   * - :code:`**`
     - Exponent 
     - :code:`2 ** 3 = 8`
   * - :code:`%`
     - Modulus/Remainder 
     - :code:`22 % 8 = 6`
   * - :code:`//`
     - Integer division 
     - :code:`22 // 8 = 2`
   * - :code:`/`
     - Division 
     - :code:`22 / 8 = 2.75`
   * - :code:`*`
     - Multiplication 
     - :code:`3 * 3 = 9`
   * - :code:`-`
     - Subtraction
     - :code:`5 - 2 = 3`
   * - :code:`+`
     - Addition
     - :code:`2 + 2 = 4`

Comparison Operators
++++++++++++++++++++

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Operator
     - Meaning
   * - :code:`==`
     - Equal to
   * - :code:`!=`
     - Not equal to
   * - :code:`<`
     - Less than
   * - :code:`>`
     - Greater Than
   * - :code:`<=`
     - Less than or Equal to
   * - :code:`>=`
     - Greater than or Equal to




Boolean Operators 
+++++++++++++++++

Operator :code:`and`
````````````````````

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Expression
     - Result
   * - :code:`True and True`
     - :code:`True`
   * - :code:`True and False`
     - :code:`False`
   * - :code:`False and True`
     - :code:`False`
   * - :code:`False and False`
     - :code:`False`
    
Operator :code:`or`
```````````````````

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Expression
     - Result
   * - :code:`True or True`
     - :code:`True`
   * - :code:`True or False`
     - :code:`True`
   * - :code:`False or True`
     - :code:`True`
   * - :code:`False and False`
     - :code:`False`

Operator :code:`not`
`````````````````````
.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Expression
     - Result
   * - :code:`not True`
     - :code:`False`
   * - :code:`not False`
     - :code:`True`
