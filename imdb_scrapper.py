import wikipedia
from bs4 import BeautifulSoup
import requests
import re
from pymongo import MongoClient
from pprint import pprint as pp

# MongoDB Setup
client = MongoClient()
db = client.search_engineDB

# creating collection or tables
posts = db.actor_data

# IMDB data scrap
name_list = []
url = "https://www.imdb.com/list/ls025814950/"
req = requests.get(url)

# Initialize BeautifulSoup and parse Html Source from url above
soup = BeautifulSoup(req.content.decode('utf-8'), 'html.parser')

# Get the links for every name for 100 actors.
# Regular expressions because it proved to be useful for matching all the
# text in links that are random.

names = soup.find("div", {"class": "lister list detail sub-list"})\
    .findAll("a", href=re.compile('(/name/)+([a-z0-9A-Z])+(.*nmls_hd)'))

#
# print(names)
# # iterate through all the links and append the actual name within the <a> tag to a list
for name in names:
    name = name.string.rstrip("\n")
    name_list.append(name)


subtitle_list = []
subtitle = soup.find("div", {"class": "lister list detail sub-list"})\
    .findAll("p", {"class": "text-muted text-small"})

for subs in subtitle:
    subs = subs.getText()
    subs = subs.replace("\n", "").strip(" ")
    subtitle_list.append(subs)

# pp(subtitle_list)

image_list = []
images = soup.find("div", {"class": "lister list detail sub-list"})\
    .findAll("img", {"src": re.compile('(https://m.media-amazon.com/images/M/)+'
                                       '([a-z0-9A-Z,@_.*])+(.*jpg)')})
for image in images:
    image_list.append(image['src'])

# print(name_list)

count = 1

# main iteration to get all data to mongodb
for name in name_list:

    # get the entire page by passing 1 name at a time
    wikipage = wikipedia.page(name)

    # print("Page Title: %s" % wikipage.title)
    # print("Page URL: %s" % wikipage.url)
    # print("No. of images on page: %d" % len(wikipage.images))
    # print("Summary: \n %s " % wikipage.summary)

    # # many images so it's better to keep in list I guess
    # for image in wikipage.images:
    #     image_list.append(image)

    # get the DOB from Summary of the Actors
    dob = wikipage.summary
    dob = dob[dob.find("born") + 5:dob.find(")")]

    # a dictionary format for 1 actor
    post = {
        "_id": count,
        "Actor": wikipage.title,
        "Url": wikipage.url,
        "Subtitle": subtitle_list[count-1],
        "Summary": wikipage.summary,
        "Images": image_list[count-1],
        "Dob": dob
    }

    # insert one to mongodb
    post = posts.insert_one(post)
    count += 1

    # get the id if successful
    print(post.inserted_id)