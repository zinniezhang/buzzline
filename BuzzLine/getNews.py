import requests
import json

input = "tesla"

newsapi ="22d21f2234d74ec7b27482cbe70fcde8"
url = "https://newsapi.org/v2/everything?q="+input+"&apiKey="+newsapi+""
newsObject  = requests.get(url).json()
totalArticles = newsObject["articles"]

