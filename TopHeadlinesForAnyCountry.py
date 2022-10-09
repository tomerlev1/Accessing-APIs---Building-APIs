import requests

def get_news(country, api_key='6814ca99c0f145839e4258cd8b01a989'):
  url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
  
  r = requests.get(url)

  content = r.json()
  articles = content['articles']
  results = []
  for article in articles:
    results.append(f"TITLE: {article['title']} || DESCRIPTION: {article['description']}")

  return results

my_news = get_news(country='us')
print(my_news)