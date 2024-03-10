
import  json
import urllib3
# from botocore.vendored import requests

def lambda_handler(event, context):
   # import required modules
    
    print(event)
    
    # event['parameters'][0]['value']
    
# Enter your API key here
    api_key = "b9f1538e0e30ab2e58841129a90e8127"

# base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
    city_name = "Delhi"

# complete_url variable to store
# complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# get method of requests module
# return response object
    #response = requests.get(complete_url)
    http = urllib3.PoolManager()
    r = http.request('GET', complete_url)
    x= json.loads(r.data)

    #x = response.json()
    lat = x['coord']['lat']
    lon = x['coord']['lon']
    
    response = json.dumps({
		'messageVersion': '1.0',
		"response": {
			'actionGroup': "event.actionGroup",
			"apiPath": "event.apiPath",
			"httpMethod": "event.httpMethod",
			"httpStatusCode": 200,
			"responseBody": {
				'application/json': {
					"body": {"lat": x['coord']['lat']},
				},
			},
			"sessionAttributes": {},
			"promptSessionAttributes": {},
		},
    })
    
    return response
