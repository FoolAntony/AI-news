import requests
from send_email import send_email
from simple_ai import model
from env import NEWS_API_KEY
import time

TOPIC = "business"

url = "https://newsapi.org/v2/everything?" \
      f"q={TOPIC}" \
      f"&from=({time.strftime("%Y-%B-%D")})" \
      "&sortBy=publishedAt" \
      f"&apiKey={NEWS_API_KEY}" \
      "&pageSize=8" \
      "&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with page content
content = request.json()
articles = content["articles"]
print(articles)

# AI summarizing with data
prompt = f"""
You're a news summarizer. Write a short paragraph analyzing those news
Write a second paragraph telling me how they affect the stock market.
Here are the news articles:
{articles}
"""

response = model.invoke(prompt)
response_str = response.content[0]['text']

body = "Subject: News Summary\n\n" + response_str + "\n\n"

body = body.encode("utf-8")
send_email(message=body)