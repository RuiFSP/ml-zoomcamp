import requests

url = "http://127.0.0.1:9696/predict"
customer_data = {
    "job": "management",
    "duration": 400,
    "poutcome": "success"
}

response = requests.post(url, json=customer_data)

if response.status_code == 200:
    print("Prediction:", response.json())
else:
    print("Error:", response.status_code, response.text)