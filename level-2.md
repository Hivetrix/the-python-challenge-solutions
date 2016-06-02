# Python Challenge - Level 2

- Link: http://www.pythonchallenge.com/pc/def/ocr.html


## Problem


 ![](images/ocr.jpg)
 
> recognize the characters. maybe they are in the book, 
> but MAYBE they are in the page source.



Right click and select "View Page Source":

```html
<!--
find rare characters in the mess below:
-->

<!--
%%$@_$^__#)^)&!_+]!*@&^}@[@%]()%+$&[(_@%+%$*^@$^!+]!&_#)_*}{}}!}_]$[%}@[{_@#_^{*
@##&{#&{&)*%(]{{([*}@[@&]+!!*{)!}{%+{))])[!^})+)$]#{*+^((@^@}$[**$&^{$!@#$%)!@(&
+^!{%_$&@^!}$_${)$_#)!({@!)(^}!*^&!$%_&&}&_#&@{)]{+)%*{&*%*&@%$+]!*__(#!*){%&@++
!_)^$&&%#+)}!@!)&^}**#!_$([$!$}#*^}$+&#[{*{}{((#$]{[$[$$()_#}!@}^@_&%^*!){*^^_$^
]@}#%[%!^[^_})+@&}{@*!(@$%$^)}[_!}(*}#}#___}!](@_{{(*#%!%%+*)^+#%}$+_]#}%!**#!^_
...
```

## Solution

Save the characters in between ``<!--`` and ``-->`` to ``data.txt``

```python
f = open('data.txt', 'r')
count = {}
for line in f:
    for c in line:
        count[c] = count.get(c, 0) + 1   
print(count)
```

output:


> {'^': 6030, '&': 6043, '@': 6157, '%': 6104, 't': 1, 'i': 1, '}': 6105, '{': 6046, '$': 6046, 'u': 1, '_': 6112, 'e': 1, 'l': 1, 'y': 1, ']': 6152, 'q': 1, 'a': 1, '#': 6115, '!': 6079, ')': 6186, '\n': 1220, '*': 6034, '[': 6108, '+': 6066, '(': 6154}


The ``rare`` characters only have 1 occurrence: t, i, u, e, l, y, q, a.

If you are having a hard time to guess the meaning:

```python
import re
f = open('data.txt', 'r')
data = "".join(f.readlines())
print("".join(re.findall("[A-Za-z]", data)))
```

result:


> equality


## Next Level

http://www.pythonchallenge.com/pc/def/equality.html

## Read More

- [Python 3 - IO](http://www.hackingnote.com/en/python/io)