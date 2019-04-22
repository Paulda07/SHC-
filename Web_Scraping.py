# from requests import get
# from requests.exceptions import RequestException
# from contextlib import closing
# from bs4 import BeautifulSoup

# def simple_get(url):

#     try:
#         with closing(get(url, stream=True)) as resp:
#             if is_good_response(resp):
#                 return resp.content
#             else:
#                 return None

#     except RequestException as e:
#         log_error('Error during requests to {0} : {1}'.format(url, str(e)))
#         return None


# def is_good_response(resp):

#     content_type = resp.headers['Content-Type'].lower()
#     return (resp.status_code == 200 
#             and content_type is not None 
#             and content_type.find('html') > -1)


# def log_error(e):

#     print(e)

# raw_html = simple_get('https://realpython.com/blog/')
# print(len(raw_html))

import urllib3
from bs4 import BeautifulSoup as b
import requests

base_url = 'https://pipl.com/search/?q='
request = 'Paul+Sampson'
url_seperator = '&l=&sloc=&in=6'

url = base_url+request+url_seperator

# html = urllib3.urlopen(url)

# print (html)

http = urllib3.PoolManager()


response = requests.get(url)

print (response)
# soup = BeautifulSoup(response.data)