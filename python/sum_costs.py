import csv
import sys

f = open(sys.argv[1], 'rt')
w = open(sys.argv[2], 'wt')

reader = csv.DictReader(f)

list_all_orgs = []
list_org_names = []
list_summed_orgs = []

for row in reader:
	list_all_orgs.append(row)


for i, v in enumerate(list_all_orgs):
	list_org_names.append(v['Organization Name'])


set_org_names = set(list_org_names)

for i, v in enumerate(set_org_names):
	my_dict = {'Organization Name':v,
				'Direct Cost':0,
				'Indirect Cost':0,
				'Funding':0
				}
	list_summed_orgs.append(my_dict)

for i, v in enumerate(list_all_orgs):
	for y, x in enumerate(list_summed_orgs):
		if v['Organization Name'] == x['Organization Name']:
			try:
				x['Direct Cost'] += int(v['Direct Cost'])
			except Exception as e: 
				print e
			try:
				x['Indirect Cost'] += int(v['Indirect Cost'])
			except Exception as e: 
				print e
			try:
				x['Funding'] += int(v['Funding'])
			except Exception as e: 
				print e

fieldnames = ('Organization Name', 'Direct Cost', 'Indirect Cost', 'Funding')

writer = csv.DictWriter(w, fieldnames=fieldnames )

headers = dict( (n,n) for n in fieldnames )

writer.writerow(headers)

for y, x in enumerate(list_summed_orgs):
	writer.writerow( { 'Organization Name':x['Organization Name'], 'Direct Cost':x['Direct Cost'], 'Indirect Cost':x['Indirect Cost'], 'Funding':x['Funding']})


