#basic requirements
from ctypes.wintypes import tagMSG
import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = "https://www.screener.in/screens/184382/large-cap/"

#Step 1: Get the HTML
r = requests.get(url, verify = False)
htmlContent = r.content
# print(htmlContent)

#Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())

#Step 3: HTML Tree Traversal
# Commonly used types of objects:
# 1. Tag
# 2. NavigableString 
# 3. BeautifulSoup
# 4. Comment
#get all paras similarly other tags
p = soup.find_all('a')
print(p[0])

# print(soup.find('p')) #get first element
#get class of any element in html page
# print(soup.find('p')['class']), similarly other functionalities