import requests
import sys
import os
import csv

region_by_px_little = "/50,50,200,200/full/0/"
region_by_px_big = "/50,50,2000,2000/full/0/"
region_by_px_width = "/50,50,2500,90/full/0/"
region_by_px_height = "/50,50,90,2500/full/0/"
region_by_px_y_height = "/50,2000,90,1000/full/0/"
rotation_by_90s = '/full/full/90/'
mirroring = '/full/full/!0/'
size_by_w = '/full/800,/0/'
size_by_h = '/full/,800/0/'
size_by_pct = '/full/pct:80/0/'
size_by_wh = '/full/3000,2500/0/'
size_by_forced_wh = '/full/!3000,2500/0/'
combination = '/50,50,2000,1500/!3000,2500/!0/'
modifications = {"regionByPx (small)": region_by_px_little, "regionByPx (big)": region_by_px_big,
"regionByPx (focus width)": region_by_px_width, "regionByPx (focus height)": region_by_px_height,
"regionByPx (focus y - height)": region_by_px_y_height,  
"rotationBy90s": rotation_by_90s, "mirroring": mirroring, "sizeByW": size_by_w,
"sizeByH": size_by_h, "sizeByPct": size_by_pct, "sizeByWh": size_by_wh, 
"sizeByForcedWh": size_by_forced_wh, "combination": combination}
iiif_urls = ["https://iiif.meemoo.be/jm23b5x28q_19140131_0004", 
"https://iiif.meemoo.be/rx9377728b_19140504_0001", "https://iiif.meemoo.be/rx93777c4k_19180526_0002",
"https://iiif.meemoo.be/9p2w37mw6t_19160803_0005", "https://iiif.meemoo.be/tt4fn12n0w_19161108_0003",
"https://iiif.meemoo.be/8p5v698x44_19181112_0001", "https://iiif.meemoo.be/m03xs5k818_191412xx_0015"]

def create_csv():
    with open("nvdgo_image_api_tests.csv", 'w') as output_file:
        writer = csv.writer(output_file)
        url_list = [["action", "parameters", "URL", "response"]]
        for action, parameter in modifications.items():
            for url in iiif_urls:
                image_api_call = f"{url}{parameter}default.jpg"
                try:
                    print(f"Checking URL:\n{image_api_call}")
                    request = requests.get(image_api_call)
                    url_list.append([action, parameter, image_api_call, request.status_code])
                except requests.ConnectionError: print("fail") 
        writer.writerows(url_list)
    output_file.close()

create_csv()