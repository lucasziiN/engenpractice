import numpy
import random

names = ["Tim Elphick", "Tim Elphick", "Jemma Konig", "Jemma Konig", "Eibe Frank", "Eibe Frank", "Eibe Frank", "Eibe Frank", "Tim Elphick", "Tim Elphick", "Tim Elphick", "Eden Pohipi", "Eden Pohipi", "Eden Pohipi", "Vimal Kumar", "Vimal Kumar", "Vimal Kumar", "Vimal Kumar", "Debby Dada", "Debby Dada", "Debby Dada", "Debby Dada"]

print(names)
print('The length of this list is ' + str(len(names)))

names_set = set(names)

print(names_set)
print('The number of unique names in this list is: ' + str(len(names_set)))

file = open("C:\\Users\\lucas\\Downloads\\unique_names.txt", 'w')
for i in names_set:
    file.write(i + "\n")
file.close()

average_entry = len(names) / len(names_set)
average_entry = format(average_entry, ".3f")
print(str(average_entry))


letter_cost = 1.07
envelope_box_cost = 11

cost = letter_cost * len(names_set) + envelope_box_cost
cost_per_entrant = cost/len(names_set)
cost_per_entrant = format(cost_per_entrant, ".2f")
print("The cost of posting an advertising letter to each entrant is $" + str(cost_per_entrant))

user_choice = int(input("Do you want to (1) look up an entrant by name or (2) look up an entrant by entry number? " ))

if user_choice == 1:
    name = input("Enter a name: ")
    if name in names_set:
        print(str(name) + " found")
    else:
        print(str(name) + " not found")
elif user_choice == 2:
    num = int(input("Enter entry number: "))
    if num>= 0 and num < len(names_set):
        print(names[num])
    else:
        print("This is not a valid entrant number")

random_number = random.randint(0, len(names) - 1)
print(str(names[random_number]) + ' has won the competition!')

names_set.remove(names[random_number])

for i in names_set:
    print(str(i) + ' did not win ')
    