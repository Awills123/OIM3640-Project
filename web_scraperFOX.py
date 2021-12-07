
import csv
import urllib.request
from bs4 import BeautifulSoup


DOWNLOAD_URL = 'https://www.foxnews.com/health'

def download_page(url):
    return urllib.request.urlopen(url)


def parse_html(html):
    """analyze the html page, find the information and return the move list of tuples (movie_name, year)"""
    soup = BeautifulSoup(html, features="html.parser")
#     # print(soup.prettify())
    article_table = soup.find('section', attrs={'class': 'collection collection-article-list'})
    # print(article_table)
    article_list = []
    for news in article_table.find_all('h4',{'class':'title'}):
        article_name = ("Title: {}".format(news.text))
        print(article_name)
        article_link = ("https://www.foxnews.com{}".format(news.a['href']))
        print (f'Link: {article_link}')
        specific_articles = download_page(article_link)
        summary_soup = BeautifulSoup(specific_articles,features="html.parser")
        links = summary_soup.find_all('p',{'class':'speakable'})
        all_text = " ".join(link.text for link in links)
        article_summary = ("Brief: {}".format(all_text))
        print(article_summary)
        article_list.append((article_name,article_link,article_summary))
    return article_list
    
def return_FOX():
    return parse_html(download_page(DOWNLOAD_URL).read())


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
