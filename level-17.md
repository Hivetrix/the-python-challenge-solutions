# Level 17

## Problem
http://www.pythonchallenge.com/pc/return/romance.html
## Solution

```python
from urllib.request import urlopen
import re, bz2

num = '12345'
info = ''
while(True):
    h = urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='+num)
    raw = h.read().decode("utf-8")
    print(raw)
    cookie = h.getheader("Set-Cookie")
    info += re.findall(r'info=(.*?);',cookie)[0]
    num = re.findall(r'\d+', raw)
    if len(num)<1: break
    num = num[-1]
print(info)
```

Output:

```
...
and the next busynothing is 96070
and the next busynothing is 83051
that's it.
BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90
```

