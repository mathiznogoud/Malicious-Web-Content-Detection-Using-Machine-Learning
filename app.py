from flask import Flask, request, jsonify, json, make_response
from prediction import get_prediction_from_url
import requests, urllib2
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/localPrediction/",methods=['GET', 'POST'])
def check():
	content=request.json
	url = content['url']
	google_api_url='https://safebrowsing.googleapis.com/v4/threatMatches:find?key=AIzaSyDj5s8zj2-a_a-sey3Hjw8clebqJGcSIuU'
	data =   {
			    "client": {
			      "clientId":      "URL Phishing Detection",
			      "clientVersion": "1.0"
			    },
			    "threatInfo": {
			      "threatTypes":      ["MALWARE", "SOCIAL_ENGINEERING"],
			      "platformTypes":    ["ANY_PLATFORM"],
			      "threatEntryTypes": ["URL"],
			      "threatEntries": [
			        {"url": url}
			      ]
			    }
			  }
	headers = {'content-type': 'application/json'}
	r = requests.post(google_api_url, data=json.dumps(data), headers=headers)
	#content = r.text
	dictdump = json.loads(r.text)
	print(type(content))
	#a=	content.find('matches')
	#print str(a) + content
	if 'matches' in dictdump:
		return "Malicious"
	else:
		req2 = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
		html = urllib2.urlopen(req2).read()
		print(html)
		result = get_prediction_from_url(url,html)
		print result
		if (result == 1):
			return "Safe"
		elif (result	== -1):
			return "Malicious"




if __name__ == "__main__":
    app.run(threaded=True,port=5000)