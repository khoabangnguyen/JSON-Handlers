import json
import csv
import os

# Program to convert nested JSON files into flat CSV files

# Helper function to help flatten nested JSON values


def flatten_json(nested_json):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '.')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '.')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(nested_json)
    return out


# Function to convert all JSON files in a directory into a single CSV file
def convert_dir(directory, file_name):
    csv_writer = csv.writer(open(file_name, "w", newline=''))
    for file_name in os.listdir(directory):
        csv_writer.writerow([file_name])
        print(file_name)
        file_path = directory + file_name
        json_in = open(file_path, encoding="utf8")
        json_data = json.load(json_in)
        flat_json = flatten_json(json_data)

        for key, value in flat_json.items():
            key_list = [" ",key]
            val_list = [value]
            key_list.extend(val_list)
            print(key_list)
            csv_writer.writerow(key_list)


# Function to convert a single file in a directory
def convert_file(file_path, file_name):
    csv_writer = csv.writer(open('C:/Users/user/PycharmProjects/jsonConverter/csv_en/' + file_name + ".csv", "w",
                                 newline=''))
    json_in = open(file_path, encoding="utf8")
    json_data = json.load(json_in)
    flat_json = flatten_json(json_data)

    for key, value in flat_json.items():
        key_list = [key]
        val_list = [value]
        key_list.extend(val_list)
        # print(value) # only for converting Tamil json back
        csv_writer.writerow(key_list)


# Function to convert all JSON files in directory to separate CSV Files
def convert_dir_separate(directory):
    for file_name in os.listdir(directory):
        print(file_name)
        file_path = directory + file_name
        csv_name = file_name[:-5]
        convert_file(file_path, csv_name)


# Niche function to print out translated values with special characters
def get_special_text(file_path):
    json_in = open(file_path, encoding="utf-8")
    json_data = json.load(json_in)
    flat_json = flatten_json(json_data)

    for key, value in flat_json.items():
        print(value)

# Use functions
# current_path = 'C:/Users/user/PycharmProjects/jsonConverter/en/'
# convert_dir_separate(current_path)
# get_special_text('C:/Users/user/PycharmProjects/jsonConverter/tm/cms_index.json')


convert_dir('C:/Users/user/PycharmProjects/jsonConverter/cms_en/', 'landingCMS.csv')
# convert_file('C:/Users/user/PycharmProjects/jsonConverter/en/occupations.json', 'occupations')

