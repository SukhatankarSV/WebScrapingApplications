import requests
from bs4 import BeautifulSoup
import pandas as pd
'''
r=requests.get(url)

soup=(BeautifulSoup)(r.content,"htmlparser")

now 
nav=soup.nav // we get to nav tags
body=soup.body 

for paragraph in body.find_all('p'):              // basically finds all paragraph tags in the body
    print(paragraph.text) 

'''

r=requests.get("https://pythonprogramming.net/parsememcparseface/")
soup=(BeautifulSoup)(r.content,"html.parser")

#print(soup.prettify())
# .FIND_ALL WILL ALWAYS RETURN A TUPLE HENCE for I IN XYZ: do somethinfg is almost true everytime
table_rows=soup.find_all("tr")

for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text for i in td]
    print(row)

