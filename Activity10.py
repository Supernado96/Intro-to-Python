num = int(input("Enter an integer: "))
if num == 15:
    print("The number = 15")
if num > 15:
    if num %2 == 0:
        print("The number is greater than 15 and is even.")
    else:
        print("The number is greater than 15 and is odd.")
elif num < 15:
    if num > 0:
        print("The number is less than 15 and is positive.")
        if num %2 == 0:
            print("The number is also even.")
        else:
            print("The number is also odd.")
    if num < 0:
        print("The number is negative and less than 15.")
        if num %2 == 0:
            print("The number is also even.")
        else:
            print("The number is also odd.")
    if num == 0:
        print("The number is 0 and is even.")