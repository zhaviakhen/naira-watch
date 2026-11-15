import time
import json 
import os
from datetime import date
import requests
url = "https://api.frankfurter.dev/v2/rates?base=USD&quotes=NGN"
response = None
for attempt in range(1,4):
     try:
          r =requests.get(url, timeout=10)
          r.raise_for_status()
          response = r
          break
     except requests.exceptions.RequestException as error:
          print(f"Attempt {attempt} failed: {error}")
          time.sleep(2)
if response is None:
     print("All 3 attempts failed. Try again later.")
     exit()
print(response.status_code)
data = response.json()
os.makedirs("data/raw", exist_ok=True)
filename = f"data/raw/rates_{date.today()}.json"
with open(filename, "w") as f:
     json.dump(data, f, indent=2)
     print("Saved", filename)
for item in data:
     print(item["date"], item["rate"])