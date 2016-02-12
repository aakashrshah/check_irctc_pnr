import requests
from BeautifulSoup import BeautifulSoup
import json
import argparse

parser = argparse.ArgumentParser(description='Choose a target Host.')
parser.add_argument('--pnr', nargs='?', help='pnr')
args = parser.parse_args()


url = "http://api.checkpnrstatusirctc.in/pnrajax/pnr.php?pnrno=%d" % int(args.pnr)
# payload = {'pnrno': '8742813141'}
headers = {'Content-Type' : 'text/html'}
r = requests.get(url,headers=headers)
# print r.content
html = r.content
# print html

soup = BeautifulSoup(html)
table = soup.find('table', attrs={'class': 'table_border mdl-js-data-table'})
# print table

for row in table.findAll("tr"):
    cells = row.findAll("td")
    #For each "tr", assign each "td" to a variable.
    for item in cells:
        print str(item).strip('<td>,</td>, ')
    print("\n")