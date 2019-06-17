import urllib.request
import re

htmlfile=urllib.request.urlopen("https://in.finance.yahoo.com/quote/AAPL?p=AAPL")
htmltext=(str)(htmlfile.read())



#regex='<span class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)" data-reactid="35">(.+?)</span>'
regex='<span id="yfs_184_aapl>(.+?)</span>'

pattern=re.compile(regex)

price=re.findall(pattern,htmltext)
print(price)