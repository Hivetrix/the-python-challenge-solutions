# Level 7

## Problem

![](http://www.pythonchallenge.com/pc/def/oxygen.png)

Nothing else... the gray scale should contain the information.

## Solution

Pick an image processing library. PIL does not work. Try ``PyPNG``:

```bash
pip install pypng
```

```python
from urllib.request import urlopen
import png 

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
smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121] integrity
```


