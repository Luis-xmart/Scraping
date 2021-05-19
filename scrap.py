from bs4 import BeautifulSoup
import requests
import pandas as pd 

url='https://experience.arcgis.com/experience/dde44bc14618478c888cadda320ccee4'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

#Numero
N = soup.find_all('span', class_='esriNumericValue')
#N = soup.find_all('ember237', class_='feature-description ember_view')
print(N)