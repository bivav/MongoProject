from flask import Flask, render_template, request, flash, redirect
from pymongo import MongoClient
import datetime

app = Flask(__name__)

client = MongoClient()
db = client.search_engineDB
actor_data = db.actor_data
car_data = db.cars_data
artists_data = db.artist_data

history = db.history_data

admin_name = ""
admin_pass = ""
updateValue = ""


@app.route("/", methods=["GET", "POST"])
def main_page():
    global drop_down

    try:
        drop_down = ["Actor", "Artist", "Auto Mobile"]

        if request.method == "POST":

            # print(str(request.form.get('select_list')))
            if request.form.get("select_list") == "Actor":

                # first insert to history
                count = history.find({}).count()

                if request.form.get("keyword") is not "":
                    hist_data = {
                        "_id": count + 1,
                        "Search": request.form.get("keyword"),
                        "Category": request.form.get("select_list"),
                        "Date": datetime.datetime.now().strftime("%c")
                    }

                    history_check = history.insert_one(hist_data)
                    print(history_check.inserted_id)

                data_list = []
                main_list = []

                for posts in actor_data.find(
                        {'Actor': {'$regex': request.form['keyword'], '$options': "i"}},
                        {"Actor": 1, 'Dob': 1, 'Summary': 1, '_id': 0, 'Subtitle': 1,
                         "Url": 1, "Images": 1}):
                    data_list.append(posts['Actor'])
                    data_list.append(posts['Images'])
                    data_list.append(posts['Dob'])
                    data_list.append(posts['Subtitle'])
                    data_list.append(posts['Summary'])
                    data_list.append(posts['Url'])

                    main_list.append(data_list)
                    data_list = []

                return render_template("index.html", data_content=main_list, select_data=drop_down)

            elif request.form.get("select_list") == "Auto Mobile":

                # first insert to history
                count = history.find({}).count()

                if request.form.get("keyword") is not "":
                    hist_data = {
                        "_id": count + 1,
                        "Search": request.form.get("keyword"),
                        "Category": request.form.get("select_list"),
                        "Date": datetime.datetime.now().strftime("%c")
                    }

                    history_check = history.insert_one(hist_data)
                    print(history_check.inserted_id)

                data_list = []
                main_list = []

                for posts in car_data.find(
                        {'Car': {'$regex': request.form['keyword'], '$options': "i"}},
                        {"Car": 1, 'Summary': 1, '_id': 0, "Url": 1, "Images": 1}):
                    data_list.append(posts['Car'])
                    data_list.append(posts['Images'])
                    data_list.append(posts['Summary'])
                    data_list.append(posts['Url'])

                    main_list.append(data_list)
                    data_list = []

                return render_template("index.html", data_car=main_list, select_data=drop_down)

            elif request.form.get("select_list") == "Artist":

                # first insert to history
                count = history.find({}).count()

                if request.form.get("keyword") is not "":
                    hist_data = {
                        "_id": count + 1,
                        "Search": request.form.get("keyword"),
                        "Category": request.form.get("select_list"),
                        "Date": datetime.datetime.now().strftime("%c")
                    }

                    history_check = history.insert_one(hist_data)
                    print(history_check.inserted_id)

                data_list = []
                main_list = []

                for posts in artists_data.find(
                        {'Name': {'$regex': request.form['keyword'], '$options': "i"}},
                        {"Name": 1, 'Dob': 1, 'Summary': 1, '_id': 0, "Url": 1, "Image": 1}):
                    data_list.append(posts['Name'])     # 0
                    data_list.append(posts['Image'])    # 1
                    data_list.append(posts['Dob'])      # 2
                    data_list.append(posts['Summary'])  # 3
                    data_list.append(posts['Url'])      # 4

                    main_list.append(data_list)
                    data_list = []

                return render_template("index.html", data_artist=main_list, select_data=drop_down)

    except Exception as e:
        flash(e)

    return render_template("index.html", select_data=drop_down)


@app.route("/history/", methods=["GET", "POST"])
def history_page():
    if request.method == "POST":

        if request.form.get("id") is not None:
            delete = history.delete_one({"_id": int(request.form.get("id"))})
            print(request.form.get("id"))
            flash("Deleted " + str(delete.deleted_count) + " Records!")
        else:
            # print(request.form.get("id"))
            delete = history.remove({})
            flash("Deleted " + str(delete["n"]) + " Records!")

    hist_getData = history.find({})
    hist_data = []

    main_list = []
    for data in hist_getData:
        hist_data.append(data["_id"])
        hist_data.append(data["Search"])
        hist_data.append(data["Category"])
        hist_data.append(data["Date"])

        main_list.append(hist_data)
        hist_data = []

    return render_template("history.html", history_data=main_list)


