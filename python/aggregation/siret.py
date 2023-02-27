import os
import google
import insee
import wikipedia


def main():
    #RNCP29276
    siret = "78370700300035" #78370700300035
    result = insee.information_siret(siret)

    adresseEtablissement = insee.convert_etablissement_address(result['etablissement']['adresseEtablissement'])
    name = insee.format_query_text(result['etablissement']['uniteLegale']['denominationUniteLegale'])

    resultGeocoding = google.geocoding(adresseEtablissement)
    location = resultGeocoding['results'][0]['geometry']['location']

    autoCompleteResult = google.autocomplete_get(name)

    if autoCompleteResult['predictions']:
        place_id = autoCompleteResult['predictions'][0]['place_id']
        result3 = google.details_get(place_id)  # pas le bon id ?
        print(result3['result']['international_phone_number'])
        print(result3['result']['website'])

    wiki_link = wikipedia.get_information(name)
    if wiki_link:
        print(wiki_link)
        print(insee.confirm_siren_siret(siret, wiki_link['siren']))


main()
