import os
import csv


budget1 = os.path.join("raw_data", "budget_data_1.csv")
budget2 = os.path.join("raw_data", "budget_data_2.csv")
monthcount1 = []
monthcount2 = []
dollar1 = 0
dollar2 = 0
maxdollar1 = 0
maxdollar2 = 0
mindollar1 = 0
mindollar2 = 0
maxmonth1 = 0
minmonth1 = 0
maxmonth2 = 0
minmonth2 = 0
#set(listname) = unique values

with open(budget1, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    next(csvfile)
    for row in csvreader:
        monthcount1.append(row[0])
        dollar1 = int(dollar1) + int(row[1])
        if maxdollar1 > int(row[1]):
            maxdollar1
            maxmonth1
        else:
            maxdollar1 = int(row[1])
            maxmonth1 = (row[0])
        if mindollar1 < int(row[1]):
            mindollar1
            minmonth1
        else: 
            mindollar1 = int(row[1])
            minmonth1 = (row[0])

            
    avgr1 = dollar1 / int(len(monthcount1))


with open(budget2, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    next(csvfile)
    for row in csvreader:
        monthcount2.append(row[0])
        dollar2 = int(dollar2) + int(row[1])
        if maxdollar2 > int(row[1]):
            maxdollar2
            maxmonth2
        else:
            maxdollar2 = int(row[1])
            maxmonth2 = (row[0])
        if mindollar2 < int(row[1]):
            mindollar2
            minmonth2
        else: 
            mindollar2 = int(row[1])
            minmonth2 = (row[0])
    avgr2 = dollar2 / int(len(monthcount2))

print("Financial Analysis")
print("----------------------------------------------------")        
print("for first file, the number of months are: " + str(len(monthcount1)))
print("The total dollar value in file 1 is " + str(dollar1))
print("The average value of file 1 dollar value is " + str(avgr1))
print("The max increase of file 1 is " + str(maxdollar1) + "and it occured in " + str(maxmonth1))
print("The min increase of file 1 is " + str(mindollar1) + "and it occured in " + str(minmonth1))
print("----------------------------------------------------")      
print("for second file, the number of months are: " + str(len(monthcount2)))
print("The total dollar value in file 2 is " + str(dollar2))
print("The average value of file 2 dollar value is " + str(avgr2))
print("The max increase of file 2 is " + str(maxdollar2) + "and it occured in " + str(maxmonth2))
print("The min increase of file 2 is " + str(mindollar2) + "and it occured in " + str(minmonth2))

with open('output.txt','w', newline = '') as outfile:
    print("Financial Analysis", file = outfile)
    print("----------------------------------------------------", file = outfile)        
    print("for first file, the number of months are: " + str(len(monthcount1)), file = outfile)
    print("The total dollar value in file 1 is " + str(dollar1), file = outfile)
    print("The average value of file 1 dollar value is " + str(avgr1), file = outfile)
    print("The max increase of file 1 is " + str(maxdollar1) + "and it occured in " + str(maxmonth1), file = outfile)
    print("The min increase of file 1 is " + str(mindollar1) + "and it occured in " + str(minmonth1), file = outfile)
    print("----------------------------------------------------", file = outfile)      
    print("for second file, the number of months are: " + str(len(monthcount2)), file = outfile)
    print("The total dollar value in file 2 is " + str(dollar2), file = outfile)
    print("The average value of file 2 dollar value is " + str(avgr2), file = outfile)
    print("The max increase of file 2 is " + str(maxdollar2) + "and it occured in " + str(maxmonth2), file = outfile)
    print("The min increase of file 2 is " + str(mindollar2) + "and it occured in " + str(minmonth2), file = outfile)