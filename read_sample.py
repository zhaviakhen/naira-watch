# 1. import json
# 2. open sample.json
# 3. load it into data
# 4. loop through data
# 5. find USD to NGN
# 6. print it
import csv
import json
import logging
logging.basicConfig(
    filename="naira_watch.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logging.info("Scripts started")
try: 
  with open("sample.json") as f:
      data = json.load(f)
except FileNotFoundError:
    print("Could not find sample.json. Check it is in the naira-watch folder.")
    logging.error("sample.json not found")
    exit()
logging.info(f"Loaded {len(data)} records")
for item in data:
    if item["base"] == "USD" and item["quote"] == "NGN":
        print(item["date"], item["rate"])
        logging.info(f"USD to NGN on {item['date']} is {item['rate']}")
with open("rates.csv", "w" , newline="") as out:
    writer = csv.writer(out)
    writer.writerow(["date", "base", "quote", "rate"])
    for item in data:
        writer.writerow([item["date"], item["base"], item["quote"], item["rate"]])
logging.info("Wrote rates.csv")