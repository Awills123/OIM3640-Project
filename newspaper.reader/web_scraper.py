import csv
import urllib.request
from bs4 import BeautifulSoup


DOWNLOAD_URL = 'https://www.cnn.com/health'

def download_page(url):
    return urllib.request.urlopen(url)


# print(download_page(DOWNLOAD_URL).read())


def parse_html(html):
    """analyze the html page, find the information and return the move list of tuples (movie_name, year)"""
    soup = BeautifulSoup(html, features="html.parser")
    # print(soup.prettify())
    article_table = soup.find('div', attrs={'class': 'column zn__column--idx-1'})
    print(article_table)
    # article_list = []
    # for article_row in article_table.find_all(''):
    #     article_detail = article_row.find('li', attrs={'class': 'titleColumn'})
    #     # print(movie_detail)
    #     movie_name = article_detail.find('a').string
    #     # print(movie_name)
    #     year = article_detail.find('span', attrs={'class': 'secondaryInfo'}).string.strip(
    #         '()'
    #     )
    #     # print(year)
    #     article_list.append((movie_name, year))
    # return article_list




