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
	elif v['Organization Name'] == "YESHIVA UNIVERSITY": v['Organization Name'] = "ALBERT EINSTEIN COL OF MED(See YESHIVA UNIV)"
	elif v['Organization Name'] == "WEILL MEDICAL COLL OF CORNELL UNIV": v['Organization Name'] = "WEILL MEDICAL COLLEGE OF CORNELL UNIV"
	elif v['Organization Name'] == "VANDERBILT UNIVERSITY MED CTR": v['Organization Name'] = "VANDERBILT UNIVERSITY"
	elif v['Organization Name'] == "UT MD ANDERSON CANCER CTR": v['Organization Name'] = "UNIVERSITY OF TEXAS MD ANDERSON CAN CTR"
	elif v['Organization Name'] == "UNIVERSITY OF WISCONSIN-MADISON": v['Organization Name'] = "UNIVERSITY OF WISCONSIN MADISON"
	elif v['Organization Name'] == "UNIVERSITY OF VIRGINIA": v['Organization Name'] = "UNIVERSITY OF VIRGINIA CHARLOTTESVILLE"
	elif v['Organization Name'] == "UNIVERSITY OF TEXAS, AUSTIN": v['Organization Name'] = "UNIVERSITY OF TEXAS AUSTIN"
	elif v['Organization Name'] == "UNIVERSITY OF TEXAS DALLAS": v['Organization Name'] = "UNIVERSITY OF TEXAS SW MED CTR/DALLAS"
	elif v['Organization Name'] == "UNIVERSITY OF MISSOURI-COLUMBIA": v['Organization Name'] = "UNIVERSITY OF MISSOURI COLUMBIA"
	elif v['Organization Name'] == "UNIVERSITY OF MINNESOTA": v['Organization Name'] = "UNIVERSITY OF MINNESOTA TWIN CITIES"
	elif v['Organization Name'] == "UNIVERSITY OF MICHIGAN": v['Organization Name'] = "UNIVERSITY OF MICHIGAN AT ANN ARBOR"
	elif v['Organization Name'] == "UNIVERSITY OF MAINE ORONO": v['Organization Name'] = "UNIVERSITY OF MAINE"
	elif v['Organization Name'] == "UNIVERSITY OF LOUISVILLE RES FDN": v['Organization Name'] = "UNIVERSITY OF LOUISVILLE"
	elif v['Organization Name'] == "UNIVERSITY OF GEORGIA": v['Organization Name'] = "UNIVERSITY OF GEORGIA (UGA)"
	elif v['Organization Name'] == "UNIVERSITY OF CONNECTICUT SCH OF MED/DNT": v['Organization Name'] = "UNIVERSITY OF CONNECTICUT HEALTH SCIENCE CENTER"
	elif v['Organization Name'] == "UNIVERSITY OF COLORADO": v['Organization Name'] = "UNIVERSITY OF COLORADO AT BOULDER"
	elif v['Organization Name'] == "UNIVERSITY OF CALIFORNIA": v['Organization Name'] = "UNIVERSITY OF CALIFORNIA SAN DIEGO"
	elif v['Organization Name'] == "UNIVERSITY OF ARKANSAS AT LITTLE ROCK": v['Organization Name'] = "UNIVERSITY OF ARKANSAS MED SCIS LTL ROCK"
	elif v['Organization Name'] == "UNIV OF NORTH CAROLINA CHAPEL HILL": v['Organization Name'] = "UNIVERSITY OF NORTH CAROLINA CHAPEL HILL"
	elif v['Organization Name'] == "TEXAS A&M UNIVERSITY HEALTH SCIENCE CTR": v['Organization Name'] = "TEXAS A&M UNIVERSITY SYSTEM"
	elif v['Organization Name'] == "TEMPLE UNIV OF THE COMMONWEALTH": v['Organization Name'] = "TEMPLE UNIVERSITY"
	elif v['Organization Name'] == "STATE UNIVERSITY OF NY,BINGHAMTON": v['Organization Name'] = "STATE UNIVERSITY NEW YORK BINGHAMTON"
	elif v['Organization Name'] == "STATE UNIVERSITY OF NEW YORK AT BUFFALO": v['Organization Name'] = "S. U. N. Y. COLLEGE AT BUFFALO "
	elif v['Organization Name'] == "STANFORD UNIVERSITY": v['Organization Name'] = "STANFORD"
	elif v['Organization Name'] == "ST. LUKE'S-ROOSEVELT INST FOR HLTH SCIS": v['Organization Name'] = "ST. LUKE'S-ROOSEVELT HOSPITAL"
	elif v['Organization Name'] == "ST. JOSEPH'S HOSPITAL AND MEDICAL CENTER": v['Organization Name'] = "ST. JOSEPH'S HOSPITAL"
	elif v['Organization Name'] == "SLOAN-KETTERING INST CAN RES": v['Organization Name'] = "SLOAN-KETTERING INSTITUTE FOR CANCER RES"
	elif v['Organization Name'] == "RUTGERS THE STATE UNIV OF NJ CAMDEN": v['Organization Name'] = "RUTGERS THE ST UNIV OF NJ NEW BRUNSWICK"
	elif v['Organization Name'] == "RUTGERS THE STATE UNIV OF NJ NEWARK": v['Organization Name'] = "RUTGERS THE ST UNIV OF NJ NEW BRUNSWICK"
	elif v['Organization Name'] == "RUTGERS BIOMEDICAL/HEALTH SCIENCES-RBHS": v['Organization Name'] = "RUTGERS THE ST UNIV OF NJ NEW BRUNSWICK"
	elif v['Organization Name'] == "RBHS-NEW JERSEY MEDICAL SCHOOL": v['Organization Name'] = "UNIV OF MEDICINE &DENTISTRY OF NEW JERSEY"
	elif v['Organization Name'] == "RBHS-SCHOOL OF PUBLIC HEALTH": v['Organization Name'] = "UNIV OF MEDICINE &DENTISTRY OF NEW JERSEY"
	elif v['Organization Name'] == "RBHS-ROBERT WOOD JOHNSON MEDICAL SCHOOL": v['Organization Name'] = "UNIV OF MEDICINE &DENTISTRY OF NEW JERSEY"
	elif v['Organization Name'] == "RBHS-SCHOOL/ HEALTH RELATED PROFESSIONS": v['Organization Name'] = "UNIV OF MEDICINE &DENTISTRY OF NEW JERSEY"
	elif v['Organization Name'] == "RBHS -CANCER INSTITUTE OF NEW JERSEY": v['Organization Name'] = "UNIV OF MEDICINE &DENTISTRY OF NEW JERSEY"
	elif v['Organization Name'] == "RBHS-SCHOOL OF DENTAL MEDICINE": v['Organization Name'] = "UNIV OF MEDICINE &DENTISTRY OF NEW JERSEY"
	elif v['Organization Name'] == "PHOENIX BIOSYSTEM, INC.": v['Organization Name'] = "PHOENIX BIOSYSTEMS, INC."
	elif v['Organization Name'] == "Organization Name - Copy of Worldwide2013": v['Organization Name'] = "Organization Name - Indirect costs worksheet"
	elif v['Organization Name'] == "OREGON HEALTH & SCIENCE UNIVERSITY": v['Organization Name'] = "OREGON HEALTH AND SCIENCE UNIVERSITY"
	elif v['Organization Name'] == "NORTHSHORE UNIVERSITY HEALTHSYSTEM": v['Organization Name'] = "NORTHSHORE UNIVERSITY HEALTHSYSTEM*"
	elif v['Organization Name'] == "NORTHERN CALIFORNIA INSTITUTE/RES/EDU": v['Organization Name'] = "NORTHERN CALIFORNIA INSTITUTE RES & EDUC"
	elif v['Organization Name'] == "National Disease Research Interchange": v['Organization Name'] = "NATIONAL DISEASE RESEARCH INTERCHANGE"
	elif v['Organization Name'] == "MCLEAN HOSPITAL": v['Organization Name'] = "MC LEAN HOSPITAL (BELMONT, MA)"
	elif v['Organization Name'] == "MAYO CLINIC ROCHESTER": v['Organization Name'] = "MAYO CLINIC"
	elif v['Organization Name'] == "LURIE CHILDREN'S HOSPITAL OF CHICAGO": v['Organization Name'] = "CHILDREN'S MEMORIAL HOSPITAL (CHICAGO)"
	elif v['Organization Name'] == "LUDWIG INSTITUTE  FOR CANCER RES  LTD": v['Organization Name'] = "LUDWIG INSTITUTE FOR CANCER RESEARCH"
	elif v['Organization Name'] == "LOUISIANA STATE UNIV-UNIV OF NEW ORLEANS": v['Organization Name'] = "LOUISIANA STATE UNIV HSC NEW ORLEANS"
	elif v['Organization Name'] == "HEALTHPARTNERS INSTITUTE": v['Organization Name'] = "HEALTHPARTNERS RESEARCH FOUNDATION"
	elif v['Organization Name'] == "HARVARD UNIVERSITY (SCH OF PUBLIC HLTH)": v['Organization Name'] = "HARVARD UNIVERSITY SCHOOL OF PUBLIC HEALTH"
	elif v['Organization Name'] == "HARVARD UNIVERSITY (MEDICAL SCHOOL)": v['Organization Name'] = "HARVARD UNIVERSITY MEDICAL SCHOOL"
	elif v['Organization Name'] == "GUTTMACHER INSTITUTE": v['Organization Name'] = "ALAN GUTTMACHER INSTITUTE"
	elif v['Organization Name'] == "GEISINGER CLINIC": v['Organization Name'] = "WEIS CENTER FOR RESEARCH-GEISINGER CLINC"
	elif v['Organization Name'] == "FRED HUTCHINSON CAN RES CTR": v['Organization Name'] = "FRED HUTCHINSON CANCER RESEARCH CENTER"
	elif v['Organization Name'] == "DANA-FARBER CANCER INST": v['Organization Name'] = "DANA-FARBER CANCER INSTITUTE"
	elif v['Organization Name'] == "CORNELL UNIVERSITY": v['Organization Name'] = "CORNELL UNIVERSITY ITHACA"
	elif v['Organization Name'] == "COLUMBIA UNIV NEW YORK MORNINGSIDE": v['Organization Name'] = "COLUMBIA UNIVIVERSITY IN THE CITY OF NEW YORK"
	elif v['Organization Name'] == "COLORADO STATE UNIVERSITY": v['Organization Name'] = "COLORADO STATE UNIVERSITY-FORT COLLINS"
	elif v['Organization Name'] == "CLEVELAND CLINIC LERNER COM-CWRU": v['Organization Name'] = "CLEVELAND CLINIC LERNER COL/MED-CWRU"
	elif v['Organization Name'] == "CLARK UNIVERSITY (WORCESTER, MA)": v['Organization Name'] = "CLARK UNIVERSITY "
	elif v['Organization Name'] == "CINCINNATI CHILDRENS HOSP MED CTR": v['Organization Name'] = "CHILDREN'S HOSPITAL MEDICAL CENTER CINCI"
	elif v['Organization Name'] == "CHILDREN'S RESEARCH INSTITUTE": v['Organization Name'] = "CHILDREN'S NATIONAL MEDICAL CENTER"
	elif v['Organization Name'] == "CHILDREN'S HOSPITAL OF LOS ANGELES": v['Organization Name'] = "CHILDREN'S HOSPITAL LOS ANGELES"
	elif v['Organization Name'] == "CHILDREN'S HOSPITAL CORPORATION": v['Organization Name'] = "CHILDREN'S HOSPITAL BOSTON"
	elif v['Organization Name'] == "CHILDREN'S HOSP OF PHILADELPHIA": v['Organization Name'] = "CHILDRENS HOSPITAL OF PHILADELPHIA"
	elif v['Organization Name'] == "CALIFORNIA POLY STATE U SAN LUIS OBISPO": v['Organization Name'] = "CALIFORNIA POLY STATE U SAN LOUIS OBISPO"
	elif v['Organization Name'] == "BOWLING GREEN STATE UNIVERSITY": v['Organization Name'] = "BOWLING GREEN STATE UNIV BOWLING GREEN"
	elif v['Organization Name'] == "BOSTON UNIVERSITY MEDICAL CAMPUS": v['Organization Name'] = "BOSTON UNIVERSITY"
	elif v['Organization Name'] == "BOSTON UNIVERSITY (CHARLES RIVER CAMPUS)": v['Organization Name'] = "BOSTON UNIVERSITY"
	else: pass

fieldnames = ('Organization Name','Direct Cost', 'Indirect Cost', 'Funding')

writer = csv.DictWriter(w, fieldnames=fieldnames )

headers = dict( (n,n) for n in fieldnames )

writer.writerow(headers)

for y, x in enumerate(list_all_orgs):
	writer.writerow( { 'Organization Name':x['Organization Name'], 'Direct Cost':x['Direct Cost'], 'Indirect Cost':x['Indirect Cost'], 'Funding':x['Funding']})

print "Finished"