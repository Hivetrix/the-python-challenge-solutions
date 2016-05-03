# Level 15

## Problem



```
<!-- he ain't the youngest, he is the second -->
```
## Solution


```python
import datetime, calendar
for year in range(1006,1996,10):
    d=datetime.date(year, 1, 26)
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

1756-01-27 is the birthday of Mozart...

## Next Level

http://www.pythonchallenge.com/pc/return/mozart.html