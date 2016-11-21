# Python Challenge - Level 30

- Link: http://www.pythonchallenge.com/pc/ring/yankeedoodle.html
- Username: **repeat**
- Password: **switch**

## Problem

![](images/yankeedoodle.jpg)

> The picture is only meant to help you relax

## Solution

$ wget --user repeat --password switch http://www.pythonchallenge.com/pc/ring/yankeedoodle.csv


```python
from PIL import Image
import math

with open('yankeedoodle.csv') as f:
    data = [x.strip() for x in f.read().split(",")]
    length = len(data)
    print(length)
    # 7367

    factors = [x for x in range(2, length) if length % x == 0]
    print(factors)
    # [53, 139]

    img = Image.new("F", (53, 139))
    img.putdata([float(x) for x in data], 256)

    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img = img.transpose(Image.ROTATE_90)
    #img.show()
    
    a = data[0::3]
    b = data[1::3]
    c = data[2::3]

    res = bytes([int(x[0][5] + x[1][5] + x[2][6]) for x in zip(data[0::3], data[1::3], data[2::3])])

    print(res)
    
```

```
b'So, you found the hidden message.\nThere is lots of room here for a long message, but we only need very little space to say "look at grandpa", so the rest is just garbage. \nVTZ.l\'\x7ftf*Om@I"p]...'
```

keyword: grandpa

## Next Level

http://www.pythonchallenge.com/pc/ring/grandpa.html

<div class="ad">
<script src='//z-na.amazon-adsystem.com/widgets/onejs?MarketPlace=US&amp;adInstanceId=0f3c2d71-0c18-4aca-be44-ba6e8892af33&amp;storeId=xstore0b-20'></script> 
</div>  