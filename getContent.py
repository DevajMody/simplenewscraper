import requests
import bs4
from newspaper import Article

def getContent(link):
 content = {}
 article = Article(link)
 try:
  article.download()
  article.parse()
 except:
  return "error"
 authors = article.authors
 title = article.title
 publishDate = article.publish_date
 text = article.text
 link = link.split("https://google.com/url?q=")[1]

 content["authors"] = authors
 content["title"] = title
 content["publishdate"] = publishDate
 content["link"] = link
 content["text"] = text
 
 return content
 