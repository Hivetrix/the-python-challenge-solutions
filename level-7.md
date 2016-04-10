# Level 7

## Problem

![](http://www.pythonchallenge.com/pc/def/oxygen.png)

Nothing else... the gray scale should contain the information.

## Solution

Pick an image processing library. 

### Solution 1: PIL(Pillow)

Install Pillow
```
$ pip install pillow
```

```python
import re
from PIL import Image

i = Image.open("oxygen.png")
row = [i.getpixel((x, 45)) for x in range(0, i.size[0], 7)]
ords = [r for r, g, b, a in row if r == g == b]

print("".join(map(chr, map(int, re.findall("\d+", "".join(map(chr, ords)))))))
```

### Solution 2: PyPNG
``PyPNG``:

```bash
pip install pypng
```

```python
from urllib.request import urlopen
import png, re 

response = urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png")

(w, h, rgba, dummy) = png.Reader(response).read()

it = list(rgba)
mid = int(h / 2)
l = len(it[mid])
res = [chr(it[mid][i]) for i in range(0, l, 4*7) if it[mid][i] == it[mid][i + 1] == it[mid][i + 2]]
print("".join(res))
```

The pixels are stored as ``[r, g, b, a, r, g, b, a...]``, if the pixel is gray, rgb should be equivalent. Another tricky part is the width of each block is 7px(correspond to the number of level?) so the step of the range is ``4 * 7``.

Output

```
smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
```

Modify the last line:

```python
print("".join(map(chr, map(int, re.findall("\d+", "".join(res))))))
```

So integers are extracted and mapped to characters

Final result:

```
integrity
```