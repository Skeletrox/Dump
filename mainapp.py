#!/usr/bin/python

acclist = []

class Account:
    __accno = 0
    __name = ""
    __type = ""
    __balance = 0.0
    def __init__ (self):
       self. __accno = int(input('Enter Account number: '))
       self.__name = input('Enter User name: ')
       self. __type = input('Enter Account type: ')
       self.__balance = float(input('Enter initial balance: '))

    def withdraw (self, x):
        if (self.__balance >= x):
            self.__balance -= x;
            print ('Withdrawal Successful')
            return True
        else:
            print ('Insufficient funds to complete transaction')
            return False

    def deposit (self, x):
        self.__balance += x;
        print ('Deposit Successful')

    def display(self):
        print ('Account number: ' + str(self.__accno))
        print ('Name: ' + self.__name)
        print ('Account type: ' + self.__type)
        print ('Available balance: ' + str(self.__balance))

    def accret(self):
        return self.__accno

    def balret(self):
        return self.__balance

def Transfer (a, b, x):
    if (a.withdraw(x)):
        b.deposit(x)
    else:
        print ('Transaction Failed')

#Main program here!


print ("""Welcome to the banking system built on Python
Use the following options to perform the following functions:
    1. Make an account
    2. Deposit into an account
    3. Withdraw from an account
    4. Transfer between accounts
    5. Show account
    Anything else to exit
    """)
while (True):
    choice = int(input('Enter Choice:\t'))
    if (choice == 1):
        a = Account()
        acclist.append(a)
    elif (choice == 2):
        num = int(input ('Enter account number to deposit into: '))
        for i in range (0, len(acclist)):
            if (acclist[i].accret() == num):
                num = float(input('Enter amount to deposit: '))
                acclist[i].deposit(num)
                break
        if (i > len(acclist)):
            print ('404')
    elif (choice == 3):
        num = int(input ('Enter account number to withdraw from: '))
        for i in range (0, len(acclist)):
            if (acclist[i].accret() == num):
                num = float(input('Enter amount to withdraw: '))
                acclist[i].withdraw(num)
                break
        if (i > len(acclist)):
            print ('404')
    elif (choice == 4):
        num = int(input('Enter account number to transfer from: '))
        num2 = int(input('Enter account number to transfer to: '))
        flag1, flag2 = False, False
        for i in range (0, len(acclist)):
            if(acclist[i].accret() == num):
                x = i
                flag1 = True
            if(acclist[i].accret() == num2):
                y = i
                flag2 = True
            if (flag1 & flag2):
                break
        if (flag1 & flag2):
            Transfer(acclist[x], acclist[y])
        else:
            print ('Verify account numbers again')
    elif (choice == 5):
        num = int(input('Enter account to display: '))
        for i in range(0, len(acclist)):
            if(acclist[i].accret() == num):
                acclist[i].display()
                break
        if (i > len(acclist)):
            print ('404')
    else:
        print ('Bye')
        break
#print (acclist)                //For debug purposes
