import requests
import time 
from IPython.core.display import clear_output
import requests_cache

requests_cache.install_cache()


#response = requests.get("http://api.open-notify.org/astros.json")
#print(response.status_code)


def get_parameterized_entity(parameters):
    response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
    return response


def get_entity(url, headers, payload):
    response = requests.get(url, headers=headers, params=payload)
    return response

def get_paged_entities(url, headers):
    responses = []

    page = 1
    total_pages = 20 # this is just a dummy number so the loop starts

    while page <= total_pages:
        payload = {
            'api_key': API_KEY,        
            'method': 'chart.gettopartists',
            'limit': 500,
            'page': page,
            'format': 'json'
        }

        # print some output so we can see the status
        print("Requesting page {}/{}".format(page, total_pages))
        # clear the output to make things neater
        clear_output(wait = True)
        # make the API call
        response = get_entity(url, headers,payload)

        # if we get an error, print the response and halt the loop
        if response.status_code != 200:
            print(response.text)
            break

        # extract pagination info        
        page = int(response.json()['artists']['@attr']['page'])
        #total_pages = int(response.json()['artists']['@attr']['totalPages'])

        # append response
        responses.append(response)

        # if it's not a cached result, sleep
        if not getattr(response, 'from_cache', False):
            time.sleep(0.25)

        # increment the page number
        page += 1
    
    return responses
    
    
    #response = requests.get(url, headers=headers, params=payload)
    #return response

##Start

API_KEY = '202d1f5a468eba539c6c163a2c847a40'
USER_AGENT = 'Dataquest'

url = 'http://ws.audioscrobbler.com/2.0/'

headers = {
    'user-agent': USER_AGENT
}

payload = {
    'api_key': API_KEY,
    'method': 'chart.gettopartists',
    'format': 'json'
}

#a = get_entity(url, headers, payload)

parameters = {
    "lat": 40.71,
    "lon": -74
}
#b = get_parameterized_entity(parameters)

get_paged_entities(url, headers)


#post
#put
#get id/all 
#get all 
"""
Application name	ApiHelper
API key	202d1f5a468eba539c6c163a2c847a40
Shared secret	0ad936baea055065a6cb7807f9e648e8
Registered to	acarson510
"""




