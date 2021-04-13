import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from urllib.request import urlopen
import datetime


url="https://en.wikipedia.org/wiki/List_of_school_shootings_in_the_United_States"
html = urlopen(url) 
soup = BeautifulSoup(html, 'html.parser')
tables = soup.find_all('table')
year_dict = {
    '2000': [],
    '2001': [],
    '2002': [],
    '2003': [],
    '2004': [],
    '2005': [],
    '2006': [],
    '2007': [],
    '2008': [],
    '2009': [],
    '2010': [],
    '2011': [],
    '2012': [],
    '2013': [],
    '2014': [],
    '2015': [],
    '2016': [],
    '2017': [],
    '2018': [],
    '2019': [],
    '2020': [],
    '2021': []
}


count = 0
for table in tables:
    if len(table) >1:
        rows = table.find_all('tr')

        #Skip the first row, which is the name of the columns
        for row in rows[1:]:
            individual_incident = row.find_all('td')
            individual_incident_date = individual_incident[0].text.split(',')[1].strip()
            if individual_incident_date in year_dict.keys():
                date = individual_incident[0].text.replace('\n', '')
                location = individual_incident[1].text.replace('\n', '')
                year_dict[individual_incident_date].append(date + " | " + location)
                count += 1


print("\n====================================================================")


print("\nNumber of US School Shooting Incidents by Year (2000-2021):\n")
for key in year_dict:
    print('%s: %d' % (key, len(year_dict[key])))


print("\n====================================================================")


print("\nTotal US School Shooting Incidents (2000-2021): %d" % count)


print("\n====================================================================")


def occurences_within_rage(from_, to_):
    from_ = from_
    to_ = to_
    count = 0
    for year in range(from_.year, to_.year + 1):
        events_of_year = year_dict[str(year)]
        for event in events_of_year:
            full_date = event.split(" | ")[0].split(' ')
            month = datetime.datetime.strptime(full_date[0], "%B").month
            day = full_date[1].strip(",")

            converted_date = datetime.date(year, month, int(day))

            if (from_ <= converted_date <= to_):
                count += 1
    return count


Obama = occurences_within_rage(datetime.date(2009, 1, 20), datetime.date(2017, 1, 20))
print("\n(January 20, 2009 - January 20, 2017) : 8 YEARS")
print("Total Incidents During Obama's Presidency: %d incidents" % Obama)
print("Average Incidents During Obama's Presidency: %f" % (Obama/8))


print("\n====================================================================")


Trump = occurences_within_rage(datetime.date(2017, 1, 20), datetime.date(2021, 1, 20))
print("\n(January 21, 2017 - January 20, 2021) : 4 YEARS")
print("Total Incidents During Trump's Presidency: %d incidents" % Trump)
print("Average Incidents During Trump's Presidency: %f" % (Trump/4))


print("\n====================================================================")