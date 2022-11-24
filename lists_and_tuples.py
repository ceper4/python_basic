# First task code:
# line = (input("Please enter a sentence: ").split(" "))
# print (f"{type(line)=}, {line=}")
# print(f"So, every third word in your line is: {line[2::3]}")

# Second task code:
list_1 = [1, 2.1, "f", "2", 3, "1", 18, "df"]
list_2 = []
for elem in (list_1):
    if type(elem) == float:
        list_2.append(elem)
    elif type(elem) == int and elem % 2 == 0:
        list_2.append(elem)
    elif type(elem) == int and elem % 2 !=0:
        list_2.append(elem**2)
    elif type(elem) == str and elem.isdigit():
        list_2.append(int(elem)*3)
    else:
        list_2.append(-1)
print(list_1)
print(list_2)
