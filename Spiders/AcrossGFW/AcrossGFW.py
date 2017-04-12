#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Collect and modify hosts
'''

from datetime import date
__author__="NoBystander"
__date__=str(date.today())

import requests
import bs4

root_url="http://www.360kb.com"
google_url=root_url+"/kb/2_122.html"
facebook_url=root_url+"/kb/2_139.html"

all_url="https://raw.githubusercontent.com/nobystander/toys/master/Script/AcrossGFW/hosts"

def get_urls(url,ele):
    response = requests.get(url) 
    soup = bs4.BeautifulSoup(response.text)
    return [a for a in soup.select(ele)]

Google=str(get_urls(google_url,'pre')[0])
Google=Google[Google.find('#'):-8]
All=str(get_urls(all_url,'p')[0])
All=All[All.find('#'):-8]

#print Google 
#print All 

with open('/etc/hosts','w') as f:
    f.write(Google+'\n\n')
    f.write(All+'\n\n')

