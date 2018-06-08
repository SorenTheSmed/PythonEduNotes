from urllib.request import urlopen
from bs4 import BeautifulSoup


data = urlopen("http://www.codemonkey.mobi").read()

soup = BeautifulSoup(data, "html.parser")

foundLinks = []

for link in soup.findAll("a"):
    foundLinks.append(link.get("href"))

print(foundLinks, "\n")