# -*- coding: utf-8 -*-
# Find the time and value of max load for each of the regions
# COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
# and write the result out in a csv file, using pipe character | as the delimiter.
# An example output can be seen in the "example.csv" file.
import xlrd
import os
import csv
from zipfile import ZipFile
DATADIR = os.path.dirname(os.path.realpath(__file__))
zipfile = os.path.join(DATADIR, "2013_ERCOT_Hourly_Load_Data")
datafile = os.path.join(DATADIR, "2013_ERCOT_Hourly_Load_Data.xls")
outfile = os.path.join(DATADIR, "2013_Max_Loads.csv")


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        print("Unzipped")
        myzip.extractall(path=DATADIR)


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    headers = ['Station', 'Year', 'Month', 'Day', 'Hour', 'Max Load']
    data = []
    data.append(headers)
    rows = sheet.nrows
    cols = sheet.ncols-1
    time_data = [sheet.cell_value(r, 0) for r in range(rows)]
    for col in range(1, cols):
        station = [sheet.cell_value(r, col) for r in range(rows)]
        max_load = max(station[1:])
        max_index = station.index(max_load)
        max_time = xlrd.xldate_as_tuple(time_data[max_index], 0)
        year = max_time[0]
        month = max_time[1]
        day = max_time[2]
        hour = max_time[3]
        row = [station[0], year, month, day, hour, max_load]
        data.append(row)
    return data


def save_file(data, filename):
    with open(outfile, 'w') as csvfile:
        w = csv.writer(csvfile, delimiter='|', lineterminator='\n')
        for row in data:
            w.writerow(row)
    return None


def test():
    open_zip(zipfile)
    data = parse_file(datafile)
    save_file(data, outfile)

    ans = {'FAR_WEST': {'Max Load': "2281.2722140000024",
                        'Year': "2013", "Month": "6", "Day": "26", "Hour": "17"}}

    fields = ["Year", "Month", "Day", "Hour", "Max Load"]
    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            s = line["Station"]
            if s == 'FAR_WEST':
                for field in fields:
                    print("Made it here")
                    assert ans[s][field] == line[field]


test()
