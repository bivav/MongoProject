from pprint import pprint as pp

from pymongo import MongoClient

client = MongoClient()

db = client.search_engineDB

data = db.actor_data

# print all documents
post = []
summary = []
dob = []
subtitle = []
url_link = []
images = []

data_list = []
main_list = []

for posts in data.find({'Actor': {'$regex': 'tom', '$options': "i"}},
                       {"Actor": 1, 'Dob': 1, 'Summary': 1, '_id': 0, 'Subtitle': 1,
                                    "Url": 1, "Images": 1}):
    post.append(posts['Actor'])
    summary.append(posts['Summary'])
    subtitle.append(posts['Subtitle'])
    url_link.append(posts['Url'])
    dob.append(posts['Dob'])
    images.append(posts['Images'])

for d in range(len(post)):
    data_list.append(post[d])
    data_list.append(images[d])
    data_list.append(dob[d])
    data_list.append(subtitle[d])
    data_list.append(summary[d])
    data_list.append(url_link[d])

    main_list.append(data_list)
    data_list = []


pp(main_list)


for data in main_list:
    print(data[0])
    print(data[1])