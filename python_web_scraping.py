
import requests
from bs4 import BeautifulSoup
url=""
r=requests.get(url)
soup=BeautifulSoup(r.content)
# to get all the a tags from the html page
links = soup.find_all("a")  
for link in links:
	if "http" in link.get("href"):
		print "<a href='%s'>%s</a>"%(link.get("href"),link.text) 
#to identify any particular class or id from the html page
g_data = soup.find_all("div",{"class":""}) 
for item in g_data:
	print item.contents[0].text