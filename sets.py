first_set = set(input("Enter your text with numbers: "))
second_set = set(input("Enter your text with numbers: "))

same_letter = set([element for element in first_set.intersection(second_set) if element.isalpha()])
print(type(same_letter), same_letter)
numbers = set([element for element in first_set.symmetric_difference(second_set) if element.isdigit()])
print(type(numbers), numbers)



# first_set = {4, 5, 7, 14, 23}
# second_set = {5, 9, 15}
# third_set = {14, 9, 11}
# #first_set |= second_set | third_set # |= all sets elements together
# #first_set &= second_set | third_set # &= match the elements if they are repeats in all sets
# first_set -= second_set #- third_set
# first_set ^= second_set #^ third_set
# print(type(first_set),(first_set))
