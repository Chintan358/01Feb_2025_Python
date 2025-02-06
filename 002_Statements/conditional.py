
# age = 17

# if age>=18 :
#     print("Elegeble for voting")
# else :
#     print("Not elegeble for voting")


a = 100
b = 100
c = 50

# if a>b:
#     if a>c:
#         print("A is greater")
#     else:
#         print("C is greater")
# else:
#     if b>c:
#         print("B is greater")
#     else:
#         print("C is greater")

# if a>b and a>c:
#     print("A is greater")
# elif b>a and b>c:
#     print("B is greater")
# elif c>a and c>b:
#     print("C is greater")
# else:
#     print("any two are same")


marks = int(input("Enter marks : "))

if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=70 and marks<90:
    print("Grade B")
elif marks>=50 and marks<70:
    print("Grade C")
elif marks>=35 and marks<50:
    print("Grade D")
elif marks>=0 and marks<35:
    print("Grade F")
else:
    print("Invalid input : enter marks between 0 to 100")