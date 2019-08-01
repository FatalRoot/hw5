#!/usr/bin/ python
'''
Python v3.7
July 31, 2019
Homework 5 - Kassandra Bethune
hw5.py
'''

infile = r"C:\Users\Kass\Documents\todo.txt"
# open and read todo.txt
with open(infile, 'r+') as todo_file:
    lines = todo_file.readlines()

#create dict to store data from for loop
task_dict = {}

for line in lines:
    task = line.split(",")[0].strip()
    priority = line.split(",")[1].strip()
    task_dict[task] = priority

#provide user options
while(True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()#adding a new line
    #Choice 1: show current items in file
    if (strChoice.strip() == '1'):
        for key, val in task_dict.items():
            print(key, val)
    #Choice 2: add a new item to the list/table
    elif(strChoice.strip() == '2'):
        new_key = input("Enter a new task name: ")
        new_value = input("Enter the new task's priority from low to high: ")
        task_dict[new_key] = new_value
    #Choice 3: remove an item from list/Table
    elif(strChoice == '3'):
        remove_key = input("Enter the task name to remove: ")
        if remove_key in task_dict.keys():
            del task_dict[remove_key]
        else:
            input("Your task is not in the dictionary, please try again: ")
    #Choice 4: save tasks to todo file
    elif(strChoice == '4'):
        with open(infile, 'r+') as fh:
            fh.writelines(task_dict)
            for key, value in task_dict.items():
                fh.writelines('{},{}\n'.format(key, value))
    #Choice 5: end program
    elif (strChoice == '5'):
        break
        todo_file.close()