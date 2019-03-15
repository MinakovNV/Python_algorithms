import sqlite3

class Account:

    def __init__(self, account_name, validity, owner, manager):
        self.account_name = account_name
        self.validity = validity
        self.owner = owner
        self.manager = manager

    def getAccName(self):
        return self.__account_name

    def getOwner(self):
        return self.__owner

    def setOwner(self, owner):
        self.__owner = owner

    def getManager(self):
        return self.__manager

    def setManager(self, manager):
        self.__manager = manager


class Client(Account):

    def __init__(self, account_name, validity, owner, manager, f_name, l_name, balance, credit_amount):
        Account.__init__(account_name, validity, owner, manager)
        self.__f_name = f_name
        self.__l_name = l_name
        self.__balance = balance
        self.__credit_amount = credit_amount

    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
        self.__balance = balance

    def setCreditAmount(self, credit_amount):
        self.__credit_amount = credit_amount

    def getManagerName(self):
        return self.__f_name + " " + self.__l_name

    def setManagerName(self, f_name, l_name):
        self.__l_name = l_name
        self.__f_name = f_name

    def withDraw(self):
        print("HZ")

class Manager(Account):

    def __init__(self, account_name, validity, owner, manager, f_name, l_name, position):
        Account.__init__(account_name, validity, owner, manager)
        self.__f_name = f_name
        self.__l_name = l_name
        self.__position = position

    def getNames(self):
        return self.__f_name + " " + self.__l_name

    def getPosition(self):
        return self.__position

    def setPosition(self, position):
        self.__position = position

    def changeValidity(self, validity):
        self.validity = validity

    def deleteAccount(self):
        Account.__init__(None, None, None, None)

clients = []
managers = []


clients.append(Client('Minakov111', 10, 1, 2, 'Minakov', 'Nikita', 20000, 2))
clients.append(Client('Niyazova222', 10, 2, 3, 'Niyazova', 'Dilnaz', 34000, 5))
clients.append(Client('Sazontov333', 10, 3, 4, 'Sazontov', 'Andrew', 14500, 3))


con = sqlite3.connect("myDB.db")

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Account (AccName TEXT, Validity INTEGER, Owner_id INTEGER, Manager_id INTEGER)")

cur.execute("INSERT INTO Account VALUES\
            ('Minakov111', 10, 01, 01), ('Niyazova222', 10, 02, 01),\
            ('Sazontov333', 10, 03, 01)")

s = cur.execute("SELECT AccName, Validity, Owner_id, Manager_id FROM Account")

con.commit()

con.close()

