'''
two main tools for web scraping are : requests and BeautifulsOUP
requests.get (url ) fetches the html page and once it is in computer beautiful soup helps us



'''

import requests
from bs4 import BeautifulSoup

r=requests.get("https://www.yellowpages.in/hyderabad/food-stores/837087808")
#print(r.content)------------- prints html content

soup=BeautifulSoup(r.content,"html.parser")
# print(soup.prettify()) --------------- makes code clean and readable format awesome
#print(soup.find_all("a")) #finds all anker tag elements .

'''
    the parameter to soup.find_all() is any html tag whose data we want to fetch
    FIRST PARAMETER :TAG WHICH WE WANT 
    SECOND PARAMETER : JSON OBJECT OF {"KEY":"VALUE"} I.E {"CLASS":"CLASS_NAME"}

listoflinks=soup.find_all("a")
for link in listoflinks:
    print(link.text," ",link.get("href"))

'''

resultdata=soup.find_all("div",{"class":"eachPopular"})
#print(resultdata)
resultdata2=soup.find_all("div",{"class":"popularTitleTextBlock"})
'''
food_store.contents[0].text gives me all the text of the first child of div class:eachPOPULAR TAG
here in this case it gives eachPopularLeft
if it was contents[1] then it would give contents i.e text of 2nd the 2nd child of eachPopular tag i.e in this case
eachPopularRight



note correction: [0] indicates first element of list or tuple
'''
'''
-----------------------------------------------
for food_store in resultdata:
    try:
        print(food_store.contents[0].text)
    except:
        pass
    

navigate through nested divs by
div.div2.p.img["src/title"]
----------------------------------------
'''
for food_store in resultdata2:
    print(food_store.text)

