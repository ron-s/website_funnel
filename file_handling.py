import csv


# read tab-delimited file
with open('tab_delim.tsv','rb') as filein:
    read = csv.reader(filein, delimiter='\t')
    filecontents = [line for line in read]

# write comma-delimited file (comma is the default delimiter)
with open('comma_delim.csv','wb') as fileout:
    write = csv.writer(fileout, quotechar='')
    write.writerows(filecontents)

    