a = str(input("To enter the exam you must answer the question: Do you have a medical condition?(Y/N): "))
if a == "Y":
    print("You can enter the exam.")
else:
    atten = int(input("Enter your attendance out of a hundred: "))
    if atten >= 75:
        print("You are eligible for the exam.")
    else:
        print("You are not eligible for the exam.")