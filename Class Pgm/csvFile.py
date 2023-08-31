#       CSV-BASICS
# importing CSV module :
import csv

with open("CSVFILE.csv","r") as csv_file:
    # creating Reader obj to read from the csv_file
    Reader=csv.reader(csv_file)
    for line in Reader:
        print(line[0]," ",line[1]," ",line[2])

    with open("CSVFILE2.csv","w") as csv_file:
        # creating Reader obj to read from the csv_file
        Writer=csv.writer(csv_file)
        for line in Reader:
            Writer.writerow(line)
