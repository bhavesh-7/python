name = input("Enter your name: ")
print("Enter your marks- ")
p = int(input("Physics: "))
c = int(input("Chemistry: "))
m = int(input("Maths: "))
per = (p+c+m)/3
print("Name       : "+name)
print("Percentage : ",per)
if per>90:
    print("Grade      : O+")
elif per>80:
    print("Grade      : O")
elif per>70:
    print("Grade      : A+")
elif per>60:
    print("Grade      : A")
elif per>50:
    print("Grade      : B")
elif per>40:
    print("Grade      : C")
else:
    print("Grade      : F")
