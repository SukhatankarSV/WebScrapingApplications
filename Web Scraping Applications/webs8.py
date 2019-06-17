import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage

class Client(QWebPage):

    def __init__(self,url):
        self.app=QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.quit()



url="https://pythonprogramming.net/parsememcparseface/"
client_response=Client(url)
source=client_response.mainFrame().toHtml()
soup=(BeautifulSoup)(source,'lxml')
js_test=soup.find("p",{"class":"jstest"})
#print(js_test.text)

