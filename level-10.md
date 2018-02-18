# Python Challenge - Level 10

- Link: http://www.pythonchallenge.com/pc/return/bull.html
- Username: **huge**
- Password: **file**

## Problem

![](src/level_10/bull.jpg)

> len(a[30]) = ?

By clicking the image:

```
a = [1, 11, 21, 1211, 111221, 
```

A [look-and-say sequence](https://en.wikipedia.org/wiki/Look-and-say_sequence)

## Solution 1

This is a naive solution, just look, and say, assemble the string while we are counting.

```python
a = '1'
b = ''
for i in range(0, 30):
    j = 0
    k = 0
    while j < len(a):
        while k < len(a) and a[k] == a[j]: k += 1
        b += str(k-j) + a[j]
        j = k
    print b
    a = b
    b = ''
print len(a)
```

## Solution 2

Python can do much better. We can use regular expression to find the (number, length) pairs

```python
>>> import re
>>> re.findall(r"(\d)(\1*)", "111221")
[('1', '11'), ('2', '2'), ('1', '')]
```

Note that the pattern is a *raw string*(``r"..."``), which means backslash(``\``) does not need to be escaped. It is 
equivalent to 

```python
>>> re.findall("(\\d)(\\1*)", "111221")
```

The result tuples are in the form: (first appearance, following appearance), so from the first one we get the number,
 and the second one we get the length(remember to +1)
 
```python
>>> "".join([str(len(i+j))+i for i,j in re.findall(r"(\d)(\1*)", x)])
'11'
>>> "".join([str(len(i+j))+i for i,j in re.findall(r"(\d)(\1*)", "1")])
'11'
>>> "".join([str(len(i+j))+i for i,j in re.findall(r"(\d)(\1*)", "11")])
'21'
>>> "".join([str(len(i+j))+i for i,j in re.findall(r"(\d)(\1*)", "21")])
'1211'
>>> "".join([str(len(i+j))+i for i,j in re.findall(r"(\d)(\1*)", "1211")])
'111221'
```

Let it run 30 times:

```python
>>> x = "1"
>>> for n in range(30):
...     x="".join([str(len(j) + 1)+i for i, j in re.findall(r"(\d)(\1*)", x)])
... 
>>> len(x)
5808
```

## Solution 3

Similar to Solution 2, but we are using ``itertools.groupby()`` instead of regular expression to find the (number, 
length) pairs:

```python
>>> "".join([str(len(list(j))) + i for i,j in itertools.groupby("1211")])
'111221'
```

The result of ``groupby`` is (number, all appearances)

```python
>>> [(i, list(j)) for i,j in itertools.groupby("1211")]
[('1', ['1']), ('2', ['2']), ('1', ['1', '1'])]
```

that is why we do not need to ``+1`` when calculating the length as in Solution 2.

```python
>>> x = "1"
>>> for n in range(30):
...     x = "".join([str(len(list(j))) + i for i,j in itertools.groupby(x)])
... 
>>> len(x)
5808
```

## Solution 4

This is not recommend, but it is a cool one-liner solution. Do not sacrifice clarity for coolness in the real world 
projects!

```python
>>> from itertools import groupby
>>> from functools import reduce
>>> len(reduce(lambda x, n:reduce(lambda a, b: a + str(len(list(b[1]))) + b[0], groupby(x), ""), range(30), "1"))
5808
```

2 nested ``reduce()``, the outer one simply let it run for 30 times, and set the initial value ``1`` for ``x``; the 
inner one does exactly the same as in Solution 3.

Again, whether this bothers you or not, do not code anything that need you extensive explanations.

## Next Level

http://www.pythonchallenge.com/pc/return/5808.html
