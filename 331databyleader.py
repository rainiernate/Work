import csv

table331 = []
tableleader = []

sum1 = 0

with open('331data.csv', 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        table331.append(row)
        
int(table331)


        ##table331.append(row)
##
##with open('dept_leaders.csv', 'rt') as g:
##    reader = csv.reader(g)
##    for row in reader:
##        tableleader.append(row)






