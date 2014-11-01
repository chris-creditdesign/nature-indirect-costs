import csv
import sys

f1 = open(sys.argv[1], 'rt')
f2 = open(sys.argv[2], 'rt')
w = open(sys.argv[3], 'wt')

# reader 1 

reader1 = csv.DictReader(f1)

list_orgs1 = []

for row in reader1:
	list_orgs1.append( row['Organization Name'] )

# print len(list_orgs1)

set_orgs1 = set(list_orgs1)

# print len(set_orgs1) Duplicates in indirect-costs.csv

# reader 2 

reader2 = csv.DictReader(f2)

list_orgs2 = []

for row in reader2:
	list_orgs2.append( row['Organization Name'] )

set_orgs2 = set(list_orgs2)

missing_orgs = set_orgs1.difference(set_orgs2);

writer = csv.writer(w, quoting=csv.QUOTE_NONNUMERIC)

writer.writerow( ('Organization Name', "") )

for i, v in enumerate(missing_orgs):
	writer.writerow( (v, "") )

