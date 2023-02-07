#1 sortOut Dublicate and print
list1=[1,2,2,4,5,6,7,8,9,7,14,5,10,11,12,13,14,11,]
list2=[]
list3=[]
for i in list1:
    if i not in list2:
        list2.append(i)
    elif i not in list3:
        list3.append(i)
print(list1)
print(list2)
print(list3)
#2
sum=0
for i in list1:
    sum=sum+i
print("Total: ",sum)
#3
list4=[]
for x in list1:
    for y in list3:
        if x==y:
            list4.append(x)
print(list4)
#4
s1=input("Enter String 1: ")
s2=input("Enter String 2: ")
print("String 1: ",s1)
print("String 2: ",s2)
print("Concantated String: ",s1+s2)
print("SubString: ",s1[1:4])
#5
car=["Supra","Civic","Corolla","AMG","M3"]
bikes=["ZX-10R","H2","V4","StreetFighter","Katana"]
vehicles=car+bikes
print("Vehicles    : ",vehicles)
print("Cars        : ",car)
print("Bikes       : ",bikes)
car.remove("AMG")
car.remove("M3")
print("Updated Car : ",car)
#6
myTuple=("Apple","Mango","Chikoo","")
