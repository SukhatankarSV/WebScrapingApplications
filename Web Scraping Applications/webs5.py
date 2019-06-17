import urllib.request
import re

#htmlfile=urllib.request.urlopen("https://www.google.com/finance?q=aapl")

htmlfile=urllib.request.urlopen()
htmltext=(str)(htmlfile.read())


regex='<span id="ref_[^.]*_l">(.+?)</span>' #any string of any character repeated any no. of times ...middle regex meaning in span tag
pattern=re.compile(regex)

results=re.findall(pattern,htmltext)

print(results)