import sys
import os
import json
import vk
import pathlib

session = vk.Session(access_token='41547da141547da141547da168410a14134415441547da118ea3a43f6cc46a2ea378d09')
vk_api = vk.API(session, v='5.68') 

mas = vk_api.wall.get(owner_id='-101826369', count=30)

#print(mas)
#print(type(mas))

'''
get an item by key'''
def get_vk_item(json_data, key):
    text_array =[]
    for i, item in enumerate(json_data['items']):
        item_text = item[key]
        text_array.append(item_text)
    return text_array
'''
applying qet_vk_item()'''
info_array = get_vk_item(mas, 'text')
key_words = ['хакатон']
clean_info_array = []
for info in info_array:
    for key_word in key_words:
        if key_word in info:
            clean_info_array.append(info)

print(clean_info_array)

resultFyle = open("vk_data.csv",'wb')

# Write data to file
for r in clean_info_array:
    resultFyle.write(r.encode())
resultFyle.close()

'''
saving data as json file
just for checking structure'''
#with open("output.json", "w", encoding="utf-8") as file:
    #json.dump(mas, file)