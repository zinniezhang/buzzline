import requests
import json
import matplotlib.pyplot as plt
from textblob import TextBlob

input = "tesla"

newsapi ="1757172a47034f13a34d5081871bc2b6"
url = "https://newsapi.org/v2/everything?q="+input+"&apiKey="+newsapi+""
newsObject  = requests.get(url).json()
totalArticles = newsObject["articles"]
publishingDate = []
sentimentAnalysis = []
for ar in totalArticles:
    publishingDate.append(ar["publishedAt"][0:10])
    articleSent = TextBlob(ar["content"])
    sentimentAnalysis.append(articleSent.sentiment.polarity)

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

# Your key here
key = 'H2TRXQR5HFYF1EVK'
# Chose your output format, or default to JSON (python dict)
ts = TimeSeries(key, output_format='pandas')
ti = TechIndicators(key)

def graphTicker(tickerSymbol):
    # Get the data, returns a tuple
    # aapl_data is a pandas dataframe, aapl_meta_data is a dict
    aapl_data, aapl_meta_data = ts.get_daily(symbol=tickerSymbol)
    # aapl_sma is a dict, aapl_meta_sma also a dict
    aapl_sma, aapl_meta_sma = ti.get_sma(symbol=tickerSymbol)

    # print(aapl_data)

    # Visualization
    figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
    print(aapl_data)
    aapl_data['4. close'].plot()
    plt.tight_layout()
    plt.grid()
    plt.savefig('stocks/' + tickerSymbol + '.png')
    plt.show()
    plt.scatter(publishingDate, sentimentAnalysis)
    plt.savefig('sentimentValue.png')
    return 'stocks/' + tickerSymbol + '.png'
    

