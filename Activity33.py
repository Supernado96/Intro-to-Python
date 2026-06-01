print("Right angled triangle generator")

rows = int(input("Enter the number of rows: "))

for i in range(rows):
    for x in range(i+1):
        print("* ", end = " ")
    print()