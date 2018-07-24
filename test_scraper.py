#!/usr/bin/env python
#fetching top headlines of Hacker News

#load import module BeautifulSoup
from bs4 import BeautifulSoup
import requests

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

#asks user to manually type in the URL
url = raw_input("Enter a website to extract from: ")

#HTTP GET request
r = requests.get("http://" +url)

#creating the soup
soup = BeautifulSoup(r.text)

#filter for all tds associated with the class "title"
for td in soup.findAll("td", { "class":"title" }):
    #then find all <a> tags in that subset
    for tda in td.findAll("a"):
        #return the title and URL for each post
        print(color.BLUE + td.text + color.END + '\n' + tda.attrs["href"] + '\n')
