def decor(func_to_decor):
    print("Tomato")
    def warapper():
        print("Cheese")
        func_to_decor()
    print("Meat")
    return warapper

@decor
def main_func():
    print("Bread")

main_func()