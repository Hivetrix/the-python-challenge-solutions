# Level 10

## Problem


len(a[30]) = ?

By clicking the image:

```
a = [1, 11, 21, 1211, 111221, 
```

## Solution

```python
a = '1'
b = ''
for i in range(0, 30):
    j = 0
    k = 0
    while j < len(a):
        while k < len(a) and a[k] == a[j]: k += 1
        b += str(k-j) + a[j]
        j = k
    print b
    a = b
    b = ''
print len(a)
```

Output: 5808

## Next Level

http://www.pythonchallenge.com/pc/return/5808.html