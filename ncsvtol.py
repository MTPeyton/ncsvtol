import sys
import csv

filename = sys.argv[1]

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    headers = []
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            headers = row
        else:
            for i, col_value in enumerate(row):
                if i == 0:
                    print(f"- {col_value}")
                elif i == 1:
                    print(f"    - {headers[i]}:: {col_value}")
                else:
                    print(f"      {headers[i]}:: {col_value}")
        line_count += 1
