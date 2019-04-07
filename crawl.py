import requests
from bs4 import BeautifulSoup
def crawl(URL,time):
    if time == 0:
        return
    url=requests.get(URL)#url的type是 response status code  url.text才是裡面的HTML檔
    soup=BeautifulSoup(url.text,"html.parser")#html.parser是把url.text的HTML檔當字串
    data=soup.select("body .r-ent .title a")
    findhref=soup.select(".btn-group-paging .wide")
    count=0
    for f in findhref:
        count=count+1
        if count == 2:
            print(f)
            nexthref=f
            N=nexthref.a['href']
            print(N)
#    for d in data:
#        print(d,end="\n")
crawl("https://www.ptt.cc/bbs/StupidClown/index.html",3)
