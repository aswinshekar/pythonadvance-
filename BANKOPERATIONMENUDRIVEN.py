###bank operations


class Account():
    def _init_(self):
        self.accnmbr=int(input("enter ac nmbr:"))
        self.accname=input("enter name")
        self.balance=int(input("enter balance"))

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))

        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        self.balance = self.balance + amount
        print("Amount deposited:", amount)

    def showbalance(self):
        print("Balance:", self.balance)


l=[]
while(1):
    print("banking operations")
    print("1.create an account")
    print("2.withdraw")
    print("3.deposit")
    print("4.show balance")
    print("5.exit")

    ch=int(input("enter your choice:"))
    if ch==1:
        a=Account()
        l.append(a)
        print(l)
    elif ch==2:
        n=int(input("enter acc numbr:"))
        for i in l:
            if i.accnmbr==n:
                i.withdraw()
                i.showbalance()
                break
        else:
            print("account doesnt exist")

    elif ch==3:
        n = int(input("enter acc numbr:"))
        for i in l:
            if i.accnmbr == n:
                i.deposit()
                i.showbalance()
                break
        else:
            print("account doesnt exist")

    elif ch==4:
        n = int(input("enter acc numbr:"))
        for i in l:
            if i.accnmbr == n:
                i.showbalance()
        else:
            print("account doesnt exist")

    else:
        exit()



