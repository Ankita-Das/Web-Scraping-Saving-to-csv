#The libraries are imported
import urllib.request
import datetime
from bs4 import BeautifulSoup
import csv
from scrape2 import cake_desp
quote_page = "https://www.bakingo.com/cake-delivery" #Site of scraping
page = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(page, "html.parser")

csv_file=open('scraped.csv','w') #The csv file is written
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Product_ID','Links','Title','Short_title','Price','Introducing','Date_Time','Description'])#The columns of csv files are named.

#The lists are defined
img_list=[] 
tit_list=[]
s_tit_list=[]
p_list=[]
intro_list=[]
pid=[]
desc_list=[]
dttm=[]


print('**************************************************')




#IMAGE URLS extracted
for b in soup.find_all("div",{'class':'cake-img'}):
    for a in b.find_all('img',src=True):
        #print ("Found the URL:", a['src'])
        links=a['src']
        #csv_writer.writerow([links])
        img_list=img_list+[links]

i=1
#CAKE-TITLES extracted
for c in soup.find_all("div",{'class':'cake-title'}):
    #print ("Found the URL:",b.text.strip())
    title=c.text.strip()
    tit_list=tit_list+[title]
    pid=pid+[i]
    i=i+1
    #csv_writer.writerow([links,title])


 #SHORT-TITLE extracted
for e in soup.find_all("div",{'class':'cake-pd'}):
    #print ("Found the URL:",b.text)
    s_tit=e.text
    #csv_writer.writerow([links])
    s_tit_list=s_tit_list+[s_tit]

#PRICE extracted   
for f in soup.find_all("div",{'class':'cake-p'}):
    #print ("Found the URL:",b.text)
    price=f.text
    #csv_writer.writerow([links])
    p_list=p_list+[price]

#CAKE-INTRODUCTION extracted and DATE-TIME saved to csv.
for g in soup.find_all("div",{'class':'cake-desc'}):
    #print ("Found the URL to move:",b.text)
    intro=g.text.strip()
    intro_list=intro_list+[intro]
    dttm=dttm+[datetime.datetime.now()]

    
#The LINKS to the next page are extracted 
#and the passed to the function cake_desp().
#This function in (next_url_scrape.py)[https://github.com/Ankita-Das/Web-Scraping-Saving-to-csv/blob/master/next_url_scrape.py] file then scrapes the cake description of the cake(whose url is passed) 
for i in soup.find_all("div",{'class':'cake-title'}):
    for j in i.find_all('a',href=True):
        url="https://www.bakingo.com"
        url=url + j['href']
        #print("Linked to page:"+ url+"\n")
        desc=cake_desp(url)
        desc_list=desc_list+[desc]



    
#Writing to the csv file from lists.
zipped=zip(pid,img_list,tit_list,s_tit_list,p_list,intro_list,dttm,desc_list)
d=list(zipped)#list of lists
#print(d)
csv_writer.writerows(d)
csv_file.close()


