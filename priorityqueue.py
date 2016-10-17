import csv

activities=dict()
onlyactivities=dict()
uniqueactivites=dict()
prioritylist=dict()
counter=0
serial_no=0
matchfound=0
counter2=0

fp=open('Academic _Schedule.csv','r')
reader = csv.reader(fp)


for row in reader:
    activities[serial_no]=row[0],row[1],row[2]
    serial_no+=1
serial_no=0

for i in range(activities.__len__()):
    r,r,row=activities[counter]
    onlyactivities[counter]=row
    counter+=1

uniqueactivites = set()
for dic in onlyactivities:
   for val in onlyactivities.values():
      uniqueactivites.add(val)

while uniqueactivites():
    activity=uniqueactivites
    prioritylist[]

    

