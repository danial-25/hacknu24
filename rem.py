import requests

url = 'https://hacknu24.onrender.com/reading'  # Example API endpoint

response = requests.get(url)

if response.status_code == 200:  # 200 means success
    data = response.json()  # Convert response to JSON format
    print('Data extracted successfully:')
    print(data)
else:
    print(f'Request failed with status code: {response.status_code}')