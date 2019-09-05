#bare-bones tracking app that informs you of your package delivery.
#through USPS.

from bs4 import BeautifulSoup
import requests
#import time

#traking_id = '' //through USPS
traking_id = input('Please provide your tracking id: ')
url = 'https://tools.usps.com/go/TrackConfirmAction?tLabels='

'''tests different "redirect" links
test_url = f'{url}{traking_id}'
redirected_links = set()
while True:
    r = requests.get(test_url, allow_redirects=False)
    
    if test_url in redirected_links: 
        print(r.status_code)
        break
    
    redirected_links.add(test_url)
    print(test_url)
'''

#create session to pass "header" info.
s = requests.Session()
s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
r = s.get(f'{url}{traking_id}')
#print(r.status_code)

soup_obj = BeautifulSoup(r.text, 'html.parser')
#print(soup_obj.prettify())

'''grabs whole "div" class that we are interested in.
delivery_status = soup_obj.find('div', class_='delivery_status')
print(delivery_status)
'''

#grabs specific item we need.
delivery_status = soup_obj.find('p', class_='important').text

#check if deliverd
if delivery_status.lower().find('delivered') != -1:
    print('your item has been ' + delivery_status.lower())
else:
    print('your package is not delivered...')
