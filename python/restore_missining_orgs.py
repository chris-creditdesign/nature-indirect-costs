import csv
import sys

f1 = open(sys.argv[1], 'rt')
f2 = open(sys.argv[2], 'rt')
w = open(sys.argv[3], 'wt')

list_all_orgs = []

reader1 = csv.reader(f1)

for row in reader1:
	list_all_orgs.append(row)

list_all_discrepancies = []

reader2 = csv.reader(f2)

for row in reader2:
	list_all_discrepancies.append(row)

list_remaining_orgs = []

for i,v in enumerate(list_all_orgs):
	for y,z in enumerate(list_all_discrepancies):
		if v[0] == z[0]:
			list_remaining_orgs.append(v)


writer = csv.writer(w, quoting=csv.QUOTE_NONNUMERIC)

writer.writerow( (	'Organization Name', 
					'ORG_CITY',
					'ORG_STATE/ORG_COUNTRY',
					'FY12',
					'FY13',
					'Institution type',
					'Organization Name',
					'Direct Cost',
					'Indirect Cost',
					'Funding',
					'Calculated Indirect cost') )

for i,v in enumerate(list_remaining_orgs):
	if i > 0:
		writer.writerow( (v[0], v[1], v[2], v[3], v[4], v[5], v[0], 0, 0, 0, 0) )