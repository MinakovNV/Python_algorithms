"""
 "  Minakov Nikita CSSE 1709R
 "  Lab 04 Python
"""
import sys
from datetime import *
from random import *
from collections import deque, Counter
import os
import json



############################################################

# Task 1
print("Task_1\n\n")
try:
    os.chdir("Lab07/Task1")

    def Random_my():
        for i in range(0, num_numbers):
            a[i] = randint(0, 9)


    def Write_func(num_files):

        for i in range(0, num_files):
            with open('Task1_txt_' + myTxt_names[i] + '.txt', "w") as myTxt:
                Random_my()
                for j in range(0, num_numbers):
                    myTxt.write(str(a[j]))
                    myTxt.write(" ")


    def Read_func():
        for i in range(0, num_files):
            with open('Task1_txt_' + myTxt_names[i] + '.txt', "r") as myTxt:
                lines = myTxt.readline()
                lines_list = list(lines)

                for j in range(0, len(lines_list)//2):
                    lines_list.remove(" ")

                lines_list = list(map(int, lines_list))

                print("Elements of file:", lines_list)
                print("In file", myTxt_names[i] + "MyTxt.txt: Max =", max(lines_list))


                a_sum[i] = sum(lines_list)
                print("Sum in this file:", a_sum[i], "\n")
                a_sum.index(max(a_sum))
        print("The biggest file is", a_sum.index(max(a_sum))+1, ", with the sum = ", max(a_sum), )


    num_files = int(input("Input number of files:(not bigger than 10)\n"))
    num_numbers = int(input("Input number of numbers:\n"))

    a = [x for x in range(0, num_numbers)]
    a_sum = [x for x in range(0, num_numbers)]

    myTxt_names = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')

    Write_func(num_files)
    Read_func()

except:
    print("Error")


############################################################

# Task 2
print("\n\nTask_2\n\n")

try:
    os.chdir("Lab07/Task2")


    def Write_func():
        with open('Task2_txt.txt', "w") as myTxt:
            date_time = str(datetime.now())
            dd = str(date_time)
            myTxt.write("File was created in: ")
            myTxt.write(dd)


    def Write_func_plus():
        with open('Task2_txt.txt', "a+") as myTxt:
            date_time = str(datetime.now())
            dd = str(date_time)
            myTxt.write("\n")
            myTxt.write("File was edited in: ")
            myTxt.write(dd)


    def Rewrite(inp_str):
        with open('Task2_txt.txt', "a+") as myTxt:
            myTxt.write("\n")
            myTxt.write(inp_str)

            print("File was rewritten")


    def Append(inp_str):
        print("Appending text")
        with open('Task2_txt.txt', "a+") as myTxt:

            myTxt.write("\n")
            myTxt.write(inp_str)


    def Delete():
        print("Deleting file text")
        with open('Task2_txt.txt', "w") as myTxt:
            myTxt.write("")


    input_ = int(input("\nWhat do you wanna do?\n1. Rewrite\n2. Append\n3. Delete\n"))

    if input_ == 1:
        inp_str = input("Input your text:")
        Write_func()
        Rewrite(inp_str)
    elif input_ == 2:
        inp_str = input("Input your text:")
        Write_func_plus()
        Append(inp_str)
    elif input_ == 3:
        Write_func_plus()
        Delete()
    else:
        print("Invalid input")

except:
    print("Error")



############################################################

#Task 3
print("\n\nTask_3\n\n")
try:
    os.chdir("Lab07/Task3")

    def Json_read():
        with open('dict.json', "r") as maJson:
            myReadData = json.load(maJson)
            return myReadData

    glossary = Json_read()
    flag = 1

    while flag:
        word = input("\nPlease input a word:")
        word = word.lower()

        i = 0

        list_keys = []
        list_val = []
        list_final = []


        for i, j in glossary.items():
            if word in i:
                #print(i, end=", ")
                list_keys.append(i)

        len_word = len(word)

        #posessing and outputing

        ii_str = "*"

        if glossary.get(word) != None:
            list_val.append(glossary.get(word))
            old_str = ''.join(map(str, list_val))
            new_str = old_str.replace('"', '')
            new_str = new_str.replace(",", "")
            new_str = new_str.replace("'", "")
            new_str = new_str.replace("[", "")
            new_str = new_str.replace("]", "")

            new_str = new_str.replace(".", ii_str)
            list_final = new_str.split()
            print(word, ":", sep="")
            print("* ", end="")

            for i in range(0, len(new_str)):

                if new_str[i] == ii_str:

                    print("\n")

                print(new_str[i], sep="", end="")
                flag = 0

        #print(new_str)

        else:
            print("\nNo this word in dictionary!\nSuggestions:\n")
            for i in range(0, len(list_keys)):
                z = list_keys[i]
                if z[0:len_word] == word:
                    print(z)

    #print(glossary.get(word))

except:
    print("Error")



############################################################

#Task 4
print("\n\nTask_4\n\n")

try:
    os.chdir("Lab07/Task4")

    def Json_retakers_create():
        with open('Task4_Retakers.json', "w") as maJson:
            json.dump(ret, maJson)

    def Json_luckers_create():
        with open('Task4_Luckers.json', "w") as maJson:
            json.dump(luck, maJson)


    def Json_update():
        with open('Task4_Json.json', "w") as maJson:
            json.dump(list_ll, maJson)


    def Json_create():
        id_list = ("101", "102", "103", "104", "105")
        names_list = ("Minakov", "Bogdanowitcz", "Niyazova", "Bychkova", "Daineko")
        marks_list = (80, 81, 100, 95, 30)
        list_lists = (id_list, names_list, marks_list)

        with open('Task4_Json.json', "w") as maJson:
            json.dump(list_lists, maJson)

    def Json_read():
        with open('Task4_Json.json', "r") as maJson:
            myReadData = json.load(maJson)
            return myReadData

    def Output_print():
        print("ID | Student | Mark")
        for j in range(len(list_ll) + 2):
            # for j in range(3):
            print(list_ll[i][j], "|", list_ll[i + 1][j], "|", list_ll[i + 2][j])

    #Json_create()#comment this line after first compilation
    print("Comment this line after first compilation")

    myReadData = Json_read()

    list_ll = list(myReadData)

    list_id, list_name, list_mark = zip(list_ll)

    i = 0
    print("Students in your class:")
    Output_print()


    aa = int(input("\nWhat do you want?\n1. Change mark for all class\n2. Find student by ID\n3. Skip"))

    if aa == 1:
        for j in range(0, len(list_ll)+2):
            print("Input a new mark for", list_ll[i+1][j])
            mark_new = int(input())
            list_ll[i+2][j] = mark_new

        Json_update()
        print("Marks was successfully updated")
    elif aa == 2:
        id_ = int(input("Input ID:(101-105)\n"))
        id_ = id_ - 101

        print(list_ll[i][id_], "|", list_ll[i + 1][id_], "|", list_ll[i + 2][id_])
    else:
        print("Skiping")

    retake_id = ["", "", "", "", ""]
    retake_names = ["", "", "", "", ""]
    retake_mark = ["", "", "", "", ""]
    lucky_id = ["", "", "", "", ""]
    lucky_names = ["", "", "", "", ""]
    lucky_mark = ["", "", "", "", ""]
    x = 0
    xx = 0

    for j in range(0, len(list_ll)+2):
        if (list_ll[i + 2][j]<51):
            retake_id[x] = (list_ll[i][j])
            retake_names[x] = (list_ll[i + 1][j])
            retake_mark[x] = (list_ll[i + 2][j])
            x += 1

        elif (list_ll[i + 2][j] > 49):
            lucky_id[xx] = (list_ll[i][j])
            lucky_names[xx] = (list_ll[i + 1][j])
            lucky_mark[xx] = (list_ll[i + 2][j])
            xx += 1

    #print("Retakers:", retake_id, retake_names, retake_mark)
    #print("Luckers:", lucky_id, lucky_names, lucky_mark)

    ret = [retake_id, retake_names, retake_mark]
    luck = [lucky_id, lucky_names, lucky_mark]

    Json_retakers_create()
    Json_luckers_create()

except:
    print("Invalid input")

