import re

patternx = r'^[\w]+([\w]|\.[\w]+)*[\w]$'
pattern = '''
^
[a-z]
([\w]|\.[\w]+)*
@
([\w]|\.[\w]+)+
$
'''

while True:
    string = str(input("String: "))
    print(re.search(pattern, string, re.VERBOSE))