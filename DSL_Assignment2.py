# SPPU DSL Assignment 2 ( Subject code: 210246 )

from typing import Counter


print("*****************Welcome!*****************")
marks_list = [67, '', 99, 100, 'AB', 68, 70, 90, 68, 83, 'NA', 55, 76, 60, 88]
print('The list of marks scored by students in subject FDS are as follows:')
print(marks_list)


def menu():
    print('1. The average score of the class.')
    print('2. Highest score and lowest score of the class.')
    print('3. Count of students who were absent for the test.')
    print('4. Marks with highest frequency.')
    print('5. Close menu.')
    choice = int(
        input('Enter appropriate number to execute the following task:'))

    if choice == 1:
        print('**** Average score of the class ****')
        averageScore()
        print("******************************************")
        menu()

    elif choice == 2:
        print('**** Highest and lowest score of the class ****')
        highestScore()
        lowestScore()
        print("******************************************")
        menu()

    elif choice == 3:
        print("**** Count of students who were absent ****")
        absentCount()
        print("******************************************")
        menu()

    elif choice == 4:
        print("Marks with highest frequency: ", end="")
        freqHigh()
        print("******************************************")
        menu()

    elif choice == 5:
        exit
    else:
        print("Bro, I can only handle 5 things. Read the menu again!")
        menu()


# Definition of functions used above


def averageScore():
    count = avg = total = 0
    n = len(marks_list)
    print('Strength of class is: ', n)
    for i in marks_list:
        if type(i) == type(" "):          # Don't use isalpha() here.
            # Here, count is the no of students who were absent.
            count += 1
        else:
            total = total+i
    avg = total/(n-count)
    print('Average is: ', avg)


def highestScore():
    max = count = 0
    for i in marks_list:
        if type(i) == type(" "):           # Don't use isalpha() here.
            count += 1
        elif i > max:
            max = i
    print('Highest Score achieved is: ', max)


def lowestScore():
    # assumed min value to be max and will change it by comparing with list of marks
    min = 100
    count = 0
    for i in marks_list:
        if type(i) == type(" "):
            count += 1
        elif i < min:
            min = i
    print("Lowest Score achieved is: ", min)


def absentCount():
    count = 0
    for i in marks_list:
        if type(i) == type(" "):
            count += 1
    print("No. of absent students: ", count)


def freqHigh():
    max = 0
    res = marks_list[0]
    for i in marks_list:
        freq = marks_list.count(i)
        if freq > max:
            max = freq
            res = i
    print(str(res))
    print(max)


menu()
