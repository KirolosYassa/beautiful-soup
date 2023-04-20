import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

counter = 0
news = {}
all_votes = soup.select("span > .score")
print(all_votes)
for item in all_votes:
    score_string = item.get_text()
    score = score_string.split(" ")[0]
    # score = int(score_string)
    news[counter] = {"score": score}
    counter += 1
    
    
skipped = 0
counter = 0
all_links = soup.select("span.titleline > a")
print(len(all_links))

semi_counter = 0
for item in all_links:
    link = item.get("href")
    name = item.get_text()
    print(link, name)
    semi_counter += 1
    print(f"counter = {counter}")
    print(f"semi_counter = {semi_counter}")
    news[counter]["name"] = name
    news[counter]["link"] = link
    counter += 1

    
print(news)
print(f"semi_counter = {semi_counter}")
print(f"counter = {counter}")
print(f"skipped = {skipped}")

