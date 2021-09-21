import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text,'html.parser')
print(soup.select('.score'))
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for inx, item in enumerate(links):
        title = links[inx].getText()
        href = links[inx].get('href', None)
        vote = subtext[inx].select('.score')
        if len(vote):
          points = int(vote[0].getText().replace('points',''))
          if points > 99:
           hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)  

pprint.pprint(create_custom_hn(links, subtext))   
