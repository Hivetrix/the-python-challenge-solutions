# Python Challenge - Level 8

- Link: http://www.pythonchallenge.com/pc/def/integrity.html

## Problem

![](src/level_08/integrity.jpg)

> Where is the missing link?

The fly is clickable, but it asks for user name and password, and this line:

> The site says: "inflate"

And in the page source:

```html
<!--
un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
-->
```

The opposite of "inflate" is... "compress". Do not blame yourself if you do not know which compression format it is. 
Here are some clues that it is "bzip2"...

> .magic:16                       = 'BZ' signature/magic number
> .version:8                      = 'h' for Bzip2 ('H'uffman coding), '0' for Bzip1 (deprecated)
> .hundred_k_blocksize:8          = '1'..'9' block-size 100 kB-900 kB (uncompressed)

## Solution

Let's decompress it:

```python
>>> import bz2
>>> bz2.decompress('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.5/bz2.py", line 348, in decompress
    res = decomp.decompress(data)
TypeError: a bytes-like object is required, not 'str'
```

That does not work... ``.decompress()`` expects some ``bytes``, not string

```python
>>> bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
b'huge'
>>> bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')
b'file'
```

### Put Everything Together

```python
import bz2

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

print(bz2.decompress(un))
print(bz2.decompress(pw))
```

## Next Level

Click the fly(or the link in page source): ``../return/good.html``, and fill in username(``huge``) and password(``file``)

http://www.pythonchallenge.com/pc/return/good.html


<div class="ad">
<script src='//z-na.amazon-adsystem.com/widgets/onejs?MarketPlace=US&amp;adInstanceId=0f3c2d71-0c18-4aca-be44-ba6e8892af33&amp;storeId=xstore0b-20'></script> 
</div>  