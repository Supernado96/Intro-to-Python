print("Enter the marks obtained in 5 subjects: ")
one = int(input())
two =int(input())
three=int(input())
four=int(input())
five=int(input())


total = one + two + three + four + five
avg = total/5


if avg >=91 and avg <=100:
    print("A")
elif avg >=81 and avg <91:
    print("B")
elif avg >= 71 and avg < 81:
    print("C")
elif avg >= 61 and avg<71:
    print("D")
elif avg >=51 and avg < 61:
    print("F")
else:
    print("F-")