# Python Challenge - Level 6


- Link: http://www.pythonchallenge.com/pc/def/channel.html

## Problem




![](src/level_06/channel.jpg)

Pants? And Spiderman's underwear?

There's no text or any useful info in the source comments except for a call out of the donation button, but the big 
hint is at the very first line of html(and I missed it...):

```html
<html> <!-- <-- zip -->
```

Ok... the image was about "zip", not "pants" or anything under it...

Replace ``html`` with ``zip``: http://www.pythonchallenge.com/pc/def/channel.zip

Unzip it. In readme.txt:

```
welcome to my zipped list.

hint1: start from 90052
hint2: answer is inside the zip
```

## Solution

```python
>>> import zipfile, re
>>> 
>>> f = zipfile.ZipFile("resources/channel.zip")
>>> num = '90052'
>>> while True:
...     content = f.read(num + ".txt").decode("utf-8")
...     print(content)        
...     match = re.search("Next nothing is (\d+)", content)        
...     if match == None:
...         break
...     num = match.group(1)
... 
Next nothing is 94191
Next nothing is 85503
Next nothing is 70877
...
Next nothing is 68628
Next nothing is 67824
Next nothing is 46145
Collect the comments.
```

Comments.. what comments? 

It turns out that zip file may contain some comments, and they can be accessed by:

- [ZipFile.comment](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.comment): comment associated with the ZIP file.
- [ZipInfo.comment](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo.comment): comment for the individual archive member.

Add a few lines to collect the comments:

```python
>>> num = '90052'
>>> comments = []
>>> while True:
...     content = f.read(num + ".txt").decode("utf-8")
...     comments.append(f.getinfo(num + ".txt").comment.decode("utf-8"))
...     content      
...     match = re.search("Next nothing is (\d+)", content)        
...     if match == None:
...         break
...     num = match.group(1)
... 
>>> print("".join(comments))
****************************************************************
****************************************************************
**                                                            **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
**                                                            **
****************************************************************
 **************************************************************

```

If you try http://www.pythonchallenge.com/pc/def/hockey.html, you will get 

```
it's in the air. look at the letters.
```

The right answer is in the letters: **oxygen**


### Put Everything Together

```python
import zipfile, re

f = zipfile.ZipFile("channel.zip")
print(f.read("readme.txt").decode("utf-8"))

num = '90052'

comments = []

while True:
    content = f.read(num + ".txt").decode("utf-8")
    comments.append(f.getinfo(num + ".txt").comment.decode("utf-8"))
    print(content)    
    match = re.search("Next nothing is (\d+)", content)    
    if match == None:
        break
    num = match.group(1)

print("".join(comments))
```

## Next Level


http://www.pythonchallenge.com/pc/def/oxygen.html

<div class="ad">
<script src='//z-na.amazon-adsystem.com/widgets/onejs?MarketPlace=US&amp;adInstanceId=0f3c2d71-0c18-4aca-be44-ba6e8892af33&amp;storeId=xstore0b-20'></script> 
</div>  