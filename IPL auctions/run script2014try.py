from bs4 import BeautifulSoup
import urllib2
import pandas as pd
import numpy as np
from dateutil import parser
import os.path
print 'imported files'

auc2014 = pd.read_csv('2014_auctions.csv')
pnames= []
players = auc2014['player_name']
for play in players:
    pnames.append(str(play.replace(' ','+')))



for player_name in pnames:
    try:

        fname = 'score_files/2014_t20_' + str(player_name) + '.csv'
        print fname
        print player_name
        if (os.path.isfile(fname)):
            print 'file exists'
            continue

        url = 'http://www.bing.com/search?q=cricketarchive.com+player+' + player_name
        print url
        #url  ='http://www.bing.com/search?q=cricketarchive.com+player+ms+dhoni'
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        page = opener.open(url)
        soup = BeautifulSoup(page.read(),"html.parser")
        print 'bing sorted'
        #finding list a and t20 urls
        divs = soup.findAll('div',{'class':'b_attribution'})
        for div in divs:
            print 'in div bhai'
            print div.text

            if str(div.text).find('cricketarchive.com/Archive/Players') != -1 or str(div.text).find('cricketarchive.com/Players')!= -1 :


                #__________________MAKE CHANGES SOME HAS ARCHIVE SOME DONT IN URL______________________
                if str(div.text).find('cricketarchive.com/Archive/Players') != -1:
                    types= 1

                else:
                    types = 2
    		        





                print div.text
                s1 = div.text
                s2 = 'Players'
                req_str =  s1[s1.index(s2) + len(s2):]
                wrds =  req_str.split('/')
                final_str = wrds[1]+ '/' + wrds[2]
                #print final_str
                if types == 1:
                    listA_url = str('http://cricketarchive.com/Archive/Players/'+final_str+'/List_A_Matches.html')
                    t20_url =   str('http://cricketarchive.com/Archive/Players/'+final_str+'/Twenty20_Matches.html')
                else:

                    listA_url = str('http://cricketarchive.com/Players/'+final_str+'/List_A_Matches.html')
                    t20_url =   str('http://cricketarchive.com/Players/'+final_str+'/Twenty20_Matches.html')

                break
        #urls found out

        listA_runs = []
        t20_runs = []
        listA_balls = []
        t20_balls = []
        listA_date = []
        t20_date = []


        page = opener.open(listA_url)
        soup = BeautifulSoup(page.read(),"html.parser")
        table = soup.findAll('table')


        rows =  table[0].findAll('tr')
        #print rows[0]
        date_start  = '2013-02-13'
        date_end  = '2014-02-13'

        for row in rows:
            tds  = row.findAll('td')
            #print tds[1].text
            date  = parser.parse(str(tds[1].text))
            if date > parser.parse(date_start) and date < parser.parse(date_end):
                print date.date()
                #listA_date.append(str(date.date()))
                mlink = tds[4].find('a')
                match_link = 'http://cricketarchive.com/' + mlink['href']
                print match_link
                match_page = opener.open(match_link)
                match_soup = BeautifulSoup(match_page.read(),"html.parser")
                #print match_soup

                found  = 0
                tabs = match_soup.findAll('table')


                rows = tabs[3].findAll('tr')
                for row in rows:
                    tds  = row.findAll('td')
                    if len(tds)  < 4:
                        continue
                    if tds[0].find('a'):
                        link_text =  tds[0].find('a')['href']
                        if link_text.find(final_str) != -1:
                            #print tds[2].text
                            #print tds[3].text
                            listA_runs.append(tds[2].text)
                            listA_balls.append(tds[3].text)
                            found =  1
                            listA_date.append(str(date.date()))
                            break
                if (found== 1 ):
                    continue


                rows = tabs[1].findAll('tr')
                for row in rows:
                    tds  = row.findAll('td')
                    if len(tds) < 4:
                        continue
                    #print tds[0]
                    if tds[0].find('a'):
                        link_text =  tds[0].find('a')['href']
                        if link_text.find(final_str) != -1:
                            listA_runs.append(tds[2].text)
                            listA_balls.append(tds[3].text)
                            listA_date.append(str(date.date()))
                            break
                            #print tds[2].text
                            #print tds[3].text
        print 'work done for odis, now for t20s'



        page = opener.open(t20_url)
        soup = BeautifulSoup(page.read(),"html.parser")
        table = soup.findAll('table')
        rows =  table[0].findAll('tr')
        #print rows[0]
        date_start  = '2013-02-13'
        date_end  = '2014-02-13'

        for row in rows:
            tds  = row.findAll('td')
            #print tds[1].text
            date  = parser.parse(str(tds[1].text))
            if date > parser.parse(date_start) and date < parser.parse(date_end):
                print date.date()
                #t20_date.append(str(date.date()))
                mlink = tds[4].find('a')
                match_link = 'http://cricketarchive.com/' + mlink['href']
                print match_link
                match_page = opener.open(match_link)
                match_soup = BeautifulSoup(match_page.read(),"html.parser")
                #print match_soup

                found  = 0
                tabs = match_soup.findAll('table')


                rows = tabs[3].findAll('tr')
                for row in rows:
                    tds  = row.findAll('td')
                    if len(tds) < 4:
                        continue
                    #print tds[0]
                    if tds[0].find('a'):
                        link_text =  tds[0].find('a')['href']
                        if link_text.find(final_str) != -1:
                            #print tds[2].text
                            #print tds[3].text
                            t20_runs.append(tds[2].text)
                            t20_balls.append(tds[3].text)
                            found =  1
                            t20_date.append(str(date.date()))
                            break
                if (found== 1 ):
                    continue


                rows = tabs[1].findAll('tr')
                for row in rows:
                    tds  = row.findAll('td')
                    #print tds[0]
                    if len(tds)<4:
                        continue
                    if tds[0].find('a'):
                        link_text =  tds[0].find('a')['href']
                        if link_text.find(final_str) != -1:
                            t20_runs.append(tds[2].text)
                            t20_balls.append(tds[3].text)
                            t20_date.append(str(date.date()))
                            break
                            #print tds[2].text
                            #print tds[3].text
        print 't20s done'

        listA = pd.DataFrame()
        listA['date'] = listA_date
        listA['runs'] = listA_runs
        listA['balls'] = listA_balls
        fname = 'score_files/2014_listA_' + str(player_name) + '.csv'
        listA.to_csv(fname, encoding='utf-8')

        t20 = pd.DataFrame()
        t20['date'] = t20_date
        t20['runs'] = t20_runs
        t20['balls'] = t20_balls
        fname = 'score_files/2014_t20_' + str(player_name) + '.csv'
        t20.to_csv(fname, encoding='utf-8')

    except:
        continue
