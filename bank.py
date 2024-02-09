a='the rocket came back from mars'
# b=list(a)
# c=['a','e','i','o','u']
# for i in a:

# a=[('hari',21)]

# import time
# def time11():
#     end=time.time()

# globel start=time.time()
# print('Q1. What is the capital of India')
# print("(a)Delhi    (b)Karachi     (c)Lucknow     (d)Chennai")
# n=input("Enter the option:- ")
# if n=="a":

#     print("(a) is the correct option")
# else:
#     print("The option is wrong")

# print('Q1. What is the capital of USA')
# print("(a)Texas    (b)Washington DC     (c)California     (d)Los Angles")
# n=input("Enter the option:- ")
# if n=="b":
#     print("(b) is the correct option")
# else:
#     print("The option is wrong")

# print('Q1. What is the capital of UK')
# print("(a)London    (b)Spain     (c)England     (d)Brooklyn")
# n=input("Enter the option:- ")
# if n=="c":
#     print("(c) is the correct option")
# else:
#     print("The option is wrong")

class Bank_account():
    def __init__(self):
        self.amount=0
    def deposit(self,Amount1):
        self.amount+=Amount1
        print("Amount successfully deposited")
    def withdraw(self,Amount1):
        if(self.amount-Amount1>=500):
            self.amount-=Amount1
            print("Amount successfully withdrawn")
        else:
            print("Insufficeint balance. \nYou have to keep atleast Rs.500 in your account")
    def display(self):
        print(f"Your bank balance is: {self.amount} ")

a=Bank_account()
while True:
    print("1.Deposit  2.Withdraw  3.Display  4.Exit")
    b=int(input("Enter your choice: "))
    if b==1:
        try:
            Amount1=float(input("Enter amount to be deposited: "))
            a.deposit(Amount1)
        except:
            (print("Please enter a number"))
    elif b==2:
        try:
            Amount1=float(input("Enter amount to be withdrawn: "))
            a.withdraw(Amount1)
        except:
            (print("Please enter a number"))
    elif b==3:
        a.display()
    elif b==4:
        exit()
    else:
        print("You have inserted wrong value")