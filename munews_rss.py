#John Guseman pyproject 
import datetime
import PyRSS2Gen
import re
import requests
import bs4

#Getting data via bs4 soup
url = requests.get("http://www.monmouth.edu/news/archives")
url2 = requests.get("https://www.monmouth.edu/news/archives/page/2/")
html = url.text
html2 = url2.text
munews_soup = bs4.BeautifulSoup(html,"html.parser")
munews_soup2 =bs4.BeautifulSoup(html2,"html.parser")
articles = munews_soup.select('article')
articles2 = munews_soup2.select('article')
print(articles[0])
print(articles2[0])
print("+++++++++++++++++++++")

#Creating lists and appending information needed twice for each link to proper list
titles = []
for article in articles:
    titles.append(article['aria-label'])
for article in articles2:
    titles.append(article['aria-label'])

#print(len(titles))
#print(titles)

links = []
for article in articles:
    anchor = article.find('a')
    links.append(anchor['href'])
for article in articles2:
    anchor = article.find('a')
    links.append(anchor['href'])


#print(len(links))
#print(links)

pubDates =[]
for article in articles:
    rawdates=article.find("div", {"class": "article-meta"})
    pubD=rawdates.text.strip()#propely format dates
    pubDates.append(pubD)
for article in articles2:
    rawdates=article.find("div", {"class": "article-meta"})
    pubD=rawdates.text.strip()#propely format dates
    pubDates.append(pubD)

#print(len(pubDates))
#print(pubDates)

rss = PyRSS2Gen.RSS2(
    title = " MU news",
    link = "http://www.monmouth.edu/news/archives",
    description = "",
    lastBuildDate = datetime.datetime.now(),
    )
#Filling PyRSS with data via indexing from lists
for i in range(0, len(titles)):
    rss.items.append(PyRSS2Gen.RSSItem(
        title = titles[i],
        link = links[i],
        description = "",
        pubDate = pubDates[i],
        ))
rss.write_xml(open("mymunews.rss.xml", "w"))