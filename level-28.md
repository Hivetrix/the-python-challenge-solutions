# Python Challenge - Level 28

- Link: http://www.pythonchallenge.com/pc/ring/bell.html
- Username: **repeat**
- Password: **switch**

## Problem

![](images/bell.png)

> RING-RING-RING 
  say it out loud

## Solution


http://www.pythonchallenge.com/pc/ring/green.html

> yes! green!



```python
from PIL import Image

im = Image.open('bell.png')

# split RGB and get Green
green = list(im.split()[1].getdata())

# calculate diff for every two bytes
diff = [abs(a - b) for a, b in zip(green[0::2], green[1::2])]

# remove the most frequent value 42
filtered = list(filter(lambda x: x != 42, diff))

# convert to string and print out
print(bytes(filtered).decode())
```

Result

```
whodunnit().split()[0] ?
```

The creator of Python is Guido van Rossum, so the final answer is "guido"

## Next Level

http://www.pythonchallenge.com/pc/ring/guido.html
