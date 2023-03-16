def area(n):
    if n == 1:
        l=int(input("Enter Length: "))
        b=int(input("Enter Breadth: "))
        print("Area of Rectangle: ",l*b)
    elif n == 2:
        h=int(input("Enter Height: "))
        b=int(input("Enter Base: "))
        print("Area of Tringle: ",0.5*b*h)
    elif n == 3:
        r=int(input("Enter Radius: "))
        pi=3.14
        print("Area of Circle: ",round(pi*r*r,3))
select=int(input("Select Shape to Calculate Area: \n1.Rectangle\n2.Trinangle\n3.Cricle\n-->"))
area(select)        
        
