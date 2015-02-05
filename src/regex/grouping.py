import re

'''
Pattern to match HTML tags
'''

pattern = re.compile(r'''
(?:
<(?P<tag>\w+)>        #starting tag
(?P<content>(?![\d]+).*)         #content
</(?P=tag)>             #ending tag
)
+?
''', re.X | re.DOTALL | re.I)

pattern2 = re.compile(r'\W+')
while True:
    string = str(input("Enter a string: "))
    m = pattern.findall(string)
    print(m)
