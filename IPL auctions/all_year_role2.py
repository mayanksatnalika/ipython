from bs4 import BeautifulSoup
import urllib2
import numpy as np
import pandas as pd

p_name = []
role = []
pidList = pd.read_csv('all_years_cricinfo_playerids.csv')
pnames= pidList['pname']
pid= pidList['id']
for i in range(0,len(pid)):
    url = 'http://www.espncricinfo.com/ci/content/player/' + str(pid[i]) + '.html'
    print url
    page=urllib2.urlopen(url)
    soup = BeautifulSoup(page.read(),'html.parser')
    divinfo = soup.findAll('p',{'class':'ciPlayerinformationtxt'})
    for div in divinfo:
        #print div.text
        if(str(div.text).find('Playing role')!=-1):
            print div.text
            if(div.text.find('batsman')!=-1 or div.text.find('Allrounder')!=-1 or div.text.find('allrounder')!=-1 ):
                role.append(1)
                p_name.append(pnames[i])
                break
            else:
                role.append(0)
                p_name.append(pnames[i])
                break

df = pd.DataFrame()
df['role'] = role
df['pname'] = p_name
df.to_csv('player_roles_all_year.csv')
