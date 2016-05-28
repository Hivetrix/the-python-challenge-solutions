from urllib.request import urlopen
import re

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"

#num = "12345"
num = str(16044/2)

while True:
    content = urlopen(uri % num).read().decode('utf-8')
    print(content)
    match = re.search("and the next nothing is (\d+)", content)
    if match == None:
        break
    else:
        num = match.group(1)
    
