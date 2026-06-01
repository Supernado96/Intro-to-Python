Total = int(input("Enter the total money required: "))
hundred = Total//100
fifty = (Total%100)//50
ten = (((Total%100)%50)//10)
print(f"You need {hundred} 100 rupee notes, {fifty} 50 rupee notes, and {ten} ten rupee notes.")