from pprint import pprint as pp
import requests
from bs4 import BeautifulSoup
import wikipedia
from pymongo import MongoClient

client = MongoClient()
db = client.get_database("search_engineDB")
posts = db.get_collection("cars_data")

url = "https://www.irishtimes.com/life-and-style/motors/top-100"
req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")

car_list = []
car_name = soup.find("div", {"class": "bt-container"}).findAll("span", {"class": "h2"})

for name in car_name:
    name = name.get_text()

    name = name[3:name.find("–")].strip()
    car_list.append(name)

i = 0
count = [0, 4, 54, 98, 99]
new_car_list = []
for item in car_list:
    new = car_list[count[i]]
    if item == new:
        if new[new.find(",")] == ",":
            item = new[new.find("P"):new.find(",")]

        if new[new.rfind(":")] == ":" and new[new.find("B")] == "B":
            item = new[:new.find(":")]

        if new[new.find("-")] == "-":
            item = new[:new.find("-")]

        if new[new.find(":")] == ":":
            item = new[2:]

        i = i + 1

    if item == "Lexus IS300h":
        item = item.replace("Lexus IS300h", "Lexus IS")

    new_car_list.append(item.strip())

# pp(new_car_list)


subtitle_list = []
image_list = []

car_images = soup.find("div", {"class": "bt-container"})\
    .findAll("img", {"data-mobile": "box_300_160"})

# [print(car['src']) for car in car_images]

for car in car_images:
    car = "https://www.irishtimes.com" + str(car['src'])
    image_list.append(car)

car_count = 1
for cars in new_car_list:
    wikipage = wikipedia.page(cars)

    # a dictionary format for 1 car
    post = {
        "_id": car_count,
        "Car": wikipage.title,
        "Url": wikipage.url,
        "Summary": wikipage.summary,
        "Images": image_list[car_count - 1]
    }

    # insert one to mongodb
    post = posts.insert_one(post)
    car_count += 1

    # get the id if successful
    print(post.inserted_id)
