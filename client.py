import requests

URL = "https://dsproject-c1qq.onrender.com"

text_to_send = input("Enter text to transform: ")
response = requests.post(URL, json={"text": text_to_send})

if response.status_code == 200:
    print("\n--- Cloud Results ---")
    print(response.json())
else:
    print("Error:", response.text)