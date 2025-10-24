import requests
import json
query=input("Enter type of news you want to search: ")
url = f"https://newsapi.org/v2/everything?q={query}&sortBy=popularity&apiKey=5583a8ee11f6418ea900a44481daec04"
         
       
      # &from=2025-09-01
       
r=requests.get(url)
#print(r.text)
news=json.loads(r.text) #converts the JSON string from the API response into a Python dictionary, so you can easily access articles and their details.
#print(news,type(news))
for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("--------------------------------------")
  