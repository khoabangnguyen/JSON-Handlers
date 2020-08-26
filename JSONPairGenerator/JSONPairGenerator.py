from stringLists import jobs as strlist
import json


# Program to systematically generate JSON files from lists of strings


# Function to generate keys from strings
def key_generator(str_list):
    keys = []
    keys_file = open("keys.txt", 'w')
    keys_file.write('[\n')
    for item in str_list:
        key = item.replace(" ", "_").lower()
        key = key.replace("’", "")
        key = key.replace("'", "")
        key = key.replace(",", "")
        keys.append(key)
        keys_file.write("'" + key + "'" + ',\n')
    keys_file.write(']\n')
    keys_file.close()
    return keys


# Combine keys and strings into a dict
new_dict = dict(zip(key_generator(strlist), strlist))


# Dump dict into JSON file
with open("new_json.txt", "w") as json_file:
    json.dump(new_dict, json_file)

