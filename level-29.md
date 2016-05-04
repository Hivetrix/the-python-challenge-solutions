# Level 29



## Solution

Notice that there "silent" empty lines in the html source code. And the lines are of different lengths. Convert the lengths to bytes and decompress by bz2:

```python
from urllib.request import Request, urlopen
import bz2, base64

req = Request('http://www.pythonchallenge.com/pc/ring/guido.html')
req.add_header('Authorization', 'Basic %s' % base64.b64encode(b'repeat:switch').decode())
raw = urlopen(req).read().splitlines()[12:]
data = bytes([len(i) for i in raw])
print(bz2.decompress(data))
```

```
b"Isn't it clear? I am yankeedoodle!"
```

## Next Level

http://www.pythonchallenge.com/pc/ring/yankeedoodle.html