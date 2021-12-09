
import csv
import urllib.request
from bs4 import BeautifulSoup


DOWNLOAD_URL = 'https://www.cnn.com/health'

"""opens the url and makes it readable to Beautifulsoup"""
def download_page(url):
    return urllib.request.urlopen(url)


def parse_html1(html):
    """analyze the html page, find the information and return the move list of tuples (movie_name, year)"""
    soup = BeautifulSoup(html, features="html.parser")
#     # print(soup.prettify())
    """finds the type of class using Beautifulsoup to find the appropriate elements to output"""
    article_table = soup.find('ul', attrs={'class': 'cn cn-list-hierarchical-xs cn--idx-0 cn-container_C599ED98-65F7-2EE8-1C38-9DBE8C506F1D'})
    # print(article_table)
    """creates a new empty list for the elements to be put in"""
    article_list = []
    """creates a for loop to find the following elements: Title, Link, and first paragraph"""
    for news in article_table.find_all('h3',{'class':'cd__headline'}):
        """Outputs the title for us"""
        article_name = ("Title: {}".format(news.text))
        print(article_name)
        """Outputs the link for us by looking at href"""
        article_link = ("https://www.cnn.com{}".format(news.a['href']))
        print (f'Link: {article_link}')
        """opens the specific articles and uses urlopen"""
        specific_articles = download_page(article_link)
        """Uses Beautifulsoup to be able to find specific elements"""
        summary_soup = BeautifulSoup(specific_articles,features="html.parser")
        """tells the forloop to look within a specific class to find the first paragraph"""
        for links in summary_soup.find_all('p',{'class':'zn-body__paragraph speakable'}):
            """Prints the brief"""
            article_summary = ("Brief: {}".format(links.text))
            print(article_summary)
            """appends the title,link, and summary to the list"""
            article_list.append((article_name,article_link,article_summary))
    return article_list

"""Automates the function above so flask doesn't have to be running"""
def return_CNN():
    return parse_html1(download_page(DOWNLOAD_URL).read())


"""this function is not critical to the website but it stores all the information into a csv file"""
def main():
    url = DOWNLOAD_URL


    with open('newspaper.reader/web_scraper.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)

        fields = ('article','link','summary')
        writer.writerow(fields)

        html = download_page(url)
        articles = parse_html1(html)
        writer.writerows(articles)


if __name__ == '__main__':
    main()
