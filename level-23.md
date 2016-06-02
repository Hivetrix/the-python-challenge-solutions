# Python Challenge - Level 23

- Link: http://www.pythonchallenge.com/pc/hex/bonus.html
- Username: **butter**
- Password: **fly**

## Problem

![](images/bonus.jpg)


## Solution

``this`` is a special module in Python:

```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

The string is internally stored as ``this.s``:

```python
>>> print(this.s)
Gur Mra bs Clguba, ol Gvz Crgref

Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyrk.
Pbzcyrk vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcnefr vf orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orngf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!
```

The text is ``rot-13`` encoded(rotate by 13 characters.

```
>>> import this
>>> print(codecs.decode(this.s, "rot-13"))
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```


And there's a built-in dict for the rotation:

```python
>>> this.d
{'n': 'a', 'J': 'W', 'o': 'b', 'r': 'e', 'T': 'G', 'K': 'X', 'v': 'i', 'H': 'U', 'L': 'Y', 'q': 'd', 'w': 'j', 'O': 'B', 'e': 'r', 'S': 'F', 'l': 'y', 'X': 'K', 'I': 'V', 'a': 'n', 'Z': 'M', 'G': 'T', 'i': 'v', 'f': 's', 'u': 'h', 'h': 'u', 'N': 'A', 'R': 'E', 'P': 'C', 'M': 'Z', 'C': 'P', 'b': 'o', 'U': 'H', 'A': 'N', 'B': 'O', 'W': 'J', 'D': 'Q', 'k': 'x', 'c': 'p', 'x': 'k', 'm': 'z', 'F': 'S', 'V': 'I', 'E': 'R', 'Q': 'D', 'p': 'c', 'g': 't', 'Y': 'L', 'j': 'w', 'y': 'l', 's': 'f', 't': 'g', 'z': 'm', 'd': 'q'}
```

So you can also do:

```python
>>> print("".join([this.d.get(c, c) for c in this.s]))
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

Use this to decode the message:

```python
>>> s = 'va gur snpr bs jung?'
>>> print("".join([this.d.get(c, c) for c in s]))
in the face of what?
```

From the "Zen": 

> In the face of ambiguity, ...

The answer is "ambiguity"

## Next Level

http://www.pythonchallenge.com/pc/hex/ambiguity.html