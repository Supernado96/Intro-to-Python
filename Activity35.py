print("Diamond Generator")
rows = int(input("Enter the number of rows: "))
if rows % 2 == 0:
    midpoint = rows//2
else:
    midpoint  = rows//2 +1
space = midpoint-1
for i in range(1, midpoint+1):
    for x in range(1, space+1):
        print(end=" ")
    space-=1
    num = 1

    for x in range(2*i-1):
        print(end=str(num))
        num+=1
    print()
space =1 
for ii in range(1, midpoint):
    for x in range(1,space+1):
        print(end=" ")
    space+=1
    num =1
    for x in range(1, 2*(midpoint-ii)):
        print(end=str(num))
        num+=1
    print()