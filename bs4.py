# -*- coding: utf-8 -*-
#爬虫-大众点评


import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd 
import DataFrame
import re

html = 'https://www.dianping.com/shop/20832376/review_more?pageno=1'
# html = urlopen('https://www.dianping.com/shop/20832376/review_more?pageno=1')
# print(html.read())
html_doc = urllib.request.urlopen (html).read ()
soup = BeautifulSoup (html_doc, 'html.parser', from_encoding='utf-8')

def pls(html):
    pinglunqu = soup.find_all('div',class_="J_brief-cont")
    pls =[]
    for pinglun in pinglunqu:
        # print(pinglun.text.strip())
        pls.append (pinglun.text.strip())
    return pls

def names(html):
    name_pic = soup.find_all('div', class_="pic")
    names = []
    for name in name_pic:
        # print(name.text.strip())
        print(name.find("p", {"class": "name"}).text)
        names.append(name.text.strip())
    return names

def stars(html):
    star_span = soup.find_all('span',{"class":re.compile("^item-rank-rst irr-star([0-9])")})
    stars=[]
    for star_num in star_span:
        if "itemprop" not in star_num.attrs:
            # star=re.findall('\d+',star_num)
            
            star = star_num.attrs['class'][1][-2:]
            print(star)
            stars.append(star)
    return stars

def kouweis(html):
    kouwei_span = soup.find_all('span',class_= "rst")
    kouweis =[]
    for kouwei in kouwei_span:
        if "口味" in kouwei.text:
            print(kouwei.text)
            kouweis.append(kouwei.text)
    return kouweis

def fuwus(html):
    fuwu_span = soup.find_all('span',class_= "rst")
    fuwus =[]
    for fuwu in fuwu_span:
        if "服务" in fuwu.text:
            print(fuwu.text)
            fuwus.append(fuwu.text)
    return fuwus

def huanjings(html):
    huanjing_span = soup.find_all('span',class_= "rst")
    huanjings =[]
    for huanjing in huanjing_span:
        if "环境" in huanjing.text:
            print(huanjing.text)
            huanjings.append(huanjing.text)
    return huanjings

# print(len(stars(html)))
print(len(huanjings(html)))

df = DataFrame({'ID名字':names(html), 
                '星级': stars(html),
                '口味': kouweis(html),
                '环境': huanjings(html),
                '服务': fuwus(html),
                '点评内容': pls(html)})

df.to_csv("E:/python_code/self_learn/df.csv",index=False,encoding='utf_8_sig')
#df.to_excel("E:/python_code/self_learn/df.xls",sheet_name=’Sheet1’)
writer = pd.ExcelWriter('output.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()



