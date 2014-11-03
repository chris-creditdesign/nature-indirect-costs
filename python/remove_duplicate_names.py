import csv
import sys

f = open(sys.argv[1], 'rt')
w = open(sys.argv[2], 'wt')

reader = csv.DictReader(f)

list_all_orgs = []

for row in reader:
	list_all_orgs.append(row)

for i, v in enumerate(list_all_orgs):
	if v['Organization Name'] == "Ohio State University": v['Organization Name'] = "OHIO STATE UNIVERSITY"
	elif v['Organization Name'] == "MASSACHUSETTS GENERAL HOSP": v['Organization Name'] = "MASSACHUSETTS GENERAL HOSPITAL"
	else: pass

fieldnames = ('Organization Name','Direct Cost', 'Indirect Cost', 'Funding')

writer = csv.DictWriter(w, fieldnames=fieldnames )

headers = dict( (n,n) for n in fieldnames )

writer.writerow(headers)

for y, x in enumerate(list_all_orgs):
	writer.writerow( { 'Organization Name':x['Organization Name'], 'Direct Cost':x['Direct Cost'], 'Indirect Cost':x['Indirect Cost'], 'Funding':x['Funding']})

print "Finished"