name = input("Enter your name: ")
print("Enter your marks- ")
p = int(input("Physics: "))
c = int(input("Chemistry: "))
m = int(input("Maths: "))
cs = int(input("Computer Science: "))
per = (p+c+m+cs)/4
print("Name       : "+name)
print("Percentage : ",per,"%")
