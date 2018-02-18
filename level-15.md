# Python Challenge - Level 15

- Link: http://www.pythonchallenge.com/pc/return/uzi.html
- Username: **huge**
- Password: **file**

## Problem

![](src/level_15/screen15.jpg)

Clues
-----

### Clue 1

There's a burnt hole on the calendar, it must be year 1xx6. 

### Clue 2

That year's Jan 1 is a Thursday. 

### Clue 3

It was a leap year, since Feb 29 is on the calendar.

### Clue 4

We are looking for Jan 26.

### Clue 5

In HTML source code:

```
<!-- he ain't the youngest, he is the second -->
```

### Clue 6

Title: ``whom?``

### Clue 7

In HTML source code:

```
<!-- todo: buy flowers for tomorrow -->
```

Exploration
-----------

So we are looking for a person, who's related to that particular date, and he is not the youngest...

The key is to find what year it was. We can filter the years between 1006 and 1996 by those clues. 

First the leap year. Is 1006 a leap year?

```python
>>> 1006 / 4
251.5
```

No, it is not, so our starting point should be 1016:

```python
>>> 1016 / 4
254.0
```

Then we can test 1036, 1056, 1076... every 20 years.

```python
>>> list(range(1016, 1996, 20))
[1016, 1036, 1056, 1076, 1096, 1116, 1136, 1156, 1176, 1196, 1216, 1236, 1256, 1276, 1296, 1316, 1336, 1356, 1376, 1396, 1416, 1436, 1456, 1476, 1496, 1516, 1536, 1556, 1576, 1596, 1616, 1636, 1656, 1676, 1696, 1716, 1736, 1756, 1776, 1796, 1816, 1836, 1856, 1876, 1896, 1916, 1936, 1956, 1976]
```

Then find the year that has Jan 26 as a Monday

```python
>>> import datetime
>>> [year for year in range(1016, 1996, 20) if datetime.date(year, 1, 26).isoweekday() == 1]
[1176, 1356, 1576, 1756, 1976]
```

From clue 5:

> he ain't the youngest, he is the second 

1976 must be the youngest, so 1756 is the second youngest... what is special with 1756-01-26? Nothing. But remember the last clue:

> todo: buy flowers for tomorrow 

And... 1756-01-27 is the birthday of Mozart...


## Solution

Alternatively we can use ``canlendar.isleap()`` to detect leap year, which makes it more clear. Check out the full solution:


```python
import datetime, calendar
for year in range(1006,1996,10):
    d = datetime.date(year, 1, 26)
    if d.isoweekday() == 1 & calendar.isleap(year):
        print(d)
```

Output

```
1176-01-26
1356-01-26
1576-01-26
1756-01-26
1976-01-26
```

## Next Level

http://www.pythonchallenge.com/pc/return/mozart.html
