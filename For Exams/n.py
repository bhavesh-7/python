name=input("Enter Name: ")
mk=[]
sum=0.0
avg=0.0
print()
for i in range(3):
    print("Enter Marks for Subject",i+1,": ")
    mk.append(int(input()))
    sum=sum+mk[i]
avg=sum/3
print("Name                 : ",name)
for i in range(len(mk)):
    print("Marks for subject",i+1,": ",mk[i])
if avg>=80:
    print("Grade: A")
elif avg>=70:
    print("Grade: B")
elif avg>=60:
    print("Grade: C")
elif avg>=35:
    print("Grade: D")
else:
    print("Fail")
