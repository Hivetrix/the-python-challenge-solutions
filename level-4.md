# Level 4

- Link: http://www.pythonchallenge.com/pc/def/linkedlist.php

## Problem


![](images/chainsaw.jpg)

Click on the image, you would see


> and the next nothing is 44827
  
And the url changed to ``http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345``

Change the url with the new number and another number will be given.

## Solution


```python
from urllib.request import urlopen
import re

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"

num = "12345"

# Later change to something else and rerun:
#     and the next nothing is 16044
#     Yes. Divide by two and keep going.
#num = str(16044/2)

while True:
    content = urlopen(uri % num).read().decode('utf-8')
    print(content)
    match = re.search("and the next nothing is (\d+)", content)
    if match == None:
        break
    else:
        num = match.group(1)
```

Result

``` 
peak.html
```

## Next Level

http://www.pythonchallenge.com/pc/def/peak.html
 
## Python 2 to Python 3

Python 2's ``urllib`` and ``urllib2`` are combined as 

