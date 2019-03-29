#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
print "Size of dataset: ", len(enron_data)

for key in enron_data:
    print "Features per person: ", len(enron_data[key])
    print enron_data[key]
    break

npoi = 0
for key in enron_data:
    if enron_data[key]["poi"] == True:
        npoi = npoi + 1

print "Person of interests: ", npoi

print "James Prentice's total stock value: ", enron_data["PRENTICE JAMES"]["total_stock_value"]
print "Mails by Wesley Colwell to poi's: ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "Jeffrey K Skilling's exercised stock options: ", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
print "Kenneth Lay's total payments: ", enron_data["LAY KENNETH L"]["total_payments"]
print "Andrew Fastow's total payments: ", enron_data["FASTOW ANDREW S"]["total_payments"]

nsal = 0
for key in enron_data:
    if enron_data[key]["salary"] != "NaN":
        nsal = nsal + 1

print "Person with salaries: ", nsal

nmail = 0
for key in enron_data:
    if enron_data[key]["email_address"] != "NaN":
        nmail = nmail + 1

print "Person with mails: ", nmail


ntp = 0
for key in enron_data:
    if enron_data[key]["total_payments"] == "NaN":
        ntp = ntp + 1

print "Person with total payments not available: ", ntp, " ", float(ntp)/float(len(enron_data)) * 100


ntp = 0
for key in enron_data:
    if enron_data[key]["poi"] == True and enron_data[key]["total_payments"] == "NaN":
        ntp = ntp + 1

print "POIs with total payments not available: ", ntp, " ",float(ntp)/float(npoi) * 100
