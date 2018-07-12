#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Let's assume that you combined the code from the previous 2 exercises
# with code from the lesson on how to build requests, and downloaded all the data locally.
# The files are in a directory "data", named after the carrier and airport:
# "{}-{}.html".format(carrier, airport), for example "FL-ATL.html".
# The table with flight info has a table class="dataTDRight".
# There are couple of helper functions to deal with the data files.
# Please do not change them for grading purposes.
# All your changes should be in the 'process_file' function
from bs4 import BeautifulSoup
from zipfile import ZipFile
import os

SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
datadir = os.path.join(SCRIPT_DIRECTORY, "data")


def open_zip(datadir):
    with ZipFile('{0}.zip'.format(datadir), 'r') as myzip:
        myzip.extractall()


def process_all(datadir):
    files = os.listdir(datadir)
    return files


def process_file(f):
    data = []
    info = {}
    info["courier"], info["airport"] = f[:6].split("-")

    with open("{}/{}".format(datadir, f), "r") as html:

        soup = BeautifulSoup(html, 'html5lib')
        table = soup.find(id='DataGrid1')
        rows = table.find_all('tr', class_='dataTDRight')
        for row in rows:
            cells = row.find_all('td')
            if cells[1].text != 'TOTAL':
                info['year'] = int(cells[0].text)
                info['month'] = int(cells[1].text)
                domestic = int(cells[2].text.replace(',', ''))
                international = int(cells[3].text.replace(',', ''))
                info['flights'] = {"domestic": domestic,
                                   "international": international}
                data.append(info)
    return data


def test():
    print "Running a simple test..."
    files = process_all(datadir)
    data = []
    for f in files:
        data += process_file(f)
    assert len(data) == 3
    for entry in data[:3]:
        assert type(entry["year"]) == int
        assert type(entry["flights"]["domestic"]) == int
        assert len(entry["airport"]) == 3
        assert len(entry["courier"]) == 2
    print "... success!"


if __name__ == "__main__":
    test()
