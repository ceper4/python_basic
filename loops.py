letters = ""
vowels = ""
spaces = ""
capital = ""
row = input("Please enter some letters, numbers and spaces: ")

for index, letters in enumerate(row):
    try:
        if row[index].isdigit() and row[index + 1].isdigit() and row[index + 2].isdigit():
            print(f'Error! you enter three numbers in a row!')
            break
    except:
        print(f'Loop is finished without mistakes')
        continue
    if letters in "aAoOuUyYiIeE":
        vowels += letters+","
    if letters in " ":
        spaces += str(index)+",";
    if letters.isupper():
        capital += letters+","

print(f'You enter this vowels letters = {vowels} \nIndexes of spaces is = {spaces} \nCapital letters is = {capital}')

