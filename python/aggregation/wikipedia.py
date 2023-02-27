import requests

def get_page(name):
    url = "https://fr.wikipedia.org/w/api.php?"
    try:
        response = requests.get(
            url,
            params={
                "action": "query",
                "list": "search",
                "srsearch": name,
                "format": "json",
            },
            headers={
                "Content-Type": "application/json",
            }
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(error)

def get_page_content(pageid):
    url = "https://fr.wikipedia.org/w/api.php?"
    try:
        response =  requests.get(
            url,
            params={
                "action": "parse",
                "pageid": pageid,
                "format": "json",
            },
            headers={
                "Content-Type": "application/json",
            }
        )
        response.raise_for_status()
        return  response.json()
    except requests.exceptions.RequestException as error:
        print(error)

from bs4 import BeautifulSoup

def get_information(name):
    try:
        result =  get_page(name)
        content =  get_page_content(result['query']['search'][0]['pageid'])
        html = content['parse']['text']['*']
        dom =  BeautifulSoup(html, "html.parser")
        th = dom.find_all('th')
        information = {}
        for i in range(len(th)):
            if th[i].text == "Siège":
                information["address"] = th[i].find_next_sibling('td').text.replace('\n', '').strip()
            if th[i].text == "SIREN":
                information["siren"] = th[i].find_next_sibling('td').text.replace('\n', '').strip()
            if th[i].text == "Site web" or th[i].text == "Sites web":
                link = th[i].find_next_sibling('td').find('a')
                if link:
                    information["website"] = link.get('href')
        return information
    except Exception as error:
        print(error)
    return None
