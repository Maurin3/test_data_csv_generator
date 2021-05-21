#!/usr/bin/env python3

import csv
import os



if __name__ == "__main__":
    print("Welcome to the test data CSV generator !")
    file_name = input("How do you want to name the file ? (without the '.csv' extension) ")

    location = input("Where do you want to create the CSV ? ")
    real_location = os.path.abspath(os.path.expanduser(location))

    header_string = input("List the header/field you want to populate (split columns by ',') ")
    header = header_string.split(",")
    line_templates = []
    for i, elem in enumerate(header):
        value = input("What value pattern do you want ? (add %s for the numbers) ")
        line_templates.append(str(value).replace("%s", "µ"))

    nb_lines = int(input("How many lines do you want to generate ? "))

    with open(f'{real_location}/{file_name}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(header)
        for i in range(1, nb_lines + 1):
            lines = []
            for line in line_templates:
                lines.append(line.replace("µ", str(i)))
            writer.writerow(lines)
    print("Your CSV file is ready !")
