#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os
 
insta_url = 'https://www.instagram.com/p/BUlPxCIAgPn/?taken-by=thekellyyang'
 
res = requests.get(insta_url)
soup = BeautifulSoup(res.text, "lxml")

meta_part = soup.find("meta", property="og:image")
img_url = meta_part['content']
img_name = os.path.split(img_url)[1]
img_data = requests.get(img_url).content

print("Start downloading.")

with open(img_name, 'wb') as handler:
    handler.write(img_data)

print("Done.")


