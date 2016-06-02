# Python Challenge - Level 6


- Link: http://www.pythonchallenge.com/pc/def/channel.html

## Problem




![](images/channel.jpg)

Download: http://www.pythonchallenge.com/pc/def/channel.zip

In readme.txt:

```
welcome to my zipped list.

hint1: start from 90052
hint2: answer is inside the zip
```

## Solution

```python
import zipfile, re

f = zipfile.ZipFile("channel.zip")
print(f.read("readme.txt").decode("utf-8"))

num = '90052'

while True:
    content = f.read(num + ".txt").decode("utf-8")
    print(content)        
    match = re.search("Next nothing is (\d+)", content)        
    if match == None:
        break
    else:
        num = match.group(1)
```

Result:

```
Next nothing is 94191
Next nothing is 85503
...
Next nothing is 46145
Collect the comments.
```

Add a few lines to collect the comments:

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
    else:
        num = match.group(1)

print("".join(comments))
```

Result:

```
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

## Next Level

If you try http://www.pythonchallenge.com/pc/def/hockey.html, you will get 

```
it's in the air. look at the letters.
```

The right answer is in the letters: oxygen

http://www.pythonchallenge.com/pc/def/oxygen.html