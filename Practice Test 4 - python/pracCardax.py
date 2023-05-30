import csv
import numpy as np
#today = open('C:\\Users\\lucas\\Downloads\\Today.txt', 'r')

#reader = csv.reader(today)

today = [12212, 17617, 16968, 13375, 11378, 17617, 12062, 19891, 15574, 10582, 16212,
         19800,15574,12062,19891,17617, 12222,19800,11274,10582,16212, 19800, 15574,
           12062, 19891, 17617, 19891, 11274, 12222, 19891]

people = {12212: 'in', 17617: 'out', 16968: 'in', 13375: 'in', 11378: 'in', 12062: 'in',
 19891: 'in', 15574: 'in', 10582: 'out', 16212: 'out', 19800: 'in', 12222: 'out', 11274: 'out'}


for i in today:
    print(i)

id_user = int(input('Enter a cardax number: '))

if id_user in today:
    print('%s has used the door today'% id_user)
else:
    print('%s has not used the door today' % id_user)

#for i in today:
#    if not np.isin(i, people) == 1:
#        people.append(i)

count = 0

for i in people:
    status = str(people[i])
    if status == 'in':
        print(str(i) + ' is in the building')
    else:
        print(str(i) + ' is not in the building')

print(str(len(people)) + ' people have access to the R-Block')

if id_user in today:
    print(str(id_user) + ' is a valid number' )
    for i in people:
        if people[i] == 'in':
            people[i] = 'out'
            print(str(i) + ' now is ' + people[i] + ' the building')
        else:
            people[i] = 'in'
            print(str(i) + ' now is ' + people[i] + ' the building')
else:
    print(str(id_user) + ' is unknown' )

for i in people:
    if people[i] == 'in':
        print(str(i) + ' is ' + people[i] + ' the building')
    else:
        print(str(i) + ' is ' + people[i] + ' the building')

inside = []

for i in people:
    if people[i] =='in':
        inside.append(i)

print(inside)

file = open('C:\\Users\\lucas\\Downloads\\inside.txt', 'w')
for i in inside:
    file.write(str(i) + '\n')
file.close()
