# Python Challenge - Level 0

- Link: http://www.pythonchallenge.com/pc/def/0.html

## Problem



![](src/level_00/calc.jpg)

> Hint: try to change the URL address.

## Explore

As the "0" indicates, this is just a warm up. 

### Loop

The naive way to solve it: multiply by 2 in a loop:

```python
>>> k = 1
>>> for i in range(38):
...     k *= 2
... 
>>> k
274877906944
```

### Power

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

### Shift

Multiply by 2 is equivalent to shifting the binary representation left by one:

```python
>>> 1<<38
274877906944
```

### Numeric Types

Done!

Wait, why 38? what is implied?

If you are coming from C/C++, Java or other languages, you know that there are multiple types just for integers: ``short``, ``integer``, ``long``, and even ``BigInteger`` beyond 64-bit. However that is not the case in Python:

```python
>>> type(2**3)
<class 'int'>
>>> type(2**38)
<class 'int'>
>>> type(2**380)
<class 'int'>
```

So 38 is a good(and random) example to show a ``int`` larger than 32-bit.

Similar for float type, in Python it can be arbitrarily large, no ``double`` needed

```python
>>> type(2**3.8)
<class 'float'>
>>> type(2.0**38)
<class 'float'>
```

## Complete Solution

```python
print(2**38)
```

Output:

```
274877906944
```

## Next Level
 
http://www.pythonchallenge.com/pc/def/274877906944.html

And it will jump to 

http://www.pythonchallenge.com/pc/def/map.html

## Read More

- [Python 3 - REPL](http://www.hackingnote.com/en/python/repl/)
