import requests

url = 'http://127.0.0.1:5000/predict_home_price'
data = {"total_sqft": 1000, "location": "1st Phase JP Nagar", "bath": 3, "bhk": 3}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=data, headers=headers)
print(response.text)

url = 'http://127.0.0.1:5000/predict_home_price'
data = {"total_sqft": 1000, "location": "1st Phase JP Nagar", "bath": 3, "bhk": 3}

response = requests.post(url, json=data)
print(response.text)
