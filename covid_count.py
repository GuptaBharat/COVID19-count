

import requests 
from bs4 import BeautifulSoup 
from tabulate import tabulate 

content = lambda row: [x.text.replace('\n', '') for x in row] 
URL = 'https://www.mohfw.gov.in/'

SHORT_HEADERS = ['SNo','State','Confirmed','Cured','Death'] 

soup = BeautifulSoup(requests.get(URL).content, 'html.parser') 
header = content(soup.tr.find_all('th')) 

stats = [] 

for row in soup.find_all('tr'): 
	stat = content(row.find_all('td')) 
	if stat: 
		if len(stat) == 5: 
			stat = ['', *stat] 
			stats.append(stat) 
		elif len(stat) == 4: 
			stats.append(stat) 

stats[-1].insert(0,' ')
stats[-1].insert(1,' ')

table = tabulate(stats, headers=SHORT_HEADERS) 
print(table)
