# Python Challenge - Level 1

- Link: http://www.pythonchallenge.com/pc/def/map.html

Problem
-------

![](src/level_01/map.jpg)

The image lists 3 pairs:

- K->M
- O->Q
- E->G

> everybody thinks twice before solving this.

> g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.

Hints
-----

The text must be encoded.

Hint from url: map. And notice that there's exactly one character between the given pairs: ``K->L->M``, ``O->P->Q``, 
``E->F->G``, and look at the very first letter in the text ``g``, if this is English, a good guess is that ``g`` is 
actually ``i``. What is the distance from ``g`` to ``i``? Yes, ``G->H->I``. So let's shift each character to the 
right, by 2, and ``y`` back to ``a``, ``z`` back to ``b``.

The string is not so long, so let's just copy and past it to REPL:

```python
>>> raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle grgl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
```

Solution 1
----------

The pair of functions that would help up make the change:

- ``ord()``: character to integer
- ``chr()``: integer to character

e.g.

```python
>>> chr(65)
'A'
>>> ord('A')
65
```

To shift a character:

```python
>>> ord('k') 
107
>>> ord('k') + 2
109
>>> chr(ord('k') + 2)
'm'
```

but it is not working for 'z':

```python
>>> chr(ord('z') + 2)
'|'
```

To make it circular, calculate it's distance from 'a'

```python
>>> (ord('z') + 2) - ord('a')
27
```

if it is larger than 26, go back to the beginning

```python
>>> ((ord('z') + 2) - ord('a')) % 26
1
```

then add that difference to ``'a'``

```python
>>> chr(((ord('z') + 2) - ord('a')) % 26 + ord('a'))
'b'
```

Let's translate the whole string:

```python
>>> result = ""
>>> for c in raw:
...     if c >= 'a' and c <= 'z':
...         result += chr(((ord(c) + 2) - ord('a')) % 26 + ord('a')) 
...     else:
...         result += c
... 
>>> result
"i hope you didnt translate it by hand. thats what computers are for. doing itin by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url."
```

That is how we make a loop in Java or C, but python has a better way: list comprehension

```python
>>> ''.join([chr(((ord(s) + 2) - ord('a')) % 26 + ord('a')) if s >= 'a' and s <= 'z' else s for s in raw])
"i hope you didnt translate it by hand. thats what computers are for. doing itin by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url."
```

But since it suggest us use ``.maketrans()``, let's try it next.

### Put Everything Together

```python
raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle grgl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print(''.join([chr(((ord(s) + 2) - ord('a')) % 26 + ord('a')) if s >= 'a' and s <= 'z' else s for s in raw]))
```



Solution 2: .maketrans()
------------------------

In Python 3, ``.maketrans`` is not in ``string`` as indicated; instead call ``str.maketrans()`` or ``bytes.maketrans()``

```python
>>> table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
>>> raw.translate(table)
"i hope you didnt translate it by hand. thats what computers are for. doing itin by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url."
```

### Put Everything Together

```python
raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle grgl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

table = str.maketrans(
    "abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"
)

result = raw.translate(table)

print(result)
```

Solution 3
----------

Let's have our own version of maketrans. The inputs are two lists, then each character is mapped from one list to 
another.


Define the two lists

```python
>>> a = "abcdefghijklmnopqrstuvwxyz,. '()"
>>> b = "cdefghijklmnopqrstuvwxyzab,. '()"
```

zip them

```python
>>> list(zip(a, b))
[('a', 'c'), ('b', 'd'), ('c', 'e'), ('d', 'f'), ('e', 'g'), ('f', 'h'), ('g', 'i'), ('h', 'j'), ('i', 'k'), ('j', 'l'), ('k', 'm'), ('l', 'n'), ('m', 'o'), ('n', 'p'), ('o', 'q'), ('p', 'r'), ('q', 's'), ('r', 't'), ('s', 'u'), ('t', 'v'), ('u', 'w'), ('v', 'x'), ('w', 'y'), ('x', 'z'), ('y', 'a'), ('z', 'b'), (',', ','), ('.', '.'), (' ', ' '), ("'", "'"), ('(', '('), (')', ')')]
```

actually we can create a dict

```python
>>> dict(zip(a, b))
{'t': 'v', 'g': 'i', 'b': 'd', 'i': 'k', ',': ',', 'v': 'x', 'u': 'w', 'd': 'f', 'e': 'g', 'h': 'j', 'm': 'o', "'": "'", '(': '(', '.': '.', 'q': 's', 'l': 'n', 'a': 'c', 'x': 'z', ' ': ' ', 'f': 'h', 'o': 'q', 'w': 'y', 'n': 'p', 'c': 'e', 'p': 'r', 's': 'u', 'z': 'b', 'j': 'l', 'y': 'a', 'r': 't', 'k': 'm', ')': ')'}
```

then mapping is as easy as 

```python
>>> dict(zip(a, b))['z']
'b'
```

translate the whole string:

```
>>> "".join([dict(zip(a,b))[x] for x in raw])
"i hope you didnt translate it by hand. thats what computers are for. doing itin by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url."
```

### Put Everything Together

```python
raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle grgl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

a = "abcdefghijklmnopqrstuvwxyz,. '()"
b = "cdefghijklmnopqrstuvwxyzab,. '()"

print("".join([dict(zip(a,b))[x] for x in raw]))
```

## Next Level

As hinted, apply the same function on the url(``map``), we get ``ocr``.

```python
>>> "map".translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"))
'ocr'
```

http://www.pythonchallenge.com/pc/def/ocr.html


## Python 2 to Python 3

In Python 2, ``maketrans()`` is a method in ``string`` module, so you need to import it first:

```python
import string

table = string.maketrans("from", "to")
```

In Python 3, ``maketrans()`` is part of either ``bytes`` or ``str``:

- ``str.maketrans(from, to)``
- ``bytes.maketrans(from, to)``


<div class="ad">
<script src='//z-na.amazon-adsystem.com/widgets/onejs?MarketPlace=US&amp;adInstanceId=0f3c2d71-0c18-4aca-be44-ba6e8892af33&amp;storeId=xstore0b-20'></script> 
</div>  