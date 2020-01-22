import re

token = re.findall(re.compile(r"[a-z0-9]+", re.IGNORECASE),x)
print(token)