# Python Challenge - Level 24

- Link: http://www.pythonchallenge.com/pc/hex/ambiguity.html
- Username: **butter**
- Password: **fly**

## Problem

![](images/maze.png)

## Solution


Load the image:

```python
>>> from PIL import Image
>>> maze = Image.open("maze.png")
>>> w, h = maze.size
```

Check the top line

```python
>>> for i in range(w): print(maze.getpixel((i, 0)))
```

There's only one black pixel(``(0, 0, 0, 255)``), others are white(``(255, 255, 255, 255)``) or grey(the upper left corner square with the number of the level), so the entrance point is ``(w - 2, 0)``.

Similarly print out the bottom line:

```python
>>> for i in range(w): print(maze.getpixel((i, h - 1)))
```

there's only one black pixel at ``(1, h - 1)``, that would be the exit point.

By printing out the "inner" pixels you may notice that the non-white points all look like ``(x, 0, 0, 255)``, where ``x`` would vary. That is the data we need to collect.

A BFS would find the shortest path:


```python
from PIL import Image

maze = Image.open("maze.png")
directions = [(0,1), (0,-1), (1,0), (-1,0)]
white = (255, 255, 255, 255)
w, h = maze.size

next_map = {}

entrance = (w - 2, 0)
exit = (1, h - 1)
queue = [exit]
while queue:
    pos = queue.pop(0)
    if pos == entrance:
        break
    for d in directions:
        tmp = (pos[0] + d[0], pos[1] + d[1])
        if not tmp in next_map and 0 <= tmp[0] < w and 0 <= tmp[1] < h and maze.getpixel(tmp) != white:
            next_map[tmp] = pos
            queue.append(tmp)

path = []
while pos != exit: 
    path.append(maze.getpixel(pos)[0])
    pos = next_map[pos]

# skipping the 0s
print(path[1::2])
open('maze.zip','wb').write(bytes(path[1::2]))
```

From the zip, a picture with the word "lake".


## Next Level

http://www.pythonchallenge.com/pc/hex/lake.html


