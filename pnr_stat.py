import mechanize
from bs4 import BeautifulSoup 
import urllib2
# Create a Browser
b = mechanize.Browser()

# Disable loading robots.txt
b.set_handle_robots(False)

b.addheaders = [('User-agent',
                 'Mozilla/4.0 (compatible; MSIE 5.0; Windows 98;)')]

# Navigate
b.open('http://pnrstatuslive.com/')

# Choose a form
b.select_form(nr=0)



b['pnr_num'] = '8746447483'
fd = b.submit()
print "submit"
soup = BeautifulSoup(fd.read(),'html.parser')
print fd.read()
   
