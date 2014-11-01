import csv
import sys

f = open(sys.argv[1], 'rt')
w = open(sys.argv[2], 'wt')

reader = csv.reader(f)

list_all_orgs = []


for row in reader:
	list_all_orgs.append(row)


for i,v in enumerate(list_all_orgs):
	if i > 0:
		try:
			v.append("%.1f" % ((float(v[8]) / float(v[7])) * 100))
		except Exception as e:
			v.append(0)
			print e


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

for i,v in enumerate(list_all_orgs):
	if i > 0:
		writer.writerow( (v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7], v[8], v[9], v[10]) )
