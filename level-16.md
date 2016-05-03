# Level 16

## Problem
http://www.pythonchallenge.com/pc/return/mozart.html


title: let me get this straight

## Solution

- Align the pink segments
- Pink is 195

```python
from PIL import Image, ImageChops

image = Image.open("mozart.gif")

for y in range(image.size[1]):
    box = 0, y, image.size[0], y + 1
    row = image.crop(box)
    bytes = row.tobytes()
    i = bytes.index(195)
    row = ImageChops.offset(row, -i)
    image.paste(row, box)

image.save("new.gif")
```

Open ``new.gif``, the image reads: romance

## Next Level

http://www.pythonchallenge.com/pc/return/romance.html