from pyexpat import features
from bs4 import BeautifulSoup as bs
import lxml
features="xml"

content = []

with open("text.xml", "r") as file:
    content = file.readlines()
    content = "".join(content)
    bs_content = bs(content, "lxml")
    #print(bs_content.prettify())

results = bs_content.find(id = "bk102")
print(results.text)
results = bs_content.find(id = "bk103")
print(results.text)