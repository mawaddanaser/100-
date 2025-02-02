from bs4 import BeautifulSoup

with open('doc.html') as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')
#print(soup.prettify())
#print(soup.title.string)

#print(soup.title.parent.name)
#print(soup.p['class'])
#print(soup.a)
print(soup.find_all('a'))