import csv
import os
import fnmatch
import json
import logging
def generate_rncp_base():
    filename = seach_file_name("ROME")
    rncp_document = {}
    with open(f'csv/{filename}', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            rncp_document[row["Numero_Fiche"]] = {}
    return rncp_document


def seach_file_name(name):
    # search file name in csv folder
    for file in os.listdir("csv"):
        if fnmatch.fnmatch(file, f'*{name}*.csv'):
            return file
    print("No file found")

#####
# These functions will be used for POC purpose
# They will be removed in the future
#####

def generate_rncp_rome():
    try:
        rome_filename = seach_file_name("ROME")
        rncp_document = generate_rncp_base()

        # add rome list to rncp document
        for rncp in rncp_document:
            rncp_document[rncp]["ROME"] = []
        
        with open(f'csv/{rome_filename}', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                rncp_document[row["Numero_Fiche"]]["ROME"].append(row["Codes_Rome_Code"])
        return rncp_document
    except Exception as e:
        raise Exception(f"generate_rncp_rome : {e}") from e


def save_dict_json(dict, filename):
    try:
        os.makedirs('./json', exist_ok=True)

        with open(f'./json/{filename}.json', 'w') as json_file:
            json.dump(dict, json_file)

    except Exception as e:
        raise Exception(f"save_dict_json : {e}") from e