@app.route("/admin/", methods=["GET", "POST"])
def admin_page():
    global updateValue
    drop_down = ["Actor", "Artist", "Auto Mobile"]

    if admin_name == "admin" and admin_pass == "admin123":

        if request.method == "POST":

            print(request.form.get("collName"))
            if str(request.form.get("collName")) == "Actor":
                update_data = actor_data.update_one({"_id": int(request.form.get("userID"))},
                                                    {"$set": {request.form.get("keyName"):
                                                                  request.form.get("updateValue")}})

                updateValue = "Updated " + str(update_data.modified_count) + " Record"
                print(update_data.modified_count)

            if request.form.get("collName") == "Artist":
                update_data = artists_data.update_one({"_id": int(request.form.get("userID"))},
                                                      {"$set": {request.form.get("keyName"):
                                                          request.form.get(
                                                              "updateValue")}})
                updateValue = "Updated " + str(update_data.modified_count) + " Record"

                print(update_data.modified_count)

            if request.form.get("collName") == "Auto Mobile":
                update_data = car_data.update_one({"_id": int(request.form.get("userID"))},
                                                  {"$set": {request.form.get("keyName"):
                                                                request.form.get("updateValue")}})
                updateValue = "Updated " + str(update_data.modified_count) + " Record"

                print(update_data.modified_count)

            if request.form.get("select_list") == "Actor":

                data_list = []
                main_list = []
                print(request.form['keyword'])

                filed_list = []

                for key in actor_data.aggregate([
                    {"$project": {"arrayofkeyvalue": {"$objectToArray": "$$ROOT"}}},
                    {"$project": {"keys": "$arrayofkeyvalue.k"}}
                ]):
                    filed_list.append(key["keys"][1])
                    filed_list.append(key["keys"][2])
                    filed_list.append(key["keys"][3])
                    filed_list.append(key["keys"][4])
                    filed_list.append(key["keys"][5])
                    filed_list.append(key["keys"][6])
                    print(filed_list)
                    break

                for posts in actor_data.find(
                        {'Actor': {'$regex': request.form['keyword'], '$options': "i"}},
                        {"Actor": 1, '_id': 1, }):
                    data_list.append(posts['_id'])
                    data_list.append(posts['Actor'])

                    main_list.append(data_list)
                    data_list = []

                return render_template("admin.html", username=main_list, select_data=drop_down,
                                       fields=filed_list, updated=updateValue)

            elif request.form.get("select_list") == "Auto Mobile":

                data_list = []
                main_list = []
                filed_list = []

                for key in car_data.aggregate([
                    {"$project": {"arrayofkeyvalue": {"$objectToArray": "$$ROOT"}}},
                    {"$project": {"keys": "$arrayofkeyvalue.k"}}
                ]):
                    filed_list.append(key["keys"][1])
                    filed_list.append(key["keys"][2])
                    filed_list.append(key["keys"][3])
                    filed_list.append(key["keys"][4])
                    print(filed_list)
                    break

                for posts in car_data.find(
                        {'Car': {'$regex': request.form['keyword'], '$options': "i"}},
                        {"Car": 1, '_id': 1}):
                    data_list.append(posts['_id'])
                    data_list.append(posts['Car'])

                    main_list.append(data_list)
                    data_list = []

                return render_template("admin.html", username=main_list, select_data=drop_down,
                                       fields=filed_list, updated=updateValue)

            elif request.form.get("select_list") == "Artist":

                data_list = []
                main_list = []
                filed_list = []

                for key in artists_data.aggregate([
                    {"$project": {"arrayofkeyvalue": {"$objectToArray": "$$ROOT"}}},
                    {"$project": {"keys": "$arrayofkeyvalue.k"}}
                ]):

                    filed_list.append(key["keys"][1])
                    filed_list.append(key["keys"][2])
                    filed_list.append(key["keys"][3])
                    filed_list.append(key["keys"][4])
                    filed_list.append(key["keys"][5])
                    print(filed_list)
                    break

                for posts in artists_data.find(
                        {'Name': {'$regex': request.form['keyword'], '$options': "i"}},
                        {"Name": 1, '_id': 1}):
                    data_list.append(posts['_id'])  # 1
                    data_list.append(posts['Name'])  # 0
                    main_list.append(data_list)
                    data_list = []

                return render_template("admin.html", username=main_list, select_data=drop_down,
                                       fields=filed_list, updated=updateValue)

        return render_template("admin.html", select_data=drop_down)

    return redirect("/signin/")
    # return "Clever"

@app.route("/signin/", methods=["GET", "POST"])
def signin_page():
    global admin_pass, admin_name

    if request.method == "POST":

        admin_name = request.form.get("userName")
        admin_pass = request.form.get("userPassword")

        if request.form.get("userName") == "admin" and \
                request.form.get("userPassword") == "admin123":

            return redirect("/admin/")
        else:
            return render_template("signin.html", data="Wrong Info!")

    return render_template("signin.html", data="")


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run()