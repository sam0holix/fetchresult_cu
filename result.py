import requests
from bs4 import BeautifulSoup

roll=input("Enter the roll number:  ")
with requests.Session() as c:
	url = 'http://wbresults.nic.in/curesult/cures_ba_bsc_p22_gen_hons_maj_18.asp'
	form_data = {
			'roll': roll, 
			'B1': 'Submit'
			}
        page=c.post(url, data=form_data, headers={"Referer": url})
	text=BeautifulSoup(page.text, 'html.parser').get_text()
	data=text[text.find('Roll'):-664]
	print(data)
