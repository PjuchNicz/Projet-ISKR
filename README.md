# Kryptie

## Description

Contribution of ISEN students to the Kryptie project.
It aims to extract the latest data from France compétence and structure it in a more organized manner. 
Also to automatically enrich data for a certificator, using a SIRET number, and to execute this on a monthly basis. 
Additionally, the project aims to create a matching engine between job offers and the needs of companies with the skills of students.

### History of our project
First, we had to work with a no-code platform for the application, and the previous developers had used firebase as an authentication system and storage.
So we had to figure out how to made our code the most efficient possible with this platform.
We chose to stay in the firebase ecosystem.
So we chose to use google cloud function to execute the code monthly, google storage as a data lake to store downloaded data in raw format and archive them, and finally firestore as a no sql database to store structured data. So the first version of our code is in javascript and connected to the firebase ecosystem.

But the project change, and we had to work without a precise stack, code, or platform... So we decided to use python because it's a language we know well, easier to debug and to test matching algorithms with library like tensorflow or implement it ourselves.

We think it's better for you to look at the python code because it's more recent and more efficient, and documented. But if in the future we need to change this code to work with other language, it's possible to do it.

## Python code

### Installations and usage

#### For linux

'''bash
cd ./python
python3 -m venv .venv 
source .venv/bin/activate 
pip install -r requirements.txt
python main.py
'''

#### For Windows

'''bash
cd ./python
python -m venv .venv 
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
'''