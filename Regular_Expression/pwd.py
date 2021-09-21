import re

pattern = re.compile(r"[a-zA-Z0-9_$#@&]{8,}\d")
string = "Ottoman_1212#@&3"

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(c)