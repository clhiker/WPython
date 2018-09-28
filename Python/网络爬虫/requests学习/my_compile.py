import re
pattern = re.compile('[a-zA-Z0-9]\w')
result = pattern.findall('as3SiOPdj#@23awe')
print(result)

