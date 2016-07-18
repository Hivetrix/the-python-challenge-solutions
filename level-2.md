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

### Load Data


You can manually copy-and-paste the text to a file(``resources/level2.txt`` in source code), then read from it:

```python
>>> data = open('resources/level2.txt').read()
```

Or extract the text from HTML directly. First load raw html source coding using ``urllib.request``:

```python
>>> import urllib.request
>>> html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()
```

Then extract the comment blocks in html. Note that by default dot does not match ``\n``, so we need to use ``re
.DOTALL`` flag. 

```python
>>> import re
>>> comments = re.findall("<!--(.*?)-->", html, re.DOTALL)
```

Alternatively we can use this:

```python
>>> comments = re.findall("<!--([\w\n]*?)-->", html)
```

The pattern ``<!--(.*)-->`` will capture all blocks inside ``<!--`` and ``-->``. We only care about the last part, so

```python
>>> data = comments[-1]
```

### Find the Rare Characters

```python
>>> count = {}
>>> for c in data:
...     count[c] = count.get(c, 0) + 1
... 
>>> count
{'*': 6034, '$': 6046, 'i': 1, '!': 6079, '[': 6108, 'u': 1, 'e': 1, '@': 6157, '#': 6115, 't': 1, '(': 6154, '+': 6066, '&': 6043, 'q': 1, 'l': 1, '%': 6104, '{': 6046, '}': 6105, 'a': 1, '^': 6030, ']': 6152, '\n': 1221, 'y': 1, '_': 6112, ')': 6186}
```

The ``rare`` characters only have 1 occurrence: t, i, u, e, l, y, q, a.

### In the right order

If you are having a hard time to guess the meaning:

```python
>>> import re
>>> "".join(re.findall("[A-Za-z]", data))
'equality'
```

result:


> equality


## Next Level

http://www.pythonchallenge.com/pc/def/equality.html

## Read More

- [Python 3 - IO](http://www.hackingnote.com/en/python/io)