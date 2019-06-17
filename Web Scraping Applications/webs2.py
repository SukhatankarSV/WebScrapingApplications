import urllib.request
import re

urls=["http://google.com","http://nytimes.com","http://CNN.com"]
i=0

regexstring='<title>(.+?)</title>' # by this regex we will get all the thing between the title tags
pattern=re.compile(regexstring) #converts regex string into something interpreted by regular expressions library


while i<len(urls):
    htmlfile=urllib.request.urlopen(urls[i]) #requrest to open html page
    htmltext=str(htmlfile.read())  # hr=tmlfile.read() must be converted to string
    titles=re.findall(pattern,htmltext) # from the htmltext find all that matches the pattern
    print(titles)
    i+=1

