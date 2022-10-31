username = input("Please tell me your name ")
print(username)
print(username.strip())
hello_username = f"Hello {username.strip().title()}, nice to meet you!"
print(hello_username)
print(len(username.strip()))
print(username.strip()[::-1])