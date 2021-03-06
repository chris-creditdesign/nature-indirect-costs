# Nature indirect costs

Working process to combine and examine large excel files.

## Process NIH Reporter data

### Extract the relevant Excel sheet

From `Copy of Worldwide2013.xls` save Sheet 2 only as `nih-reporter.xlsx`.

### Convert from Excel to csv

Install [csvkit](http://csvkit.readthedocs.org/en/0.9.0/index.html).

Convert the excel file into a csv containing just the first four columns, representing `Organization Name`, `Direct Cost`, `Indirect Cost` and `Funding`.

	in2csv excel/nih-reporter.xlsx | csvcut -c 1,2,3,4 > csv/nih-reporter.csv
	
### Remove duplicate and discrepancies

Account for duplicate names for the same organization and make organization names match the names used in `Indirect costs worksheet.xlsx`.

	python python/remove_duplicate_names.py csv/nih-reporter.csv csv/nih-reporter-cleaned.csv

### Sum up all of the grants

Run `sum_costs.py` to create a new csv file with all of the grants for each organization summed

	python python/sum_costs.py csv/nih-reporter-cleaned.csv csv/nih-reporter-summed.csv

There should now just be one entry for each organization. You can check the amount of lines in each file with.

	wc -l csv/nih-reporter-summed.csv

	wc -l csv/nih-reporter.csv

You can now remove the working files.

	rm csv/nih-reporter.csv

	rm csv/nih-reporter-cleaned.csv

## Process Indirect Costs data

### Extract the relevant Excel sheet

Copy Sheet 1 from `Indirect costs worksheet.xlsx` to a new work book `indirect-costs.xlsx`

### Convert form Excel to csv

Convert the excel file into a csv containing just the first four columns, representing `ORG_NAME`, `ORG_CITY`, `ORG_STATE/ORG_COUNTRY`, `FY12`, `FY13` and `Institution type`.

	in2csv excel/indirect-costs.xlsx | csvcut -c 1,2,3,4,5,6 > csv/indirect-costs.csv

### Replace the header

	cat csv/indirect-costs.csv | sed "1 d" > csv/headerless.csv

	echo "Organization Name,ORG_CITY,ORG_STATE/ORG_COUNTRY,FY12,FY13,Institution type" | cat - csv/headerless.csv > csv/indirect-costs.csv

	rm csv/headerless.csv

## Join the two csv files

Merge the two csv files using `Organization Name` as the column name on which to join.

	csvjoin -c 'Organization Name' csv/indirect-costs.csv csv/nih-reporter-summed.csv > csv/joined.csv

## Calculate the indirect costs

Run `calculate_indirect_costs.py` to add a new column `Calculated Indirect cost` to show `Indirect Cost` as a percentage of `Direct Cost`.

	python python/calculate_indirect_costs.py csv/joined.csv csv/indirect-costs-calculated.csv

remove the working file `joined.csv`.

	rm csv/joined.csv

## Work out number of discrepancies between datasets

	python python/missing_entries.py csv/indirect-costs.csv csv/nih-reporter-summed.csv csv/discrepancies.csv

	wc -l csv/discrepancies.csv

## Restore the organizations that have no 2013 grant data

	python python/restore_missining_orgs.py csv/indirect-costs.csv csv/discrepancies.csv csv/restore.csv

	csvstack csv/indirect-costs-calculated.csv csv/restore.csv > csv/indirect-costs-calculated-combined.csv


## Examine the data

Examine the first ten lines of just `Organization Name`,`ORG_STATE/ORG_COUNTRY`,`FY13`,`Funding`,`Calculated Indirect cost`.

	csvcut -c 'Organization Name','ORG_STATE/ORG_COUNTRY','FY13','Funding','Calculated Indirect cost' csv/indirect-costs-calculated.csv | csvlook | head

Present statistics from the file.

	csvcut -c 'Organization Name','ORG_STATE/ORG_COUNTRY','FY13','Funding','Calculated Indirect cost' csv/indirect-costs-calculated.csv | csvstat

Look at the institutions that received the most funding

	csvcut -c 'Organization Name','ORG_STATE/ORG_COUNTRY','FY13','Funding','Calculated Indirect cost' csv/indirect-costs-calculated.csv | csvsort -c 'Funding' -r | csvlook | head

Look at the institution with the highest indirect costs.

	csvcut -c 'Organization Name','ORG_STATE/ORG_COUNTRY','FY13','Funding','Calculated Indirect cost' csv/indirect-costs-calculated.csv | csvsort -c 'Calculated Indirect cost' -r | csvlook | head

Highest funding in New York.

	csvcut -c 'Organization Name','ORG_STATE/ORG_COUNTRY','FY13','Funding','Calculated Indirect cost' csv/indirect-costs-calculated.csv | csvgrep -c 'ORG_STATE/ORG_COUNTRY' -m 'NEW YORK' | csvsort -c 'Funding' -r | csvlook | head

Highest funding in California.

	csvcut -c 'Organization Name','ORG_STATE/ORG_COUNTRY','FY13','Funding','Calculated Indirect cost' csv/indirect-costs-calculated.csv | csvgrep -c 'ORG_STATE/ORG_COUNTRY' -m 'CALIFORNIA' | csvsort -c 'Funding' -r | csvlook | head


Check that MASSACHUSETTS GENERAL HOSPITAL is correct

	csvcut -c 'Organization Name','ORG_STATE/ORG_COUNTRY','FY13','Funding','Calculated Indirect cost' csv/indirect-costs-calculated.csv | csvgrep -c 'Organization Name' -m 'MASSACHUSETTS GENERAL HOSPITAL' | csvlook


Check that OHIO STATE UNIVERSITY is correct

	csvcut -c 'Organization Name','ORG_STATE/ORG_COUNTRY','FY13','Funding','Calculated Indirect cost' csv/indirect-costs-calculated.csv | csvgrep -c 'Organization Name' -m 'OHIO STATE UNIVERSITY' | csvlook

Experimental technique to sum columns 

First convert from commas to pipes to account for commas in names

	csvformat -D "|" test.csv test_pipe.csv

Then work out the total for column 4 in this instance. 

	sed '1d' test_pipe.csv | awk -F"|" '{print $4; x+=$4}END{print "Total, " x}'

Perhaps this could be printed to a new file or concatenated to the end?
