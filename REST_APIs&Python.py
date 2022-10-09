# API 6814ca99c0f145839e4258cd8b01a989
import requests 

# r = requests.get('https://newsapi.org/v2/everything?qInTitle=united%states&from=2022-9-01&to=2022-9-04&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c') #Get API
# content = r.json() #Get the json content 
# articles = content['articles'] #choose from the json only the articles keys

def get_news(topic, from_date, to_date, language='en', api_key='6814ca99c0f145839e4258cd8b01a989'):
  url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
  
  r = requests.get(url)

  content = r.json()
  articles = content['articles']
  results = []
  for article in articles:
    results.append(f"TITLE: {article['title']} || DESCRIPTION: {article['description']}")

  return results

my_news = get_news('Israel', '2022-8-28', '2022-9-04')
print(my_news)