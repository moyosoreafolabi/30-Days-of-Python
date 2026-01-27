# Web scraping is the process of extracting and collecting data from websites and storing it on a local machine or in a database.
import requests
from bs4 import BeautifulSoup
url = 'https://www.w3schools.com/python/python_lists.asp'

response = requests.get(url)
# lets check the status
status = response.status_code
print(status)

import requests
from bs4 import BeautifulSoup
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # gives the whole page on the website
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
 # the result is a list, we are taking out data from it
for td in table.find('tr').find_all('td'):
    print(td.text)