#bare-bones tracking app that informs you of your package delivery.
#through USPS.

from bs4 import BeautifulSoup
from send_email import send_email
import requests
import time

#9341989697090119754616, 9361289697090784589402
#traking_id = '123' #through USPS 
traking_id = input('Please provide your tracking id: ')
url = 'https://tools.usps.com/go/TrackConfirmAction?tLabels='

def scrape():
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
    return soup_obj.find('p', class_='important').text

def is_delivered():
    delivery_status = scrape()

    if delivery_status.lower().find('delivered') != -1:
        msg = 'Your package has been ' + delivery_status.lower()
        print(msg)
        send_email(msg)
        return True
    else:
         print('Your package is not delivered...')
         return False

#check every minute if "delivered"
while not is_delivered():
    time.sleep(60)