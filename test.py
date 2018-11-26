# # import re
#
# name_check = re.compile(r"[^A-Za-zs.]")
#
# name = input ("Please, enter your name: ")
# re.compile('(//www.ranker.com/review/)+([a-zA-Zs-])+(/)+([0-9])+(
# .*ref=node_name&pos=.*&a=0&ltype=n&l=538997&g=2)')
#
# # //www.ranker.com/review/attack-on-titan/73655135?ref=node_name&pos=2&a=0&ltype=n&l=538997&g=2

# import wikipedia

# print(wikipedia.page("Porsche Boxster & Cayman").summary)

# count = 0
#
# while(count != 10):
#     print("a")
#     count = count +1


from google_images_download import google_images_download  # importing the library

response = google_images_download.googleimagesdownload()  # class instantiation

arguments = {"keywords": "Drake (musician)", "limit": 1,
             "print_urls": True}  # creating list of arguments
paths = response.download(arguments)  # passing the arguments to the function

print(paths["Drake (musician)"][0])
