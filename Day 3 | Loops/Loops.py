# 1. Print the Sum Of N Natural Numbers
# N = int(input("Enter any number: "))
# sum = 0
# for i in range(1,N+1):
#     sum = sum + i
# print(sum)
    

# 2. Find The Factors Of a Number
# N  = int(input("Enter a Number:- "))
# M  = int(input("Enter a Number:- "))
# Min = N
# if N > M:
#     Min = M
# # print(Min)

# MaxD = N

# for i in range(2,Min+1):
#     if N % i == 0 and M % i == 0:
#         # print("Answer:-",i)
#         MaxD = i


# print(MaxD)



# 3. Count Of a Digit

# n = 154623
# count = 0
# while n > 0:
#     n = n // 10
#     count += 1

# print(count)



#4. Plaindrome Number
for i in range(100,10001):
    n = i
    n2 = n
    reverse = 0
    while n > 0:
        r = n % 10
        reverse = reverse * 10 + r
        n = n // 10

    if reverse == n2:
        print(n2,"Yes it is Palindrome")
