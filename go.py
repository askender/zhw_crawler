import read
from conf import handler_dom, CITY
import json
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from mongokit import Connection
conn = Connection()
party = conn.party.party


def view(r):
    print json.dumps(r, ensure_ascii=False, indent=4)

flag = 0
mycsv = csv.writer(sys.stdout)
# for dom in read.analyse_data():
#     for r in handler_dom(dom):
#         r['location'] = CITY
#         r['type'] = 'party'
#         if not party.find_one({'_id': r['_id']}):
#             party.insert(r)
#         else:
#             print r['title']
        # view(r)
        # if not flag:
        #     mycsv.writerow(r.keys())
        #     flag = 1
        # mycsv.writerow(r.values())
for r in party.find():
    if not flag:
        mycsv.writerow(r.keys())
        flag = 1
    mycsv.writerow(r.values())
