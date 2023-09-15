import getpass
import string
import os


users = [ '330033','343535']
pins = ['1234','2222']
amounts = [10000,7000]
counts = 0
count=0
flag = 0

print("----------WELCOME TO SBI---------")

while True:
    user = input("Enter Account Number: ")
    if user in users:
        if user == users[0]:
            n = 0
        elif user == users[1]:
            n = 1
        break
    else:
        print("------INVALID ACCOUNT NUMBER-----")

while count<1:
    pin = input("Enter PIN: ")
    if pin.isdigit():
        if user == '330033':
            if pin == pins[0]:
                print("Login Sucessfull")
                counts += 1
                count=1
        elif user == '343535':
            if pin == pins[1]:
                print("Login Sucessfull")
                counts += 1
                count=1
        else :
            print("invalid pin")

while True:
    if counts > 0 :
        print("CHOOSE OPTION")
        option = input("A. Check Balance\nB. Withdraw Ammount\n------> ")
        option = option.lower()
        if option == 'a':
            print("Account Number ", users[n], ", have ", amounts[n]," INR in your Bank Account.")
        elif option == 'b':
            cash_out = int(input("Enter Amount to withdraw: "))
            if amounts[n]<cash_out:
                print("You have insufficient Balance!")
            elif cash_out%10 != 0:
                print("ATM only have rs. 500 notes inside")
            else:
                amounts[n] = amounts[n]-cash_out;
                print("Transaction Successfull.\nYour new Balance is ",amounts[n],"INR.")
        flag = int(input("Do you want to continue? 1=yes,0=no --> "))
        if flag == 1:
            continue
        else:
            print("Bye Bye, Hope to see you soon!")
            break
    else:
        print("Something bad happened, Try again in some time.")
            
        


