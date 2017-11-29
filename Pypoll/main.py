import os
import csv

elect1 = os.path.join("raw_data", "election_data_1.csv")

candidate = {}

votercount1 = []

with open(elect1, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    next(csvfile)

    for i in csvreader:
        
        votercount1.append(i[0])
        
        if i[2] in candidate:
            candidate[(i[2])] += 1

        else: 
            candidate[(i[2])] = 1

    print("Election Results")
    print("-----------------------------------------------")
    print("Total votes = " + str(len(votercount1)))

    for key, value in candidate.items():
        
        percentage = "{:.1f}%".format(round((value / len(votercount1)),2) * 100)
        print(key, value, percentage)

    print("The winner is " + max(candidate, key=candidate.get))  

with open('output.txt','w', newline = '') as outfile:
    print("Election Results" , file = outfile)
    print("-----------------------------------------------", file = outfile)
    print("Total votes = " + str(len(votercount1)), file = outfile)

    for key, value in candidate.items():
        
        percentage = "{:.1f}%".format(round((value / len(votercount1)),2) * 100)
        print(key, value, percentage, file = outfile)

    print("The winner is " + max(candidate, key=candidate.get), file = outfile)   