import requests
import sys
import os
import csv

iiif = []

def set_urls(csv_file):
    for row in csv.DictReader(csv_file):
        iiif.append(f"{row['IIIF URL']}/info.json")
   
def check_urls(urls):
    header = ["URL", "response"]
    with open("status_IIIF_nvdgo.csv", 'w') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header)
        for url in urls:
            print(f"Checking URL:\n{url}")
            try:
                request = requests.get(url)
                writer.writerow([url, request.status_code])
            except requests.ConnectionError: print("fail")
    output_file.close()

if __name__ == "__main__":
    path = sys.argv[1]
    with open(path, 'r') as input_file:
        set_urls(input_file)
    input_file.close()
    check_urls(iiif)
