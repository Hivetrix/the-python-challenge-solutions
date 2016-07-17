f = open('data.txt', 'r')
data = "".join(f.readlines())
import re
print("".join(re.findall("[A-Za-z]", data)))
