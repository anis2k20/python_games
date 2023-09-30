
import re

s = 'ababababa'

i="aba"
regex = f"(?={i})"
res= len(re.findall(regex, s))

print("Number of substrings", res)