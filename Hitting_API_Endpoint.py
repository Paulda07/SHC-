# import requests
# import json


# base_url = 'https://qa.zeamed.com/#/consumer/searchResults/003%20-%20ECMO%20OR%20TRACH%20W%20MV%20%3E96%20HRS%20OR%20PDX%20EXC%20FACE,%20MOUTH%20&%20NECK%20W%20MAJ%20O.R./5cad7cc26c5a8a109445b2fc/Orlando,%20FL,%20USA/28.5383355/-81.37923649999999/FL'



# PARAMS = {"lat":28.5383355,"long":-81.37923649999999,"master_id":"5cad7cc26c5a8a109445b2fc","radius":250,"name":"003 - ECMO OR TRACH W MV >96 HRS OR PDX EXC FACE, MOUTH & NECK W MAJ O.R.","state":"FL"} 
  

# r = requests.get(url = base_url)


# print(r.url)

import requests
import json


base_url = 'https://api.zeamed.com:1002/BackEnd/geocheck'
data_headers = {'Content-type': 'application/json'}


DATA = {"lat":34.79981,"long":-87.67725100000001,"master_id":"5cb08bcb3c774842c6f20aa6","radius":250,"name":"OFFICE VISIT NEW","state":"AL"}
  

r = requests.post(url = base_url, json = DATA)


print(r.text)

