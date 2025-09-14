from bs4 import BeautifulSoup
import requests

## read the contents of the html file
with open('01_Web_Scraping_Introduction/sample.html') as f:
    html_doc = f.read()

## now create a soup object
soup = BeautifulSoup(html_doc,'html.parser')

## print the contents of the html doc
print(soup.prettify())

## get the title of the html document
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(type(soup.title.string))

## get the first element of its type
print(soup.div)

## get all the elements of its type
print(soup.find_all('div'))

## retrieve all links
for links in soup.find_all('a'):
    print(links.get('href'))
    print(links.get_text())

## get the elements using the CSS selectors like id or class
print(soup.find(id='italic'))
print(soup.find(class_='italic'))
print(soup.select('div.italic')) ## class selector
print(soup.select('span#italic')) ## id selector

## get the children in the DOM
for child in soup.find(class_='container').children:
    print(child)

## get the parent as well
for parent in soup.find(class_='box2').parents:
    print(parent) ## gives all the parents; nearest to the ultimate <html>

## modify existing tags
obj = soup.find(class_='container')
obj.name = 'span'

## add more elements and modify the element
ultag = soup.new_tag('ul')

litag = soup.new_tag('li')
litag.string = 'Element 1 Inserted'
ultag.append(litag)

litag = soup.new_tag('li')
litag.string = 'Element 2 Inserted'
ultag.append(litag)

soup.html.body.insert(0,ultag)
with open('01_Web_Scraping_Introduction/modified.html','w') as f:
    f.write(str(soup))
    print("Modified Content Saved..")

def has_class_but_no_id(tag):
    return tag.has_attr("class") and not tag.has_attr("id")

results = soup.find_all(has_class_but_no_id)
print(results)