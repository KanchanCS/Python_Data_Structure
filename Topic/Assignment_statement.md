# Assignment statement

* Assing a value to a name

```python

i = 5
j = 2*i
j = j +5

```

* Left hand side is a name

* Right hand side is an expression
    * Operations in expression depend on type of value

# Numeric values

* Number come in two flavours
    * int - integers
    * float - fractional numbers
* 178, -3, 4283829 are values of type int 
* 37.82, -0.01, 28.7998 are values of type float

# int vs float

* Why are these different types ?

* Internally, a value is stored as a finite sequence of 0's and 1's (binary digits, or bits)

* For an int, the sequence is read off as a binary number

* For a float, this sequence breaks up into a mantissa and exponent

    * Like " scientific" notation 0.602 X 10^24

# Operations on numbers 

* Normal arithmetic operations :  __+, -, *, /__

    * Note that **/** always produces a float
    * 7/3.5 is 2.0, 7/2 is 3.5
* Quotient and remainder: **//** and **%** 
    
    * 9 // 5 is 1, 9%5 is 4

* Exponentiation : __*__

    * 3**4 is 81
# Other Operations on Numbers 

* log(), sqrt(), sin(), ....

* Built in to Python, but not available by default

* Must include __math__ "Library"

    ```python
       from math import *
    ```
