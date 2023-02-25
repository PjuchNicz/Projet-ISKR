import requests
import logging
from dotenv import load_dotenv
import os
load_dotenv()


### Check dotenv problem
#url = f'{os.getenv("API_URL_DATAGOUV")}/{os.getenv("ENDPOINT_FRANCE_COMP_DATASET")}/{os.getenv("SLUG_FRANCE_COMP_DATASET")}'

API_URL_DATAGOUV = "https://www.data.gouv.fr/api/1"
SLUG_FRANCE_COMP_DATASET =  "repertoire-national-des-certifications-professionnelles-et-repertoire-specifique"
ENDPOINT_FRANCE_COMP_DATASET = "datasets"
BUCKET_NAME = "france-competence-test.appspot.com"

url = f'{API_URL_DATAGOUV}/{ENDPOINT_FRANCE_COMP_DATASET}/{SLUG_FRANCE_COMP_DATASET}'

def get_dataset_list(url):
    response = requests.get(url, headers={"Content-Type": "application/json"})
    response.raise_for_status()
    return response.json()

def extract_lastest_url(resources):
    # Return the url of the latest csv file
    last_url = max(filter(lambda item: "export-fiches-csv-" in item['title'], resources), key=lambda x: x['title'])['url']
    if last_url is None:
        raise Exception("No last url found")
    return last_url

def get_last_url():
    # Return the url of the latest csv file
    try:
        return extract_lastest_url(get_dataset_list(url)["resources"])
    except Exception as e:
        raise Exception(f"get_last_url: {e}") from e
