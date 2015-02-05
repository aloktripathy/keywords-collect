import json
import textfilter

filename = str(input('Enter the filename: '))
report = textfilter.keyword_occurences(filename)
if report != None:
    q = str(input('Do you want to write the report to a file?<y:default, n: no, anything else: filename>: '))
    filename = 'report.json'
    if q.lower() == 'n':
        pass
    elif q.lower() == 'y':
        textfilter.write_file(filename, json.dumps(report))
    else:

        filename = q + '.json'
        textfilter.write_file(filename, json.dumps(report))