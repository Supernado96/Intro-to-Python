print("Floyd's triangle")

n = 1

rows = int(input("Enter the number of rows as a whole number: "))

for i in range(rows):
    for x in range(i+1):
        print(n, end = " ")
        n+=1
    print()