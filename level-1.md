# Level 1

## Problem

![](http://www.pythonchallenge.com/pc/def/map.jpg)

```
everybody thinks twice before solving this.

g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
```

## Solutions

As the url indicates, this is a map problem. Notice that there's exactly one character between the given pairs: ``K->L->M``, ``O->P->Q``, ``E->F->G``

### Solution 1

```python
raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr     gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpy    lq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

result = ''.join([chr(((ord(s) + 2) - ord('a')) % 26 + ord('a')) if s >= 'a' and s <= 'z' else s for s in raw])

print(result)
```

Result:

```
i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
```

Apply the same transformation to ``map``, the result is ``ocr``

Features used:

- List comprehension
- Type conversion

### Solution 2

```python
raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr     gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpy    lq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

table = str.maketrans(
    "abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"
)

result = raw.translate(table)

print(result)
```

Features used:

- ``string`` package and ``string.maketrans()``

## Next Level

http://www.pythonchallenge.com/pc/def/ocr.html


## Python 2 to Python 3

In Python 2, ``maketrans()`` is a method in ``string`` module, so you need to import it first:

```python
import string

table = string.maketrans("from", "to")
```

In Python 3, ``maketrans()`` is part of either ``bytes`` or ``str``:

- str.maketrans(from, to)
- bytes.maketrans(from, to)