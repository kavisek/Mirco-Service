import http
import requests
import urllib

headers = {'X-API-TOKEN': 'your_token_here'}
payload = "'title'='value1'&'name'='value2'"

conn = httplib.HTTPConnection("heise.de")
conn.request("POST", "", payload, headers)
response = conn.getresponse()

print response

# Ask for a Predictin from the API: `curl -u kavi:python -i -H "Content-Type: application/json" -X POST -d '{"sepal length (cm)":"7.1","sepal width (cm)": "3.0","petal length (cm)": "5.9","petal width (cm)": "2.1"}' http://localhost:5000/todo/api/v1.0/tasks`

import requests

headers = {'X-API-TOKEN': 'your_token_here'}
payload = {'title': 'value1', 'name': 'value2'}

r = requests.post("http://foo.com/foo/bar", data=payload, headers=headers)
print(r)
print('Done')
