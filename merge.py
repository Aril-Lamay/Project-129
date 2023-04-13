import csv

dataset_1 = []
dataset_2 = []

with open("New_Dwarf_Stars.csv",'r') as f:
    csvreader = csv.reader(f)
    for raw in csvreader:
        dataset_1.append(raw)

with open("bright_stars.csv",'r') as f:
    csvreader = csv.reader(f)
    for raw in csvreader:
        dataset_2.append(raw)

header_1 = dataset_1[0]
star_data_1 = dataset_1[1:]

header_2  = dataset_2[0]
star_data_2 = dataset_2[1:]

headers = header_1 + header_2
star_data = []

for index,data_raw in enumerate(star_data_2):
    star_data.append(star_data_2[index] + star_data_1[index])

with open("final.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)