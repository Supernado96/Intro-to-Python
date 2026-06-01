x = int(input("Enter the cost price: "))
y = int(input("Enter the selling price: "))
if y > x:
    print("You have made a profit of", str(y-x)+".")
elif x > y:
    print("You have made a loss of", str(x-y)+".")
else:
    print("No profit or loss.")