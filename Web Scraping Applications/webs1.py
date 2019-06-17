import urllib.request #access internet and network request


'''
1.
    htmlfile=urllib.request.urlopen("http://google.com") #response text html generated

    htmltext=htmlfile.read()
    # print(htmltext) prints source code for google

'''

urls=["http://google.com","http://nytimes.com","http://CNN.com"]

for i in range(0,len(urls)):
    htmlfile=urllib.request.urlopen(urls[i])
    htmltext=htmlfile.read()
    print(htmltext)

