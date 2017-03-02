from bs4 import BeautifulSoup
import urllib2
import pandas as pd
import numpy as np
from dateutil import parser
import os.path
print 'imported files'
auc2014 = pd.read_csv('all_years.csv')
pnames= []
players = auc2014['player_name']
for play in players:
    #print play
    pnames.append(str(play.replace(' ','+')))
print(len(auc2014))

player_id = []
cnt = 0
p_name = []
for player_name in pnames:

    try:
        url = 'http://www.bing.com/search?q=espncricinfo+player+' + player_name
        print url
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        page = opener.open(url)
        soup = BeautifulSoup(page.read(),"html.parser")
        #print 'bing sorted'
        #finding list a and t20 urls
        divs = soup.findAll('div',{'class':'b_attribution'})
        for div in divs:
            if (div.text.find('content/player')!=-1):
                #print div.text
                parts = div.text.rsplit('/', 1)
                #print parts[-1]
                player_id.append(int((parts[-1].split('.'))[0]))
                p_name.append(player_name)
                print cnt
                cnt+=1
                break

    except:
        continue



pids = pd.DataFrame()
pids['pname']  = p_name
pids['id'] = player_id

pids.to_csv('all_years_cricinfo_playerids.csv')
