number = int(input("Enter a number: "))
temporary = number
sum = 0
while temporary > 0:
    digit = temporary % 10
    sum += digit**3
    temporary //=10

if sum == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")