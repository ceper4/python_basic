numb_comp_1 = 3 != 5

print ("numb_comp_1 is:", numb_comp_1)

numb_comp_2 = 5 == 5
numb_comp_3 = 5 >= 5
numb_comp_4 = 5 <= 5

print ("numb_comp_2 is:", numb_comp_2)
print ("numb_comp_3 is:", numb_comp_3)
print ("numb_comp_4 is:", numb_comp_4)

first = True and True or False
second = True or True or False
third = True or True and False
fourth = True and True and not False
fifth = True or not True and False

print ("first is:", first)
print ("second is:", second)
print ("third is:", third)
print ("fourth is:", fourth)
print ("fifth is:", fifth)

print (bool(None) == bool(7))
print (bool() == bool(10-1))
print (bool(True or False) == bool(print("whatever")))
print (bool(type(None)) == bool(id(None)))