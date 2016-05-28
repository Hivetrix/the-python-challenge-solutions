import httplib, base64

base64_login = base64.encodestring('%s:%s' % ("butter", "fly"))[:-1]
headers = {"Authorization": "Basic %s" % base64_login}
conn = httplib.HTTPConnection("www.pythonchallenge.com")

# Needless to say that normally we wouldn't know about the exact byte
# ranges yet and thus probably use infinite loops instead ...

for n in range(30203, 30314):
    headers["Range"] = "bytes=%s-%s" % (n, n + 1)
    conn.request("GET", "/pc/hex/unreal.jpg", "", headers)
    response = conn.getresponse()
    data = response.read()

    if data:
        print data

# We now know that our username is "invader".

for n in (2123456744, 2123456743):
    headers["Range"] = "bytes=%s-%s" % (n, n + 1)
    conn.request("GET", "/pc/hex/unreal.jpg", "", headers)
    response = conn.getresponse()

    print response.read()

# We learned that "the password is your new nickname in reverse", thus:
# "redavni". Further, that "it is hiding at 1152983631".

headers["Range"] = "bytes=1152983631-1152983632"
conn.request("GET", "/pc/hex/unreal.jpg", "", headers)
response = conn.getresponse()

h = open("data.zip", "wb")
h.write(response.read())
h.close()
