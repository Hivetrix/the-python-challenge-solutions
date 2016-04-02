# Level 0
## Problem

![](http://www.pythonchallenge.com/pc/def/calc.jpg)

Hint: try to change the URL address.

## Solution for the Impatient

```python
>>> 2 ** 38
274877906944
```

Next Level: http://www.pythonchallenge.com/pc/def/274877906944.html

And it will jump to http://www.pythonchallenge.com/pc/def/map.html

## Explanation
As the "0" indicates, this is just a warm up. Simply calculate 2^38, and follow the hint: embed the result in the URL.


### Things to Learn

First things first:

- Start the Python REPL
- Exit the Python REPL
- Calculate Power
- Run a Python script


### Start the REPL

We are using Python 3.x

```
$ python3
Python 3.5.0 (default, Sep 23 2015, 04:42:00) 
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.72)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### Calculate Power From REPLE

Use ``**`` for power:

```python
>>> 2**38
274877906944
```

In REPL the result will be printed; or you can explicitly print the result by calling ``print()``

```python
>>> print(2**38)
274877906944
```

Instead of ``**``, you can also use ``pow()``

```python
>>> pow(2,38)
274877906944
```
or

```python
>>> print(pow(2,38))
274877906944
```

### Stop the REPL

``Ctrl-C`` + ``Ctrl-D``

### Execute Python Script

Create a new file with ``.py`` extension:

```
$ vim level0.py
```

Add the content:

```
print(2**38)
```

Execute

```
$ python3 level0.py
```