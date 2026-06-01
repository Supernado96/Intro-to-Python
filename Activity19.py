a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if a%b == 0:
    print("The first number is divisible by the second number.")
elif b%a == 0:
    print("The second number is divisible by the first number.")
else:
    print("They are not divisible.")


c = int(input("Enter a number: "))
i = 1
while True:
    if c%i == 0:
        print("Your number ", c,"is divisible by", i)
    i+=1