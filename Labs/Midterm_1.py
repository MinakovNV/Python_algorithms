from random import*

#Task1


try:
    def Funck_year():
        if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
            print("False")
        else:
            print("True")

    year = int(input("Input a year:"))
    Funck_year()
except:
    print("Invalid input")



#Task2

f_name = str(input("Input first name:"))
s_name = str(input("Input Second name:"))
l_name = str(input("Input Last name:"))

list_num = (1, 2, 3, 4, 5)
list_city = ("Alamty 111", "Astana 222", "Warsawa 333", "Moscow 444", "Sorento 555")
dict_base = dict(zip(list_num, list_city))

rand_num = randint(1, 5)


print(l_name," " ,f_name[0],".",  s_name[0],". ", "->", dict_base.get(rand_num), sep="")



#Task3
month= ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
num = int(input("Input number between 1-12"))

if num>13 and num<0:
    print("Invalid number:\n")
else:
    print(month[num-1])


#Task4

money = int(input("Money:\n"))
year = int(input("Years:\n"))


for i in range(0, year):
    money = money*1.17

print(money)



#Task 5

def IntToByte(x):
    n = "" if x > 0 else "0"
    while x > 0:
        y = str(x % 2)
        n = y + n
        x = int(x / 2)
    print(n)


num = int(input("Input a number:"))

IntToByte(num)
