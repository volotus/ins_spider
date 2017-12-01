#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 @Author     : volotus
 @Contact    : ber1956@gmail.com
"""


import json
import re
import bs4 as bs
import requests

web_link = "https://www.instagram.com/huasilaoye/"

page = requests.get(web_link)
html_contents = page.text
soup = bs.BeautifulSoup(html_contents, 'lxml')
data  = soup.find_all("script")

jsondata = str(data[2])
jd = str(jsondata[52:])
newdata = str(jd[:-10])
mydict = json.loads(newdata)

id = list()
src_link = list()
id_count = 0
f = 0

for i in range(1000):
    try:
        id_count+=1
        id = (mydict['entry_data']['ProfilePage'][0]['user']['media']['nodes'][i]['id'])
        print(id_count,"....",id)
    except:
        last_id = id
        print("last id:........ ",id)
        print("located all id's")
        id_count-1
        print("id_count:.......",id_count-1)
        break

for i in range(id_count-1):
    f = f+1
    try:
        src = (mydict['entry_data']['ProfilePage'][0]['user']['media']['nodes'][i]['display_src'])

    except:
        print("image address indetifying finished")
    if src in src_link:
        print("duplicate image link found")
    src_link.append(src)


for i in src_link:
    print i



