import requests
import json

from config import geoapify_key
import requests

url = "https://airbnb19.p.rapidapi.com/api/v1/searchDestination"

querystring = {"query":"Perth","country":"Australia"}

headers = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": "dd7dd3843amsh6b942ff8ea44f5cp1ce0d5jsna104260fd951",
	"X-RapidAPI-Host": "airbnb19.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

response.json()
import requests

url = "https://airbnb19.p.rapidapi.com/api/v1/getCategory"

headers = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": "dd7dd3843amsh6b942ff8ea44f5cp1ce0d5jsna104260fd951",
	"X-RapidAPI-Host": "airbnb19.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

response.json()
import requests

url = "https://airbnb19.p.rapidapi.com/api/v1/searchProperty"

querystring = {"category":"TAB_8225","totalRecords":"10","currency":"Aus","adults":"1","pets":"1", 
               "query":"Perth","country":"Australia"}

#querystring = {"query":"Perth","country":"Australia"}
headers = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": "dd7dd3843amsh6b942ff8ea44f5cp1ce0d5jsna104260fd951",
	"X-RapidAPI-Host": "airbnb19.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
response.json()

import requests
import json
import csv

urlcomp = "https://airbnb19.p.rapidapi.com/api/v1/getCategory"
headers = {'accept': "application/json", 'accept': "text/csv"}
headers = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": "dd7dd3843amsh6b942ff8ea44f5cp1ce0d5jsna104260fd951",
	"X-RapidAPI-Host": "airbnb19.p.rapidapi.com"}
## API Call to retrieve report
rcomp = requests.get(urlcomp, headers=headers)

'''
# Write to .CSV
f = open('C:\_Python\one\\newfile.csv', "w")
f.write(rcomp.text)
f.close()
'''
data = rcomp.text
csvFile = open('C:\_Python\\CompletionReportOutput.csv', 'w')

writer = csv.writer(csvFile, delimiter = "")

for row in data.split('\n'):
    writer.writerow(row)