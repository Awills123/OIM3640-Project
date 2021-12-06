
import csv
import urllib.request
from bs4 import BeautifulSoup


DOWNLOAD_URL = 'https://www.cnn.com/health'

def download_page(url):
    return urllib.request.urlopen(url)


def parse_html(html):
    """analyze the html page, find the information and return the move list of tuples (movie_name, year)"""
    soup = BeautifulSoup(html, features="html.parser")
#     # print(soup.prettify())
    article_table = soup.find('ul', attrs={'class': 'cn cn-list-hierarchical-xs cn--idx-0 cn-container_C599ED98-65F7-2EE8-1C38-9DBE8C506F1D'})
    # print(article_table)
    article_list = []
    for news in article_table.find_all('h3',{'class':'cd__headline'}):
        article_name = ("Title: {}".format(news.text))
        print(article_name)
        article_link = ("https://www.cnn.com{}".format(news.a['href']))
        print (f'Link: {article_link}')
        specific_articles = download_page(article_link)
        summary_soup = BeautifulSoup(specific_articles,features="html.parser")
        for links in summary_soup.find_all('p',{'class':'zn-body__paragraph speakable'}):
            article_summary = ("Brief: {}".format(links.text))
            print(article_summary)
            article_list.append((article_name,article_link,article_summary))
    return article_list
   
# parse_html(download_page(DOWNLOAD_URL).read())



def main():
    url = DOWNLOAD_URL


    with open('newspaper.reader/web_scraper.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)

        fields = ('article','link','summary')
        writer.writerow(fields)

        html = download_page(url)
        articles = parse_html(html)
        writer.writerows(articles)


if __name__ == '__main__':
    main()
