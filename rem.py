import requests

url = "http://127.0.0.1:8000/grammar/choose_correct"  # Example API endpoint

params = {
    "email": "aa",
}
response = requests.get(url, params=params)

if response.status_code == 200:  # 200 means success
    data = response.json()  # Convert response to JSON format
    print("Data extracted successfully:")
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}")
