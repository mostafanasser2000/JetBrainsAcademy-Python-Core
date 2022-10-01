import argparse
import os
from collections import deque
import requests
import re
from bs4 import BeautifulSoup
from colorama import Fore
# write your code here


def print_highlighted(lst_links, lst):
    for line in lst:
        if line in lst_links:
            print(Fore.BLUE + line)
        print(line)


parser = argparse.ArgumentParser(description="Thia create a directory to save tabs")
parser.add_argument("dir_name")
args = parser.parse_args()
directory_name = os.path.join(os.getcwd(), args.dir_name)

if not(os.access(directory_name, os.F_OK)):  # check if there is a directory with the same name
    os.mkdir(directory_name)
os.chdir(directory_name)

url = ""
pages = deque()  # create a stack of visited web pages.

while True:
    url = input()
    links_text = []
    if url == "exit":
        break
    if url == "back" and pages:
        print_highlighted(links_text, pages.pop())
    elif url == "back":
        continue
    else:
        valid_url = re.match(r"[A-z0-9]+[.]+[\w]+", url, flags=re.I)
        if not valid_url:  # check if url is valid or not
            print(Fore.RED, "Invalid URL")
            break
        if not (url.startswith("https://")):  # check if url start with https://
            url = "https://" + url
        file_name = url[8:].split('.')[0]
        if not (url.startswith("https://")):
            url = "https://" + url

        r = requests.get(url)  # make a request to the webpage
        if r.status_code != 200:  # if request is failed
            print(Fore.RED, f"ERROR {r.status_code}")
            break

        soup = BeautifulSoup(r.content, 'html.parser')
        links = soup.find_all('a')  # get all links from html document to highlight links

        for link in links:
            links_text.append(link.text.strip())

        text_of_page = soup.stripped_strings
        pages.appendleft(text_of_page)
        print_highlighted(links_text, text_of_page)

        if not(os.access(file_name, os.F_OK)):  # check if file to webpage exist or not
            with open(file_name, "w", encoding='utf-8') as site:
                print(list(text_of_page))
                for line in text_of_page:
                    site.write(line)
        if url == file_name:  # url is the name of the file page
            with open(file_name, 'r') as site:
                print_highlighted(links_text, site.readlines())
