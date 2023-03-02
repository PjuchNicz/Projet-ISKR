import os
import requests

INSEE_API_KEY = ""

def information_siret(siret):
    # Get information about a siret
    url = "https://api.insee.fr/entreprises/sirene/V3/siret/"
    try:
        response = requests.get(
            url + siret,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {INSEE_API_KEY}",
            },
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise Exception(f"information_siret : {e}") from e


def format_query_text(string):
    return string.capitalize()


def convert_etablissement_address(adresse_etablissement_obj):
    # Set the "codeCommuneEtablissement" field to None
    adresse_etablissement_obj["codeCommuneEtablissement"] = None

    # Remove any None values and join the remaining fields with a space
    adresse_etablissement_list  = list(filter(lambda i: i is not None, adresse_etablissement_obj.values()))
    adresse_etablissement  = " ".join(adresse_etablissement_list)
    # Format the text by lowercasing and removing leading/trailing whitespaces

    adresse_etablissement  = " ".join(map(format_query_text, adresse_etablissement.split()))
    return adresse_etablissement 


def confirm_siren_siret(siret, siren):
    return siren == siret[:9]
