# Nature indirect costs

Working process to combine excel files.

### Extract the relevant Excel sheet

From `Copy of Worldwide2013.xls` save Sheet 2 only as `nih-reporter.xlsx`.

### Convert form Excel to csv

Install [csvkit](http://csvkit.readthedocs.org/en/0.9.0/index.html).

Convert the excel file into a csv containing just the first four columns, representing Organization Name, Direct Cost, Indirect Cost and Funding.

	in2csv excel/nih-reporter.xlsx | csvcut -c 1,2,3,4 > csv/nih-reporter.csv
	
### Sum up all of the grants

Run `sum_costs.py` to create a new csv file with all of the grants for each organization summed

	python python/sum_costs.py csv/nih-reporter.csv csv/nih-reporter-summed.csv

There should now just be one entry for each organization. You can check the amount of lines in each file with.

	wc -l csv/nih-reporter-summed.csv

	wc -l csv/nih-reporter.csv

###

Copy Sheet 1 from `Indirect costs worksheet.xlsx` to a new work book 'indirect-costs.xlsx'