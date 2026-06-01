n = int(input("Enter the number which you want to find the sum of: "))
sum = 0
for i in range(1, n+1):
    sum+=i
print("The sum is", sum)


sum = 0
for i in range(1, n+1):
    if i%2 == 0:
     sum+=i
    else: 
       continue
print("The sum of the even numbers is", sum)


sum = 0
for i in range(1, n+1):
    if i%3 == 0:
     sum+=i
    else: 
       continue
print("The sum of the odd numbers is", sum)