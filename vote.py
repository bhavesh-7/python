name = input("Enter your name: ")
age = int(input("Enter your age: "))
x=18-age
if (age>=18):
    print("Congratulations! "+name+" You're Eligible to vote.")
else:
    print("Sorry "+name+", you're not eligible to vote.")
    print("you need to wait",x,"years to vote")
