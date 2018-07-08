#!/usr/bin/env python
# -*- coding: utf-8 -*-
# All your changes should be in the 'extract_airports' function
# It should return a list of airport codes, excluding any combinations like "All"

from bs4 import BeautifulSoup
import os

DATADIR = os.path.dirname(os.path.realpath(__file__))
html_page = os.path.join(DATADIR, "options.html")


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, 'html5lib')
        airportList = soup.find(id='AirportList')
        for airports in airportList.find_all('option'):
            airport = airports['value']
            if len(airport) == 3 and airport != 'All':
                data.append(airport)
    return data


def test():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data


test()
