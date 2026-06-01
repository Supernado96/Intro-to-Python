a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

for i in range(a, b+1):
    if i > 1:
        for c in range(2, i):
            if i % c == 0:
                break
        else:
            print(i)