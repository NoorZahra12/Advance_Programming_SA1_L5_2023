# accessing twitter dev credentials
credentials = {
    'consumer_key': 'your_consumer_key',
    'consumer_secret': 'your_consumer_secret',
    'access_token': 'your_access_token',
    'access_secret': 'your_access_secret'
}

# importing statements
import sys
import json
import csv
import os
from requests_oauthlib import OAuth1Session


# getting file from local file
script_directory = os.path.dirname(os.path.realpath(__file__))
local_file = os.path.join(script_directory, "textfile.txt")

# get authentication parameters from a local file
with open(local_file) as txtfile:
    contents = txtfile.readline()
credentials = eval(contents.strip('\n'))

# api OAuth 1.0 authentication
twitter = OAuth1Session(
    credentials.get('consumer_key'),
    client_secret=credentials.get('consumer_secret'),
    resource_owner_key=credentials.get('access_token'),
    resource_owner_secret=credentials.get('access_secret')
)

# host location of api
host = 'https://api.twitter.com'
# api GET request for user ids of followers
get_path = '/1.1/search/tweets.json?q=%40IUBloomington'
url = host + get_path
response = twitter.get(url)

# PARSE
# check the HTTP response code
print(response.status_code)
# parse the JSON data into a Python object
try:
    tweets = response.json()
except json.JSONDecodeError:
    print("Error decoding JSON")
    tweets = {}

# TRANSFORM
# check the structure of the data
print(len(tweets))
print(type(tweets))
print(tweets.keys())
print(len(tweets['statuses']))
# encode uncommon characters
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
print(str(tweets['statuses']).translate(non_bmp_map))
