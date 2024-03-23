# Age = 12
# Gender = 'F'

# if Age>100 or Age < 0:
#     print("Invalid Age....")

# elif Age >= 10 and Age <= 25:
#     if Gender == 'F':
#         print("You Are Eligible Scolorship")
#     else:
#         if Age >= 15:
#             print("You Are Eligible Scolorship")
#         else:
#             print("You Are Not Eligible Scolorship Because of age....")

# else:
#     print("You Are Not Eligible Scolorship Because of age....")


#----------------------------------------------------------------

# day = 1

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid Day")

#----------------------------------------------------------------
# -----------While Lop---------
# x = 3
# while x <= 7:
#     print(x)
#     x += 1

#---------For Loop-----------

# for i in range(1,8,2):
#     print(i)

# n = int(input("Enter a Number: "))
# sum = 1
# for i in range(1,n+1):
#     sum *= i

# print(sum)


for i in range(2,201):
    if i % 7 == 0:
        print(i)