import sys
import csv

filename = sys.argv[1]
topic = sys.argv[2]

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    headers = []
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            headers = row
        else:
            out_file = None
            for i, col_value in enumerate(row):
                if i == 0:
                    out_file = open(col_value.strip() + ".md", "w")
                elif i == 1:
                    out_file.write(f"#{topic.strip()}\n")
                    out_file.write(f"- {headers[i]}:: {col_value}\n")
                else:
                    out_file.write(f"  {headers[i]}:: {col_value}\n")
            out_file.close()
        line_count += 1
