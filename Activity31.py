string = str(input("Enter a string: "))
char = str(input("Enter a character: "))

i = 0
count = 0

while i < len(string):
    if string[i] == char:
        count+=1
    i+=1

print(f'The number of instances "{char}" has occured in "{string}" is {count}.')