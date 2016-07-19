# Python Challenge - Level 7

- Link: http://www.pythonchallenge.com/pc/def/oxygen.html

## Problem

![](images/oxygen.png)

Nothing else... the gray scale should contain the information.

We need an image processing library. 

## Solution 1: PIL(Pillow)

<div class="bs-callout bs-callout-danger">
    <h4>Python 2 to 3</h4>
    <p>The original PIL was not ported to Python 3. Use the fork called ``Pillow`` instead</p>
</div>

Install Pillow

```
$ pip3 install pillow
```

Make sure you can load the module:

```python
>>> from PIL import Image
```

To load an image, one way is to download the image to local manually, then load it by:

```python
>>> img = Image.open("oxygen.png")
```

Or load it from url directly:

```python
>>> import requests
>>> from io import BytesIO
>>> from PIL import Image
>>> img = Image.open(BytesIO(requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png').content))
```

We can get some basic info about the image:

```python
>>> im.width
629
>>> im.height
95
```

And get the pixel by providing indices:

```python
>>> img.getpixel((0,0))
(79, 92, 23, 255)
```

The result is the tuple of (R, G, B, alpha).

To get the grey scale, we can take the middle row of the pixels:

```python
>>> row = [img.getpixel((x, img.height / 2)) for x in range(img.width)]
>>> row
[(115, 115, 115, 255), (115, 115, 115, 255), (115, 115, 115, 255), ...
```

As you can tell, row has lots of duplicates, since each grey block's width is larger than 1 pixel. If you do some 
manual counting, you know it is exactly 7 pixels wide, this should be the easiest way to de-dup:

```python
>>> row = row[::7]
>>> row
[(115, 115, 115, 255), (109, 109, 109, 255), (97, 97, 97, 255), ...
```



Notice that at the end of the array there are some noises: pixels that are not grey scale, which have the same value 
for R, G, and B. We can remove those pixels

```python
>>> ords = [r for r, g, b, a in row if r == g == b]
```

and since RGB is using a positive number in [0, 255] for each color, we can assume it represents a ASCII character:

```python
>>> "".join(map(chr, ords))
'smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]'
```

We were right, but it is not over... Do it again on the numbers:

```python
>>> nums = re.findall("\d+", "".join(map(chr, ords)))
>>> nums
['105', '110', '116', '101', '103', '114', '105', '116', '121']
```

Finally:

```python
>>> "".join(map(chr, map(int, nums)))
'integrity'
```

## Solution 2: PyPNG

Alternatively use a package called ``PyPNG``:

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


> smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]


Modify the last line:

```python
print("".join(map(chr, map(int, re.findall("\d+", "".join(res))))))
```

So integers are extracted and mapped to characters

Final result:

> integrity


## Next Level

http://www.pythonchallenge.com/pc/def/integrity.html

## Read More

- [Pillow Documentation](http://pillow.readthedocs.io/)