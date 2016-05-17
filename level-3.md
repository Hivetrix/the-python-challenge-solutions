# Level 3

## Problem

Link: http://www.pythonchallenge.com/pc/def/equality.html

![](http://www.pythonchallenge.com/pc/def/bodyguard.jpg)

> One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.

Again data can be found in html source.

## Solution

```python
import re

data = "".join(open('data.txt').read().splitlines())
print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data)))
```

Result: 

```
linkedlist
```

## Next Level

http://www.pythonchallenge.com/pc/def/linkedlist.html

The page will redirect you to ``linkedlist.php``

http://www.pythonchallenge.com/pc/def/linkedlist.php

## Further Readings

- [Python 3 - RegEx](http://www.hackingnote.com/en/python/re/)