from bs4 import BeautifulSoup
import requests
import random


def return_link(topic) -> str:
    string = 'https://medium.com/search?q='

    # topic is getten from javascript
    # topic='food'
    # topic = input("what topic")

    web_scrape = string + topic

    source = requests.get(web_scrape).text

    soup = BeautifulSoup(source, 'lxml')

    # p= soup.find('div', class_='col-md-9').p
    title = soup.find('title')
    p = title.text
    # . text means only print inside the tags
    # print(p)

    # ins = soup.find('ins')['style']
    # separate = soup.find('ins')['data-ad-client']
    ret = "error"

    num = 0
    randomNum = random.randint(1, 11)
    for links in soup.find_all('div', class_='postArticle-readMore'):
        # links=links.find('a', class_='button u-baseColor--buttonNormal')
        links = links.a['href']
        num += 1
        if num == randomNum:
            ret = links

    return ret
