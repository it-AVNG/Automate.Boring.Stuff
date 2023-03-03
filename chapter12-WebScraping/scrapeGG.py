import requests #launching browser to specific URL
from bs4 import BeautifulSoup 
import csv
from pathlib import Path

p = Path('content.html')


URL = 'https://help.optitex.com/#t=Optitex_2D%2FIntro_to_PDS%2FInterface%2FGetting_to_Know_the_PDS_User_Interface.htm'
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
p.write_text(soup.prettify())
quotes=[]

table=soup.find('div', attrs={'id':'all_quotes'})