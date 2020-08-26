import csv
import json
import os


# Convert flattened CSV Files back into nested JSON files
# NOTE: CSV file format: First column: key, Second Column: value

# For one CSV file at a time
# reader = csv.reader(open('C:/Users/user/PycharmProjects/nested_json_generator/csv_sg/dashboard.csv', encoding="utf8"))
# json_dict = {}
# for row in reader:
#     current_dict = json_dict
#     key = row[0]
#     value = row[1]
#     key_list = key.split(".")
#     while len(key_list) > 1:
#         if not (key_list[0] in current_dict):
#             current_dict[key_list[0]] = {}
#         current_dict = current_dict[key_list[0]]
#         key_list.pop(0)
#     current_dict[key_list[0]] = value
#
# json_object = json.dumps(json_dict, indent=4)
# json_path = 'C:/Users/user/PycharmProjects/nested_json_generator/json_sg/dashboard.json'
# with open(json_path, "w") as outfile:
#     outfile.write(json_object)

# For all CSV Files in a folder
directory = "C:/Users/user/PycharmProjects/nested_json_generator/csv_sg/"
json_dir = "C:/Users/user/PycharmProjects/nested_json_generator/json_sg/"

for filename in os.listdir(directory):
    reader = csv.reader(open(directory+filename, encoding="utf8"))
    json_dict = {}
    for row in reader:
        current_dict = json_dict
        key = row[0]
        value = row[1]
        key_list = key.split(".")
        while len(key_list) > 1:
            if not (key_list[0] in current_dict):
                current_dict[key_list[0]] = {}
            current_dict = current_dict[key_list[0]]
            key_list.pop(0)
        current_dict[key_list[0]] = value
    json_object = json.dumps(json_dict, indent=4)
    json_file = filename[:-4] + ".json"
    json_path = json_dir + json_file
    with open(json_path, "w") as outfile:
        outfile.write(json_object)

