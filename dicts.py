ASCII_dict = {element: chr(element) for element in range(1,128)}
print(type(ASCII_dict))
print (ASCII_dict)
#
# try:
#     code_word = input("Enter your password word: ").lower()
# except:
#     print(code_word)
# print(code_word)
# try:
#     password = int(input("Enter a number from 1 to 26: "))
#     if password%26 == 0:
#         password = input("you entered invalid value. please, enter only integer number")
# except:
#     print(password)
#
# alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
#          'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
#          't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
# code_numb = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
#          11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's',
#          20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
# increase = {}
# for key, value in code_numb.items():
#     for ix, exc in alphabet.items():
#         if ix == code_numb[key]:
#             if alphabet[ix]+password > 26:
#                 increase[(alphabet[ix]+password) % 26] = code_numb[key]
#             else:
#                 increase[alphabet[ix]+password] = code_numb[key]
# print(increase)
#
# for el in code_word:
#     for key, value in increase.items():
#         if increase[key] == el:
#             print(code_numb[key], end="")
