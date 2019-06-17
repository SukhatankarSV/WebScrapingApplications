import urllib.request
import re

symbolfile=open("G:\\stocksymbol.txt")
symbollist=symbolfile.read()
symbollist=symbollist.split("\n")

#print(symbollist)

i=0
for i in range(0,len(symbollist)):
    url="https://in.finance.yahoo.com/q?s="+symbollist[i]+"&ql=1"
    htmlfile=urllib.request.urlopen(url)
    htmltext=(str)(htmlfile.read())

    regex='<span id="yfs_l84_[^.]*">(.+?)</span>'
    #regex='<span class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)">(.+?)</span>'
    pattern=re.compile(regex)
    price=re.findall(pattern,htmltext)
    print(price)
