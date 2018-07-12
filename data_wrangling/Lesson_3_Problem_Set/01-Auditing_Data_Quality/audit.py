#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then clean it up.
In the first exercise we want you to audit the datatypes that can be found in some particular fields in the dataset.
The possible types of values can be:
- 'NoneType' if the value is a string "NULL" or an empty string ""
- 'list', if the value starts with "{"
- 'int', if the value can be cast to int
- 'float', if the value can be cast to float, but is not an int
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and the datatypes that can be found in the field.
All the data initially is a string, so you have to do some checks on the values first.

"""
import codecs
import csv
import json
from pprint import pprint
import os

DATADIR = os.path.dirname(os.path.realpath(__file__))
CITIES = os.path.join(DATADIR, 'cities.csv')

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal",
          "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long",
          "areaLand", "areaMetro", "areaUrban"]


def is_float(text):
    try:
        float(text)
        return True
    except ValueError:
        return False


def get_field_type(field):
    if field == 'NULL' or field == '':
        return type(None)
    if field[0] == '{':
        return type([])
    if field.isdigit():
        return type(1)
    if is_float(field):
        return type(1.1)
    return type('str')


def audit_file(filename, fields):
    fieldtypes = {}
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['URI'].find("dbpedia.org") < 0:
                continue
            for field in FIELDS:
                data = row[field]
                types = fieldtypes.get(field, set())
                data_type = get_field_type(data)
                if data_type not in types:
                    types.add(data_type)
                    fieldtypes[field] = types
    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])


if __name__ == "__main__":
    test()
