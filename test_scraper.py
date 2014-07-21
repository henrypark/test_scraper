#!/usr/bin/env python
#fetching top headlines of Hacker News

#importing stuff
from bs4 import BeautifulSoup
import requests

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
        print(td.text + '\n' + tda.attrs["href"] + '\n')
