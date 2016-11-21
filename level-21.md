# Python Challenge - Level 21

## Problem

Inside the zip file.

## Solution

```python
import zlib, bz2

with open("package.pack", "rb") as f:
    data = f.read()

    while True:
        if data.startswith(b'x\x9c'):
            data = zlib.decompress(data)
        elif data.startswith(b'BZh'):       
            data = bz2.decompress(data)
        elif data.endswith(b'\x9cx'):
            data = data[::-1]
        else:
            break
    print(data)
```

Result:

```
b'sgol ruoy ta kool'
```

Add logging:

```python
import zlib, bz2

result = ""

with open("package.pack", "rb") as f:
    data = f.read()

    while True:
        if data.startswith(b'x\x9c'):
            data = zlib.decompress(data)
            result += ' '
        elif data.startswith(b'BZh'):
            data = bz2.decompress(data)
            result += '#'
        elif data.endswith(b'\x9cx'):
            data = data[::-1]
            result += '\n'
        else:
            break
    print(result)
```

```
      ###          ###      ########    ########    ##########  ########
    #######      #######    #########   #########   #########   #########
   ##     ##    ##     ##   ##      ##  ##      ##  ##          ##      ##
  ##           ##       ##  ##      ##  ##      ##  ##          ##      ##
  ##           ##       ##  #########   #########   ########    #########
  ##           ##       ##  ########    ########    ########    ######## 
  ##           ##       ##  ##          ##          ##          ##   ## 
   ##     ##    ##     ##   ##          ##          ##          ##    ## 
    #######      #######    ##          ##          #########   ##     ## 
      ###          ###      ##          ##          ##########  ##      ##
```

Next Level
----------

http://www.pythonchallenge.com/pc/hex/copper.html


<div class="ad">
<script src='//z-na.amazon-adsystem.com/widgets/onejs?MarketPlace=US&amp;adInstanceId=0f3c2d71-0c18-4aca-be44-ba6e8892af33&amp;storeId=xstore0b-20'></script> 
</div>  