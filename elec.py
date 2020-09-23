import csv
import math
from os import listdir

HISTORY_DIR = 'historic/'

def electionfiles():
    return [HISTORY_DIR + f for f in sorted(listdir(HISTORY_DIR), key = int)]

def indexofparty(partyrow, party):
    return math.floor(partyrow.index(party)/2)*3+2

def resultsline(partyrow, totalsrow):
    republicanindex = indexofparty(partyrow, 'Republican')
    actual = int(totalsrow[republicanindex+2])
    proportional = math.floor(int(totalsrow[1])*float(totalsrow[republicanindex+1]))
    margin = actual - proportional
    return [str(actual), str(proportional), margin]
    

results = []
for electionfile in electionfiles():
    with open(electionfile, newline='') as csvfile:
        data = list(csv.reader(csvfile, delimiter=','))
        year = electionfile[electionfile.rindex('/')+1:]
        candidate = data[0][data[0].index('Republican')-1]
        results.append([year, candidate] + resultsline(data[0], data[-1]))

with open('results.csv', 'w', newline='\n') as resultsfile:
    writer = csv.writer(resultsfile, delimiter=',')
    writer.writerow(['year', 'republican candidate', 'actual', 'proportional', 'margin'])
    writer.writerows(results)
