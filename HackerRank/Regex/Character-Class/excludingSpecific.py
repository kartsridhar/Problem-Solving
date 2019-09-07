Regex_Pattern = r'^\D[^aeiou]{1}[^bcDF]{1}\S[^AEIOU]{1}[^\.,]{1}$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())