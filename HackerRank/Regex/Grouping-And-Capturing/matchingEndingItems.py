Regex_Pattern = r'^[a-z|A-Z]*s$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())