"""
 "  Minakov Nikita CSSE 1709R
 "  Lab 04 Python
"""


from random import *


# Task 1
print("Task_1\n\n")
try:
    def Printer(x1, x2):
        print("Solution: x1 = ", x1, "\nx2 = ", x2)
    def Printer(x1):
        print("Solution: x1 = x2 = ", x1)
    def Printer():
        print("Discriminant < 0, no real solutions")

    def D_positive(D, a, b, c):
        x1 = (-b+D**(1/2))/(2*a)
        x2 = (-b-D**(1/2))/(2*a)
        print("Solution: x1 = ", x1, "x2 = ", x2)

    def D_zero(D, a, b, c):
        x1 = (-b+D**(1/2))/(2*a)
        print("Solution: x1 = x2 = ", x1)

    def D_negative(D):
        print("Discriminant < 0, no real solutions")



    print("Equation: ax^2+bx+с=0, a!=0")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

    D = b*b - 4*a*c
    if(D>0):
        D_positive(D, a, b, c)
    elif (D==0):
        D_zero(D, a, b, c)
    else:
        D_negative(D)

except:
    print("Invalid input")



# Task 2
print("\n\nTask_2\n\n")
try:
    def Printer():
        print("Your random matrix:")
        for i in range(0, sq_matrix):
            for j in range(0, sq_matrix):
                print(Matrix[i][j], end=" ")
            print("")

    def Sum():
        sum_main_diag = 0
        sum_conter_diag = 0
        for i in range(0, sq_matrix):
            for j in range(0, sq_matrix):
                if (i == j):
                    sum_main_diag = Matrix[i][j] + sum_main_diag

        for i in range(0, row_num):
            sum_conter_diag = Matrix[i][row_num-i-1] + sum_conter_diag

        print("Sum on main diagonal = ", sum_main_diag)
        print("Sum on counter diagonal = ", sum_conter_diag)


    row_num = int(input("Input size of matrix:(rows)"))
    column_num = int(input("Input size of matrix:(columns)"))

    if(row_num > column_num):
        sq_matrix = row_num
        print("Your matrix isn't square. Number of columns will be changed to number of rows")
    elif (row_num < column_num):
        sq_matrix = column_num
        print("Your matrix isn't square. Number of rows will be changed to number of columns")
    else:
        sq_matrix = row_num
        print("Your matrix is square. Everything all right")

    Matrix = [[0 for x in range(sq_matrix)] for y in range(sq_matrix)]

    for i in range(0, sq_matrix):
        for j in range(0, sq_matrix):
            Matrix[i][j] = randint(1, 9)
    Printer()
    Sum()
except:
    print("Invalid input")



# Task 3
print("\n\nTask_3\n\n")

try:
    def Reverse_sentence():
        print("Your sentence in reverse form:")
        arr = []
        for i in range(len(str)):
            arr.append(str[i])
        arr.reverse()
        for i in range(len(str)):
            print(arr[i], sep="", end="")

    str = str(input("Input any sentence:\n"))

    Reverse_sentence()
except:
    print("Some strange error! What have you done, that broke my programme")



# Task 4
print("\n\nTask_4\n\n")
try:
    def Dict_d():
        key_d = [x for x in range(1, pairs_num+1)]
        value_d = [x ** 3 for x in range(1, pairs_num+1)]
        dict_d = dict(zip(key_d, value_d))
        print(dict_d)

    pairs_num = int(input("Input number of pairs:"))
    print("Dictionary with numbers as keys and values in 3rd degree of these numbers")
    Dict_d()
    
except:
    print("Invalid input")


# Task 5
print("\n\nTask_5\n\n")

try:
    def Final_list(c, b):
        aa = c + b
        print("This is the result->", aa)

    def Indexing_():
        index = a.index(max(a))
        return index

    def Random_my():
        for i in range(0, elememts_num):
            a[i] = randint(-10, 10)

    def Printer():
        print("List of random elements->", a)

    def Right_():
        index = Indexing_()
        b = a[0:index+1]
        c = a[index+1:elememts_num]
        Final_list(c, b)

    def Left_():
        index = Indexing_()
        b = a[0:index]
        c = a[index:elememts_num]
        Final_list(c, b)

    elememts_num = int(input("Input number of elements:\n"))
    a = [x for x in range(0, elememts_num)]

    Random_my()
    Printer()

    direction = input("Choose the direction: right/left\n")
    direction = direction.lower()

    if direction == "right":
        Right_()
    elif direction == "left":
        Left_()
    else:
        print("Invalid input_1")
except:
    print("Invalid input_2")


# Task 6
print("\n\nTask_6\n\n")
print("Program that defines whether this number is power of 2 or not:\n")
try:
    def Myfunction(n):
        if (number**(1/n) == 2):
            print("Yes")
        else:
            return Myfunction(n-1)

    number = int(input("Input any number:\n"))

    n = 100
    Myfunction(n)
except:
    print("No")

# Task 7
print("\n\nTask_7\n\n")
try:
    def Random_():
        for i in range(0, length):
            a.append(randint(10, 99))

    def Printer():
        print("The max number will be:")
        for i in range(0, length):
            print(a[i], sep="", end="")

    def P_Solver():
        a.sort(reverse=True)

    print("Program that returns a maximum number that is combined from numbers (digits) in the random list")
    length = int(input("Input number of elements:\n"))
    a = []
    Random_()

    print("List of random elements:\n", a)
    P_Solver()
    Printer()

except:
    print("\nInvalid input")
finally:
    print("\nThat's all! Thanks for checking:)")
