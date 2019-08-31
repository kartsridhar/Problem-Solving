Regex_Pattern = r'\b[aeiouAEIOU]+[a-z]*[A-Z]*\b'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())