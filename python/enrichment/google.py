import os
import requests

GOOGLE_API_KEY = ""

def autocomplete_get(name):
    # Function to fetch get to url and return json
    url = "https://maps.googleapis.com/maps/api/place/autocomplete/json?"
    try:
        response = requests.get(
            url + 
            "input=" + name +
            "&key=" + GOOGLE_API_KEY +
            "&components=country:fr" +
            "&language=fr",
            headers={
                "Content-Type": "application/json",
            },
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise e
        
def geocoding(address):
    # Function to fetch get to url and return json
    url = "https://maps.googleapis.com/maps/api/geocode/json?"
    try:
        response = requests.get(
            url +
            "address=" + address +
            "&key=" + GOOGLE_API_KEY,
            headers={
                "Content-Type": "application/json",
            },
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise e
        
def details_get(place_id):
    # Function to fetch get to url and return json
    url = "https://maps.googleapis.com/maps/api/place/details/json?"
    try:
        response = requests.get(
            url +
            "place_id=" + place_id +
            "&key=" + GOOGLE_API_KEY,
            headers={
                "Content-Type": "application/json",
            },
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise e
        
