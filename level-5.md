# Level 5

## Problem

![](http://www.pythonchallenge.com/pc/def/peakhell.jpg)
pronounce it 

In HTML source:

```html
<peakhell src="banner.p"/>
<!-- peak hell sounds familiar ? -->
```

Sounds like... pickle

## Solution

```python
from urllib.request import urlopen
import pickle

h = urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(h)

for line in data:
    print("".join([k * v for k, v in line]))
```