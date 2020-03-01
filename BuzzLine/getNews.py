import requests
import json
from textblob import TextBlob

input = "tesla"

newsapi ="22d21f2234d74ec7b27482cbe70fcde8"
url = "https://newsapi.org/v2/everything?q="+input+"&apiKey="+newsapi+""
newsObject  = requests.get(url).json()
totalArticles = newsObject["articles"]
sentimentAnalysis = []
for ar in totalArticles:
    articleSent = TextBlob(ar["content"])
    sentimentAnalysis.append(articleSent.sentiment)



