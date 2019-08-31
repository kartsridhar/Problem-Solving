Regex_Pattern = r'(ok)(ok)(ok)+'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())