import concurrent.futures
import requests
import json
from bs4 import BeautifulSoup
import pymongo
from pymongo import MongoClient

# URL
URL = 'https://old.accupass.com/search/changeconditions/r/1/0/6/0/1/{0}/20160101/20161231'
URL_API = 'https://api.accupass.com/v3/events/'
PROXIES = {
    'http': 'http://251.38.227.187',
    'http': 'http://87.21.107.55',
    'http': 'http://210.176.22.238',
    'http': 'http://44.143.96.18',
    'http': 'http://225.190.206.92',
    'http': 'http://96.57.119.25',
    'http': 'http://18.252.87.90',
    'http': 'http://248.48.80.38',
    'http': 'http://164.22.14.13',
    'http': 'http://187.100.109.56',
    'http': 'http://87.66.237.15',
    'http': 'http://37.6.235.57',
    'http': 'http://154.29.70.130',
    'http': 'http://71.49.17.60',
    'http': 'http://122.19.141.13',
    'http': 'http://217.192.142.249',
    'http': 'http://24.214.221.86',
    'http': 'http://33.236.61.168',
    'http': 'http://218.241.88.168',
    'http': 'http://83.250.229.75',
}


# requests init page
def get_page(page):
    url = URL.format(page)
    resp = requests.get(url, proxies=PROXIES)
    if resp.status_code == 200:
        return resp

# parse event id 
def get_eventIdNumber(html):
    raw = html.div['event-row']
    eventIdNumber = json.loads(raw)['eventIdNumber']
    return eventIdNumber

# generate event id list
def get_eventIdList(page):
    resp = get_page(page)
    soup = BeautifulSoup(resp.content, 'lxml')
    idList = soup.find_all('div', attrs={'class': 'col-xs-12 col-sm-6 col-md-4'})
    eventList = []
    for item in idList:
        eventId = get_eventIdNumber(item)
        eventList.append(eventId)
    return eventList

def get_eventInfo(eventId):
    global accupass_collection
    resp = requests.get(URL_API+eventId, proxies=PROXIES)
    accupass_collection.insert_one(resp.json())

def scraper(page):
    eventList = get_eventIdList(page)
    for eventId in eventList:
        get_eventInfo(eventId)

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        future_to_item = {}
        for page in range(1625):
            future = executor.submit(scraper, page)
            future_to_item[future] = page
        for future in concurrent.futures.as_completed(future_to_item):
            print('done')

    # for page in range(1625):
    #     print('I am scraping page: ',page)
    #     scraper(page)

if __name__ == '__main__':
    try:
        client = MongoClient()
        db = client.accupass
        accupass_collection = db.accupass_taipei
        main()
    except KeyboardInterrupt:
        quit =True
