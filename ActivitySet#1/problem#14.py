# Using Web Services
# https://www.py4e.com/lessons/servces

rom urllib import request
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/https://replit.com/comments_1546784.xml'
print ("Retrieving", url)
html = request.urlopen(url)
data = html.read()
print("Retrieved",len(data),"characters")

tree = ET.fromstring(data)
results = tree.findall('comments/comment')
icount=len(results)
isum=0

for result in results:
    isum += float(result.find('count').text)
print(icount)
print(isum)