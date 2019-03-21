import webbrowser
import sys
import requests
import bs4

ignoredWebsites = ["twitter", "facebook", "fb", "reddit", "play.google.com"]

def start(keyword):
 foundLinks = []
 numberOfLinks = 5

 res = requests.get('https://google.com/search?q='+keyword+'&tbm=nws')
 soup = bs4.BeautifulSoup(res.text,'lxml')
 links = soup.select('.r a')
 
 for i in range(numberOfLinks):
  link = links[i].get('href')

  for ignoredWebsite in ignoredWebsites:      
   if ignoredWebsite in link:
    break

  #webbrowser.open('https://google.com' + links[i].get('href'))
  #print('https://google.com' + link)
  foundLinks.append('https://google.com' + link)

 return foundLinks