from bs4 import BeautifulSoup
import requests

response = requests.get('https://appbrewery.github.io/news.ycombinator.com/')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.find_all(name='a', class_='storylink')
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvote = [ int(score.getText().split()[0]) for score in soup.find_all(name="span", class_='score')]
# print(article_texts)
# print(article_links)
# print(article_upvote)

largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)
print(article_links[largest_index])
print(article_texts[largest_index])