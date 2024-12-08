import requests
from pprint import pprint

# this is to run locally
#url = 'http://localhost:8080/2015-03-31/functions/function/invocations'


# this the url of the deployed lambda function in api gateway
url = 'https://"somethinghere".execute-api.eu-west-2.amazonaws.com/testing/predict'

data = {'url': 'http://bit.ly/mlbookcamp-pants'}

result = requests.post(url, json=data).json()
pprint(result)
