import os
import string

import requests
from bs4 import BeautifulSoup


number_of_pages = int(input())  # take number of pages from user
user_type = input()  # take type of article that user want to collect
parent_dir = os.getcwd()  # get current working directory

for page_number in range(1, number_of_pages+1):

    query = {'page': str(page_number)}  # make a query that get a certain page and add it to url
    r = requests.get("https://www.nature.com/nature/articles?sort=PubDate&year=2020",
                     params=query, headers={'Accept-Language': 'en-US,en;q=0.5'})   # make request
    page_content = r.content
    soup = BeautifulSoup(page_content, 'html.parser')  # prepare soup
    articles = soup.find_all('article')  # get all elements with tag article
    article_number = 1
    article_title_link = {}  # dictionary that will contain pairs of ('title', 'url') for each article

    for article in articles:
        article_file_name = f'{page_number}:article#{article_number}.html'
        fptr = open(article_file_name, 'wb')
        fptr.write(article.encode("utf-8"))  # create html for every single article.
        fptr.close()
        article_number += 1

        fptr = open(article_file_name, 'r')  # open the created html file for article
        file_content = fptr.read()  # read it's content as a string
        article_soup = BeautifulSoup(file_content, 'html.parser')  # parse it using soup
        type_of_article = article_soup.find('span', {'data-test': 'article.type'})  # get type of this article
        link = article_soup.find('a', {'data-track-action': "view article"})  # get link of this article
        article_type = type_of_article.text.strip('\n')  # removing any blank lines from article type

        if article_type == user_type:  # check for the given type form the user
            title = link.text
            url = 'https://www.nature.com'+link.get('href')  # create url for the matched article
            article_title_link.update({title: url})  # add title and url of the matched article to dictionary
        fptr.close()
        os.remove(os.path.join(parent_dir, article_file_name))

    curren_dir_name = f'Page_{page_number}'
    os.mkdir(curren_dir_name)  # create directory for page number i
    os.chdir(os.path.join(parent_dir, curren_dir_name))  # change working directory to Page_N so that files stored on it

    for title, link in article_title_link.items():  # loop through each title and link of each matched article
        for c in title:  # make title readable
            if c in string.punctuation:
                article = title.replace(c, '')
        title = title.strip()
        title = title.replace(' ', '_')
        fptr = open(f'{title}.txt', 'wb')

        r = requests.get(link, headers={'Accept-Language': 'en-US,en;q=0.5'})  # create a new request for match article
        soup = BeautifulSoup(r.content, 'html.parser')  # parse request
        article_body = soup.find('div', {'class': 'c-article-body main-content'})  # get body of request
        fptr.write(article_body.text.encode('utf-8'))
        fptr.close()
    os.chdir(parent_dir)  # after finishing from page return to parent directory.

print("Saved all articles.")




