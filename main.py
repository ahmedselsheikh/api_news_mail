import requests

api_key = 'd21f796453d245a7b3734cb47603dc2f'
url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-04-27&' \
      'sortBy=publishedAt&apiKey=' \
      'd21f796453d245a7b3734cb47603dc2f'
request = requests.get(url)

# Get the dictionary with data
content = request.json()

# Access the article titles and descriptions
for index, article in enumerate(content['articles']):
    print(f'article number {index+1} : {article["title"]}')
    print(f'article description {index + 1} : {article["description"]}')
