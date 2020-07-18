import os
import csv

#print(dir(os.path))


file_to_load = os.path.join("C:/python", "hedges.csv")

with open(file_to_load) as trades:
    file_reader = csv.reader((line.replace('\0','') for line in trades), delimiter=",")
    for trade in file_reader:
        if len(trade) > 0:
            for info in trade:
                if info[:2] == 'CF':
                    print(info)

#print(trades)
