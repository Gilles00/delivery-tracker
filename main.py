#bare-bones tracking app that informs you of your package delivery.
#through USPS.

from bs4 import BeautifulSoup
from send_email import send_email
import requests, time, webbrowser

traking_id = input('Please provide your tracking id: ')
url = 'https://tools.usps.com/go/TrackConfirmAction?tLabels='

def scrape():
    #create session to pass "header" info.
    session = requests.Session()
    session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    response = session.get(f'{url}{traking_id}')
    #print(response.status_code)

    soup_obj = BeautifulSoup(response.text, 'html.parser')
    #print(soup_obj.prettify())

    '''grabs whole "div" class that we are interested in.
    delivery_status = soup_obj.find('div', class_='delivery_status')
    print(delivery_status)
    '''

    #grabs specific item we need.
    return soup_obj.find('p', class_='important').text

def is_delivered(counter=''):
    delivery_status = scrape()

    if delivery_status.lower().find('delivered') != -1:
        msg = 'Your package has been ' + delivery_status.lower()
        print(msg)
        #send_email(msg)

        #open webbroswer showing the "proof" of delivery
        webbrowser.open_new(f'{url}{traking_id}')
        return True
    else:
         print('Your package is not delivered...')
         return False

#check every N seconds if "delivered"
while not is_delivered():
    time.sleep(300)