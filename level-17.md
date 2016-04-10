# Level 17

## Problem
http://www.pythonchallenge.com/pc/return/romance.html
## Solution

```python
from urllib.request import urlopen
from urllib.parse import unquote_plus, unquote_to_bytes
import re, bz2

num = '12345'
info = ''
while(True):
    h = urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='+num)
    raw = h.read().decode("utf-8")
    print(raw)
    cookie = h.getheader("Set-Cookie")
    info += re.search('info=(.*?);', cookie).group(1)
    match = re.search('the next busynothing is (\d+)', raw)
    if match == None: 
        break
    else:
        num = match.group(1)
res = unquote_to_bytes(info.replace("+", " "))
print(res)
print(bz2.decompress(res).decode())
```

Output:

```
...
and the next busynothing is 96070
and the next busynothing is 83051
that's it.
b'BZh91AY&SY\x94:\xe2I\x00\x00!\x19\x80P\x81\x11\x00\xafg\x9e\xa0 \x00hE=M\xb5#\xd0\xd4\xd1\xe2\x8d\x06\xa9\xfa&S\xd4\xd3!\xa1\xeai7h\x9b\x9a+\xbf`"\xc5WX\xe1\xadL\x80\xe8V<\xc6\xa8\xdbH&32\x18\xa8x\x01\x08!\x8dS\x0b\xc8\xaf\x96KO\xca2\xb0\xf1\xbd\x1du\xa0\x86\x05\x92s\xb0\x92\xc4Bc\xf1w$S\x85\t\tC\xae$\x90'
```

And the final line:
```
is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.
```

```python
from xmlrpc.client import ServerProxy

conn = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

print(conn.phone("Leopold"))
```

```
555-VIOLIN
```



