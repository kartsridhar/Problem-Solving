Regex_Pattern = r'^[123]{1}[120]{1}[xs0]{1}[30Aa]{1}[xsu]{1}[\.,]{1}$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())