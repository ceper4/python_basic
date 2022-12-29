######################################################### sum of numbers from a to b
# def func_one(a, b):
#     temp_var = 0
#     if a > b:
#         for i in range(b, a + 1, 1):
#             temp_var += i
#     else:
#         for i in range(a, b + 1, 1):
#             temp_var += i
#     return temp_var
#
# start = int(input("Enter first number: "))
# end = int(input("Enter second number: "))
# result = func_one(start, end)
# print(result)
######################################################### seconds convertation
# seconds = int(input("Enter how many seconds you want to convert: "))
# def convert_seconds(seconds):
#     days = int(seconds / 86400)
#     hours = int(seconds % 86400 / 3600)
#     minutes = int(seconds % 86400 % 3600/ 60)
#     seconds = int(seconds % 86400 % 3600 % 60)
#     return f'{days} : {hours} : {minutes} :{seconds}'
# print(convert_seconds(seconds))
######################################################### for-cicle
# list = [1, 2, 3, 4, 5, 6]
# a = 0
# for item in list:
#     if item !=0:
#         a += item
# print(a)
######################################################### with while
# numb = int(input("Enter your numbers: "))
# sum = 0
# while numb !=0:
#     a = numb % 10
#     sum = sum + a
#     numb = numb // 10
# print (sum)
######################################################### recursion
listsum = [1, 3, 5, 7, 9, 5]
def summ(number, index=0):
    if index >= len(number):
        return 0
    else:
        return number[index] + summ(number, index+1)
recursion =summ(listsum)
print(recursion)
######################################################### fibonacci numb
# def fibo(n):
#     if n > 2:
#         return (fibo(n-1) + fibo(n-2))
#     else:
#         return 1
# print (fibo(6))
# print (fibo(7))
# print (fibo(8))
# print (fibo(9))
