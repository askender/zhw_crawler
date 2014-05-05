import json
import tablib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from mongokit import Connection
conn = Connection()
party = conn.party.party


def view(r):
    print json.dumps(r, ensure_ascii=False, indent=4)

flag = 0
data = []
for r in party.find():
    if not flag:
        headers = r.keys()
        flag = 1
    data.append(r.values())
data = tablib.Dataset(*data, headers=headers)
print data.csv
with open('partys.xls', 'wb') as f:
    f.write(data.xls)
