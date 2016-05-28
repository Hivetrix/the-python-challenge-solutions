# Level 20

- Link: http://www.pythonchallenge.com/pc/hex/idiot2.html
- Username: **butter**
- Password: **fly**

## Problem

![](images/unreal.jpg)


> but inspecting it carefully is allowed.



## Solution

```python
import urllib.request, base64

request = urllib.request.Request('http://www.pythonchallenge.com/pc/hex/unreal.jpg')
cred = base64.b64encode(b"butter:fly")
request.add_header("Authorization", "Basic %s" % cred.decode())
print(request.headers)
# {'Authorization': 'Basic YnV0dGVyOmZseQ=='}

response = urllib.request.urlopen(request)
print(response.headers)
# Content-Type: image/jpeg
# Content-Range: bytes 0-30202/2123456789
# Connection: close
# Transfer-Encoding: chunked
# Server: lighttpd/1.4.35

```

So it is a huge file(length of 2123456789) however only a small portion is served(0 to 30202). Try to get the content after that:

```python
pattern = re.compile('bytes (\d+)-(\d+)/(\d+)')
content_range = response.headers['content-range']
(start, end, length) = pattern.search(content_range).groups()
request.headers['Range'] = 'bytes=%i-' % (int(end) + 1)
response = urllib.request.urlopen(request)
print(response.headers)
# {'Authorization': 'Basic YnV0dGVyOmZseQ=='}
# Content-Type: application/octet-stream
# Content-Transfer-Encoding: binary
# Content-Range: bytes 30203-30236/2123456789
# Connection: close
# Transfer-Encoding: chunked
# Server: lighttpd/1.4.35

print(response.read().decode())
# Why don't you respect my privacy?
```

So now the content between 30203 and 30236 is served, which is "Why don't you respect my privacy?"; continue for a few iterations:

```python
pattern = re.compile('bytes (\d+)-(\d+)/(\d+)')
content_range = response.headers['content-range']
(start, end, length) = pattern.search(content_range).groups()

while True:
    try:
        request.headers['Range'] = 'bytes=%i-' % (int(end) + 1)
        response = urllib.request.urlopen(request)
        print(response.read().decode())
        print(response.headers)
        (start, end, length) = pattern.search(response.headers['content-range']).groups()
    except: 
        break
```

It prints:

```
Why don't you respect my privacy?

we can go on in this way for really long time.

stop this!

invader! invader!

ok, invader. you are inside now. 
```

The last request ends at 30346.


Go to http://www.pythonchallenge.com/pc/hex/invader.html

> Yes! that's you!

What about content after the length:

```python
request.headers['Range'] = 'bytes=%i-' % (int(length) + 1)
response = urllib.request.urlopen(request)
print(response.headers)
print(response.read().decode())
```

Result:

```
Content-Type: application/octet-stream
Content-Transfer-Encoding: binary
Content-Range: bytes 2123456744-2123456788/2123456789
Connection: close
Transfer-Encoding: chunked
Server: lighttpd/1.4.35

esrever ni emankcin wen ruoy si drowssap eht
```

The content is reversed: "the password is your new nickname in reverse". The "nickname" is "invader", so password is "redavni".

Now "reverse" the search: 

```python
request.headers['Range'] = 'bytes=2123456743-'
response = urllib.request.urlopen(request)
print(response.headers)
print(response.read().decode())
```

```
Content-Type: application/octet-stream
Content-Transfer-Encoding: binary
Content-Range: bytes 2123456712-2123456743/2123456789
Connection: close
Transfer-Encoding: chunked
Date: Mon, 02 May 2016 18:12:45 GMT
Server: lighttpd/1.4.35


and it is hiding at 1152983631.
```

Then save it as a zip file:

```python
request.headers['Range'] = 'bytes=1152983631-'
response = urllib.request.urlopen(request)

with open("level21.zip", "wb") as f:
    f.write(response.read())
```

Unzip it with the password("redavni").

> Yes! This is really level 21 in here. 
> And yes, After you solve it, you'll be in level 22!
>
> Now for the level:
>
> * We used to play this game when we were kids
> * When I had no idea what to do, I looked backwards.

## Next Level

Inside the zip file