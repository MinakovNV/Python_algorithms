#Minakov Nikita Csse1709R EndTerm

import sqlite3


# ___________________Task 1
class Account:

    def __init__(self, accname, owner):
        self.__accName = accname
        self.__owner = owner

    def getAccName(self):
        return self.__accName

    def getOwner(self):
        return self.__owner

    def setOwner(self, owner):
        self.__owner = owner

    def getManager(self):
        return self.__manager

    def setManager(self, manager):
        self.__manager = manager


class Client:
    balance = 100000

    def __init__(self, fname, lname):
        self.__fname  = fname
        self.__lname = lname

    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
        self.__balance = balance

    def setCreditAmount(self, crAm):
        self.__crAm = crAm

    def getManagerName(self):
        return self.__fname + " " + self.__lname

    def setManagerName(self, lname, fname):
        self.__lname = lname
        self.__fname = fname

    def withDraw(self):
        if (self.balance -self.__crAm) > 0:
            return self.balance - self.__crAm
        else:
            return "Not enough balance"

class Manager:

    validity = 100  # days until closing an account

    def __init__(self, fname, lname):
        self.__fname = fname
        self.__lname = lname

    def getNames(self):
        return self.__fname + " " + self.__lname

    def getPosition(self):
        return self.__position

    def setPosition(self, position):
        self.__position = position

    def changeValidity(self, validity):
        self.__validity = validity

    def deleteAccount(self):
        return "Account was deleted(No)"

# ___________________Task 2

con = sqlite3.connect("Endterm.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Client(fname text, s_name text, balance integer, credit_amount integer)")

cur.execute("CREATE TABLE IF NOT EXISTS Account(acc_name text, validity integer, owner integer, manager integer)")

cur.execute("CREATE TABLE IF NOT EXISTS Manager(fname text, s_name text, position text)")



# ___________________Task 3

cur.execute("INSERT INTO Account VALUES\
            ('Minakov111', 100, 01, 01)")
cur.execute("INSERT INTO Client VALUES\
            ('Minakov', 'Nikita', 3900, 20)")
cur.execute("INSERT INTO Manager VALUES\
            ('Minakova', 'Weronika', 'DartVaider')")

s = cur.execute("SELECT acc_name, validity, owner, manager FROM Account")

con.commit()
con.close()

# ___________________Task 4

Client1 = Client("Minakov", "Nikita")
Client2 = Client("Niyazova", "Dilnaz")

Manager1 = Manager("Minakova", "Weronika")
Manager2 = Manager("Sazontov", "Andrew")

Account1 = Account("Minakov888", 1001)
Account2 = Account("Niyazova111", 1002)
Account3 = Account("Sazontov333", 1002)


zzz = int(input("Input Balance:"))
Client1.setBalance(zzz)
print("Balance:", Client1.getBalance())

Client2.setManagerName("Ravil", "Brankov")

print("Your manager name: ", Client2.getManagerName())

Manager1.setPosition("Boss")

print("Possition of 1st Manager", Manager1.getPosition())

print("Name of 1st account:", Account1.getAccName())

Account3.setOwner("Minakov")
print("Owner of 3rd account", Account3.getOwner())

Client2.setCreditAmount(2000)

print("WithDraw function:", Client2.withDraw())