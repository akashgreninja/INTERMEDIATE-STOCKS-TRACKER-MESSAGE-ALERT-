import requests
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

#for twilio
account_sid = "Your-sid"
auth_token = "Your-token

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
#for news api
API_KEY="Your key"
#for stocks api
API_KEY_STOCKS="your-key"

params_news={
    "q":COMPANY_NAME,
    "from":"2022-04-10",
    "to":"2022-04-11",
    "apiKey":API_KEY,
}

params_stocks={
    "function":"TIME_SERIES_DAILY",
    "symbol":f"{STOCK}",
    "apikey":API_KEY_STOCKS,



}

request_stock=requests.get(STOCK_ENDPOINT,params=params_stocks)
request_stock.raise_for_status()
data_stocks=request_stock.json()['Time Series (Daily)']
data_list=[ value  for  (key,value) in  data_stocks.items()]
Stock_price_yesterday=data_list[0]['4. close']
Stock_price_day_before=data_list[1]['4. close']
total_closing=float(Stock_price_yesterday)-float(Stock_price_day_before)
without_neg=total_closing
up_down=None
if without_neg>0:
    up_down="🔼"
else:
    up_down="🔽"





percentage=abs(round(without_neg/float(Stock_price_yesterday)*100))
print(f"{percentage}%")


if percentage>=5:
    request = requests.get(NEWS_ENDPOINT, params=params_news)
    print(request.raise_for_status())
    data = request.json()


    articles = data['articles'][:3]
    # print(articles)
    list_1=[f"{STOCK}:{up_down}{percentage}\nHeadline:{article['title']}.\nBrief:{article['description']}"for article in articles]
    print(list_1)
    client = Client(account_sid, auth_token)
    for i in list_1:
        message = client.messages \
            .create(
            body=i,
            from_='The number twilio gives you',
            to='Your number'
        )

        print(message.sid)

# for i in range(3):
#     title = data['articles'][:3][i]['title']
#     description = data['articles'][:3][i]['description']
#     print(f"{title} \n {description}")











