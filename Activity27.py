n = int(input("Enter a number: "))
sum = 0

for i in range(1, n+1):
    if sum<50:
       sum+=i
    else:
        break

print("The sum, stopping at 50 is", sum)