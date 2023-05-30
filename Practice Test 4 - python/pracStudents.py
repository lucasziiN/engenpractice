print ("Lucas")

import csv
import matplotlib.pyplot as plot

csvfile = open('C:\\Users\\lucas\\Downloads\\comp103-15a.txt', 'r')

csvreader = csv.reader(csvfile)

fsenStudentsList = []
counter = 0
for row in csvreader:
    
    if row[3] == 'FSEN':
        fsenStudentsList.append(row)
        if row[2] == 'BE(HONS)':
            print(row[1])
        
print(fsenStudentsList)


print('Number of FSEN Engineering students: ' + str(len(fsenStudentsList)))

#print(counter)

def Failing(student_grade):
    if student_grade == 'D' or student_grade =='E' or student_grade =='F' or student_grade =='IC':
        return True
    else:
        return False
    
for i in fsenStudentsList:
    if Failing(i[4]) == True:
        counter += 1

print('Number of passing students: ' + str((len(fsenStudentsList) - counter)))
print('Number of failing students: ' + str(counter))

grade_dict = {'A+': 0 , 'A': 0, 'A-': 0, 'B+': 0, 'B': 0, 'B-': 0, 'C+': 0, 'C': 0, 'C-': 0, 
        'P': 0, 'RP': 0, 'D': 0, 'E': 0, 'F': 0, 'IC': 0}

for i in fsenStudentsList:
    grade = i[4]
    if grade in grade_dict:
        grade_dict[grade] += 1
    
print(grade_dict)

grades = list(grade_dict.keys())
num_students = list(grade_dict.values())
plot.bar(grades, num_students)
plot.xlabel('Grades')
plot.ylabel('Number of students')
plot.show()

csvfile.close()