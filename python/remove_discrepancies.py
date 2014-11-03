import csv
import sys

f = open(sys.argv[1], 'rt')
w = open(sys.argv[2], 'wt')

reader = csv.DictReader(f)

list_all_orgs = []

for row in reader:
	list_all_orgs.append(row)

for i, v in enumerate(list_all_orgs):
	if v['Organization Name'] == "NEWARK BETH ISRAEL MEDICAL CENTER": v['Organization Name'] = "BETH ISRAEL MEDICAL CTR (NEW YORK)"
	elif v['Organization Name'] == "BOWLING GREEN STATE UNIV BOWLING GREEN": v['Organization Name'] = "BOWLING GREEN STATE UNIVERSITY"
	elif v['Organization Name'] == "CALIFORNIA POLY STATE U SAN LOUIS OBISPO": v['Organization Name'] = "CALIFORNIA POLY STATE U SAN LUIS OBISPO"
	elif v['Organization Name'] == "CHILDRENS HOSPITAL OF PHILADELPHIA": v['Organization Name'] = "CHILDREN'S HOSP OF PHILADELPHIA"
	elif v['Organization Name'] == "CHILDREN'S HOSPITAL LOS ANGELES": v['Organization Name'] = "CHILDREN'S HOSPITAL OF LOS ANGELES"
	elif v['Organization Name'] == "CLARK UNIVERSITY ": v['Organization Name'] = "CLARK UNIVERSITY (WORCESTER, MA)"
	elif v['Organization Name'] == "CLEVELAND CLINIC LERNER COL/MED-CWRU": v['Organization Name'] = "CLEVELAND CLINIC LERNER COM-CWRU"
	elif v['Organization Name'] == "COLORADO STATE UNIVERSITY-FORT COLLINS": v['Organization Name'] = "COLORADO STATE UNIVERSITY"
	elif v['Organization Name'] == "COLUMBIA UNIVIVERSITY IN THE CITY OF NEW YORK": v['Organization Name'] = "COLUMBIA UNIV NEW YORK MORNINGSIDE"
	elif v['Organization Name'] == "CORNELL UNIVERSITY ITHACA": v['Organization Name'] = "CORNELL UNIVERSITY"
	elif v['Organization Name'] == "DANA-FARBER CANCER INSTITUTE": v['Organization Name'] = "DANA-FARBER CANCER INST"
	elif v['Organization Name'] == "FRED HUTCHINSON CANCER RESEARCH CENTER": v['Organization Name'] = "FRED HUTCHINSON CAN RES CTR"
	elif v['Organization Name'] == "WEIS CENTER FOR RESEARCH-GEISINGER CLINC": v['Organization Name'] = "GEISINGER CLINIC"
	elif v['Organization Name'] == "ALAN GUTTMACHER INSTITUTE": v['Organization Name'] = "GUTTMACHER INSTITUTE"
	elif v['Organization Name'] == "HARVARD UNIVERSITY MEDICAL SCHOOL": v['Organization Name'] = "HARVARD UNIVERSITY (MEDICAL SCHOOL)"
	elif v['Organization Name'] == "HARVARD UNIVERSITY SCHOOL OF PUBLIC HEALTH": v['Organization Name'] = "HARVARD UNIVERSITY (SCH OF PUBLIC HLTH)"
	elif v['Organization Name'] == "HEALTHPARTNERS RESEARCH FOUNDATION": v['Organization Name'] = "HEALTHPARTNERS INSTITUTE"
	elif v['Organization Name'] == "LOUISIANA STATE UNIV HSC NEW ORLEANS": v['Organization Name'] = "LOUISIANA STATE UNIV-UNIV OF NEW ORLEANS"
	elif v['Organization Name'] == "LUDWIG INSTITUTE FOR CANCER RESEARCH": v['Organization Name'] = "LUDWIG INSTITUTE  FOR CANCER RES  LTD"
	elif v['Organization Name'] == "CHILDREN'S MEMORIAL HOSPITAL (CHICAGO)": v['Organization Name'] = "LURIE CHILDREN'S HOSPITAL OF CHICAGO"
	elif v['Organization Name'] == "MC LEAN HOSPITAL (BELMONT, MA)": v['Organization Name'] = "MCLEAN HOSPITAL"
	elif v['Organization Name'] == "NATIONAL DISEASE RESEARCH INTERCHANGE": v['Organization Name'] = "National Disease Research Interchange"
	elif v['Organization Name'] == "NORTHERN CALIFORNIA INSTITUTE RES & EDUC": v['Organization Name'] = "NORTHERN CALIFORNIA INSTITUTE/RES/EDU"
	elif v['Organization Name'] == "NORTHSHORE UNIVERSITY HEALTHSYSTEM*": v['Organization Name'] = "NORTHSHORE UNIVERSITY HEALTHSYSTEM"
	elif v['Organization Name'] == "OREGON HEALTH AND SCIENCE UNIVERSITY": v['Organization Name'] = "OREGON HEALTH & SCIENCE UNIVERSITY"
	elif v['Organization Name'] == "Organization Name - Indirect costs worksheet": v['Organization Name'] = "Organization Name - Copy of Worldwide2013"
	elif v['Organization Name'] == "PHOENIX BIOSYSTEMS, INC.": v['Organization Name'] = "PHOENIX BIOSYSTEM, INC."
	elif v['Organization Name'] == "SLOAN-KETTERING INSTITUTE FOR CANCER RES": v['Organization Name'] = "SLOAN-KETTERING INST CAN RES"
	elif v['Organization Name'] == "ST. LUKE'S-ROOSEVELT HOSPITAL": v['Organization Name'] = "ST. LUKE'S-ROOSEVELT INST FOR HLTH SCIS"
	elif v['Organization Name'] == "STANFORD": v['Organization Name'] = "STANFORD UNIVERSITY"
	elif v['Organization Name'] == "TEMPLE UNIVERSITY": v['Organization Name'] = "TEMPLE UNIV OF THE COMMONWEALTH"
	elif v['Organization Name'] == "TEXAS A&M UNIVERSITY-COMMERCE": v['Organization Name'] = "TEXAS A&M UNIVERSITY-CORPUS CHRISTI"
	elif v['Organization Name'] == "UNIVERSITY OF NORTH CAROLINA CHAPEL HILL": v['Organization Name'] = "UNIV OF NORTH CAROLINA CHAPEL HILL"
	elif v['Organization Name'] == "UNIVERSITY OF ARKANSAS MED SCIS LTL ROCK": v['Organization Name'] = "UNIVERSITY OF ARKANSAS AT LITTLE ROCK"
	elif v['Organization Name'] == "UNIVERSITY OF COLORADO AT BOULDER": v['Organization Name'] = "UNIVERSITY OF COLORADO"
	elif v['Organization Name'] == "UNIVERSITY OF GEORGIA (UGA)": v['Organization Name'] = "UNIVERSITY OF GEORGIA"
	elif v['Organization Name'] == "UNIVERSITY OF LOUISVILLE": v['Organization Name'] = "UNIVERSITY OF LOUISVILLE RES FDN"
	elif v['Organization Name'] == "UNIVERSITY OF MAINE": v['Organization Name'] = "UNIVERSITY OF MAINE ORONO"
	elif v['Organization Name'] == "UNIVERSITY OF MICHIGAN AT ANN ARBOR": v['Organization Name'] = "UNIVERSITY OF MICHIGAN"
	elif v['Organization Name'] == "UNIVERSITY OF MINNESOTA TWIN CITIES": v['Organization Name'] = "UNIVERSITY OF MINNESOTA"
	elif v['Organization Name'] == "UNIVERSITY OF MISSOURI COLUMBIA": v['Organization Name'] = "UNIVERSITY OF MISSOURI-COLUMBIA"
	elif v['Organization Name'] == "UNIVERSITY OF TEXAS SW MED CTR/DALLAS": v['Organization Name'] = "UNIVERSITY OF TEXAS DALLAS"
	elif v['Organization Name'] == "UNIVERSITY OF TEXAS AUSTIN": v['Organization Name'] = "UNIVERSITY OF TEXAS, AUSTIN"
	elif v['Organization Name'] == "UNIVERSITY OF VIRGINIA CHARLOTTESVILLE": v['Organization Name'] = "UNIVERSITY OF VIRGINIA"
	elif v['Organization Name'] == "UNIVERSITY OF WISCONSIN MADISON": v['Organization Name'] = "UNIVERSITY OF WISCONSIN-MADISON"
	elif v['Organization Name'] == "UNIVERSITY OF TEXAS MD ANDERSON CAN CTR": v['Organization Name'] = "UT MD ANDERSON CANCER CTR"
	elif v['Organization Name'] == "VANDERBILT UNIVERSITY": v['Organization Name'] = "VANDERBILT UNIVERSITY MED CTR"
	elif v['Organization Name'] == "WEILL MEDICAL COLLEGE OF CORNELL UNIV": v['Organization Name'] = "WEILL MEDICAL COLL OF CORNELL UNIV"
	elif v['Organization Name'] == "ALBERT EINSTEIN COL OF MED(See YESHIVA UNIV)": v['Organization Name'] = "YESHIVA UNIVERSITY"
	else: pass

fieldnames = ('Organization Name', 'ORG_CITY', 'ORG_STATE/ORG_COUNTRY', 'FY12', 'FY13', 'Institution type')

writer = csv.DictWriter(w, fieldnames=fieldnames )

headers = dict( (n,n) for n in fieldnames )

writer.writerow(headers)

for y, x in enumerate(list_all_orgs):
	writer.writerow( { 'Organization Name':x['Organization Name'], 'ORG_CITY':x['ORG_CITY'], 'ORG_STATE/ORG_COUNTRY':x['ORG_STATE/ORG_COUNTRY'], 'FY12':x['FY12'], 'FY13':x['FY13'], 'Institution type':x['Institution type']})

print "Finished"