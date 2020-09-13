import requests
from bs4 import BeautifulSoup
def crawl(URL,time):
    if time == 0:
        return
    url=requests.get(URL)#url的type是 response status code  url.text才是裡面的HTML檔
    soup=BeautifulSoup(url.text,"html.parser")#html.parser是把url.text的HTML檔當字串
    data=soup.select("body .r-ent .title a")
    for j in data:
        print(j)
    findhref=soup.select(".btn-group-paging .wide")
    #print("finding href:")
    count=0
    for j in findhref:
        if count == 1:
            nextpage = j;
      #      print(nextpage);
       # print(j)
        count=count+1;
    nexturl=str(nextpage)
    count=0;
    NU=str('')
    for n in nexturl:
        count=count+1
        if count < 58 and count > 26:
            NU=NU+n
            #print(NU)
    nexturl="https://www.ptt.cc"+str(NU)
    print("nexturl=")
    print(nexturl)
    time=time-1;
    crawl(nexturl,time)
#    for d in data:
#        print(d,end="\n")


crawl("https://www.ptt.cc/bbs/StupidClown/index.html",3)
