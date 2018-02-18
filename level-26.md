# Python Challenge - Level 26


- Link: www.pythonchallenge.com/pc/hex/decent.html
- Username: **butter**
- Password: **fly**

## Problem

![](src/level_26/decent.jpg)

> Hurry up, I'm missing the boat

## Solution

Send the email to ``leopold.moz@pythonchallenge.com`` and get the response:


> From: leopold.moz@pythonchallenge.com
> Subject: Re: sorry
> Date: 
> 
> Never mind that.
> 
> Have you found my broken zip?
> 
> md5: bbb8b499a0eef99b52c7f13f4e78c24b
> 
> Can you believe what one mistake can lead to?

As indicated there's only "one mistake". Try to modify the data and check by md5 code. 


```python
import hashlib

def search_and_save():
    for i in range(len(data)):
        for j in range(256):
            newData = data[:i] + bytes([j]) + data[i + 1:]
            if hashlib.md5(newData).hexdigest() == md5code:
                open('repaired.zip', 'wb').write(newData)
                return

md5code = 'bbb8b499a0eef99b52c7f13f4e78c24b'
data = open('maze/mybroken.zip', 'rb').read()
search_and_save()
```

The result is a picture with word "speed", plus the text:

> Hurry up, I'm missing the boat

The final answer is **speedboat**


## Next Level

http://www.pythonchallenge.com/pc/hex/speedboat.html


## Python 2 to 3

- ``md5`` module is deprecated, use ``hashlib.md5()``
- ``open()`` without explicitly specifying ``rb`` will use the default ``utf-8`` codec for decoding.


<div class="ad">
<script src='//z-na.amazon-adsystem.com/widgets/onejs?MarketPlace=US&amp;adInstanceId=0f3c2d71-0c18-4aca-be44-ba6e8892af33&amp;storeId=xstore0b-20'></script> 
</div>  