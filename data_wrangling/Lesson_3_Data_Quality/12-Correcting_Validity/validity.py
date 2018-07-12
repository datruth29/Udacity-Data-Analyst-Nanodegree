"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in range, as described above,
  write that line to the output_good file
- if the value of the field is not a valid year, 
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the 
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import os

DATADIR = os.path.dirname(os.path.realpath(__file__))
INPUT_FILE = os.path.join(DATADIR, 'autos.csv')
OUTPUT_GOOD = os.path.join(DATADIR, 'autos-valid.csv')
OUTPUT_BAD = os.path.join(DATADIR, 'FIXME-autos.csv')


def yearValid(year):
    return year.isdigit() and int(year) >= 1886 and int(year) <= 2014


def process_file(input_file, output_good, output_bad):
    good_data = []
    bad_data = []

    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        for row in reader:
            if row['URI'].find("dbpedia.org") < 0:
                continue
            year = row['productionStartYear'][:4]
            if yearValid(year):
                row['productionStartYear'] = int(year)
                good_data.append(row)
            else:
                bad_data.append(row)

    with open(OUTPUT_GOOD, "w", newline='') as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames=header)
        writer.writeheader()
        writer.writerows(good_data)

    with open(OUTPUT_BAD, 'w', newline='') as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames=header)
        writer.writeheader()
        writer.writerows(bad_data)


def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()
