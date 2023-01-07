# def decor(func_to_decor):
#     print("Tomato")
#     def warapper():
#         print("Cheese")
#         func_to_decor()
#     print("Meat")
#     return warapper
#
# @decor
# def main_func():
#     print("Bread")
#
# main_func()
def main_decor(func_to_decor):
    print("Sandwich is:")
    def warapper():
        print("Meat")
        func_to_decor()
        print("Bread")

    print("Tomato")

    return warapper

@main_decor
def main_func():
    print("Cheese")


main_func()