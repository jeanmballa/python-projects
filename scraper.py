import requests
import csv
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

rows = []
for q in soup.find_all("div", class_="quote"):
    text = q.find("span", class_="text").text
    author = q.find("small", class_="author").text
    rows.append([text, author])

with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Quote", "Author"])
    writer.writerows(rows)

print("Saved", len(rows), "quotes to quotes.csv")
