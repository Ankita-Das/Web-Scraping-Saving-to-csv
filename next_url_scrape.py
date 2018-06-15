import urllib.request
import datetime
from bs4 import BeautifulSoup
#This function is called from previous file scrape.py
def cake_desp(url):
    print("the URL:"+ url)
    quote_page=url
    page=urllib.request.urlopen(quote_page)
    soup=BeautifulSoup(page,"html.parser")

    price=soup.find('div',attrs={'class':'field field-name-commerce-price field-type-commerce-price field-label-hidden'})
    price=price.text.strip()
    print(price)


    #CAKE-DESCRIPTION extracted
    description=soup.find('div',attrs={'class':'field field-name-field-description field-type-text-long field-label-hidden'})
    description=description.text.strip()
    print(description)
    return description



