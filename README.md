# Kryptie

## Description

Contribution of ISEN students to the Kryptie project.
It aims to extract the latest data from France compétence and structure it in a more organized manner. 
Also to automatically enrich data for a certificator, using a SIRET number, and to execute this on a monthly basis. 
Additionally, the project aims to create a matching engine between job offers and the needs of companies with the skills of students.

## History of our project

First, we had to work with a no-code platform for the application, and the previous developers had used firebase as an authentication system and storage.
So we had to figure out how to made our code the most efficient possible with this platform.
We chose to stay in the firebase ecosystem.
So we chose to use google cloud function to execute the code monthly, google storage as a data lake to store downloaded data in raw format and archive them, and finally firestore as a no sql database to store structured data. So the first version of our code is in javascript and connected to the firebase ecosystem.

But the project change, and we had to work without a precise stack, code, or platform... So we decided to use python because it's a language we know well, easier to debug and to test matching algorithms with library like tensorflow or implement it ourselves.

We think it's better for you to look at the python code because it's more recent and more efficient, and documented. But if in the future we need to change this code to work with other language, it's possible to do it.

# Python code

## Installations and usage

### For linux

```bash
cd ./python
python3 -m venv .venv 
source .venv/bin/activate 
pip install -r requirements.txt
python main.py
```

### For Windows

```bash
cd ./python
python -m venv .venv 
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Architecture

We choose to not using the "usual" architecture of python programming, because we wanted to make the code as simple as possible, and to make it easy to understand for everyone. So we choose to use a single file for the main code, and files for a specific feature for better readability.

There is 2 main part in this code, the first one is the data extraction, and the second one is the data enrichment.

For now, the two parts are separated, but we will merge them in the future.

### Extraction

* datagrouv

    1. Get the url of the lastest zip file containing the data from France compétence

* file

    1. Download the zip file in zip folder
    2. Unzip the file
    3. Extract the csv file in csv folder

* processing

    1. Generate a rncp code dictionnary containing rome code list.
    2. Save it in the json

Because we don't know for now the finality of the data, we use for now this code to transform csv for us, but it will change based on the future of the application.

### Enrichment

If you want to use this code, you need a google maps api key and a insee siren bearer token.

In order to get information (adress, website, phone number) from a company. We use multiple sources of information.

We start from a Siret number.
We use the API sirene of the insee to get the adress of the company and it's registered name.
From this, we search the google business card of the company, and we get the website and the phone number registered on google business.
The problem, is a lot of gouvernemental structure don't have a google business card, so we use a scraping method from wikipedia, because wikipedia have a lot of information about theses structures.


## Our next steps

- [ ] Refactor the code for clean code and better architecture
- [ ] Add tests
- [ ] Better error handling
- [ ] Include matching engine in the project
