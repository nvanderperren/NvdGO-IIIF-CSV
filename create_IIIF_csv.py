import csv
import os
import sys

def parse_csv(path):
    with open(path, 'r') as input_file:
        reader = csv.DictReader(input_file)
        for row in reader:
            create_iiif_csv(row)
        input_file.close()

def write_csv(data):
    output_file = open(f"{organisation}_iiif.csv", 'w')
    writer = csv.writer(output_file)
    writer.writerows(data)
    output_file.close()

def create_iiif_csv(row):
    iiif_url = row['IIIF']
    if (iiif_url != 'NULL'):
        date_and_page = get_date_page(iiif_url)
        my_data.append([f"{row['PID']}", f"{row['aanbieder']}", f"{row['abraham']}", f"{row['titel']}",
                            f"{date_and_page[0]}", f"{date_and_page[1].lstrip('0')}", f"{iiif_url}"])
 
def get_date_page(url):
    data = url.split("_")
    return [data[1], data[2]]

if __name__ == "__main__":
    path = sys.argv[1]
    filename = os.path.basename(path)
    organisation = os.path.splitext(filename)[0]
    my_data = [["PID", "Aanbieder", "Abrahamcode", "Titel",
                "Uitgavedatum", "Pagina", "IIIF URL"]]  
    parse_csv(path)
    write_csv(my_data)
