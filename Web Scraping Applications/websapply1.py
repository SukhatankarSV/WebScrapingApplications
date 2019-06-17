import urllib.request

import  re
'''
htmlfile=urllib.request.urlopen("http://www.walchandsangli.ac.in/AboutUs/ChairmansProfile.asp")
htmltext=(str)(htmlfile.read())


regex='span class="MatterMoreSpaced">(.+?)</span>'
pattern=re.compile(regex)

result=re.findall(pattern,htmltext)

print(result)



htmlfile=urllib.request.urlopen("view-source:http://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=137&Tx_State=0&Tx_District=0&Tx_Market=0&DateFrom=27-Dec-2016&DateTo=25-Jun-2017&Fr_Date=27-Dec-2016&To_Date=25-Jun-2017&Tx_Trend=0&Tx_CommodityHead=Ajwan&Tx_StateHead=--Select--&Tx_DistrictHead=--Select--&Tx_MarketHead=--Select--")
htmltext=(str)(htmlfile.read())

print(htmltext)
'''

import requests
from bs4 import BeautifulSoup

r=requests.get("http://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=137&Tx_State=0&Tx_District=0&Tx_Market=0&DateFrom=27-Dec-2016&DateTo=25-Jun-2017&Fr_Date=27-Dec-2016&To_Date=25-Jun-2017&Tx_Trend=0&Tx_CommodityHead=Ajwan&Tx_StateHead=--Select--&Tx_DistrictHead=--Select--&Tx_MarketHead=--Select--")

soup=(BeautifulSoup)(r.content,"html.parser")

#table_data=soup.find_all("table",{"class":"tableagmark_new"})
table_data=soup.find_all("td")

for agriproduct in table_data:
    print (agriproduct.text,end="")