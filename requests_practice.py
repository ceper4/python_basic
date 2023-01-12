import requests
#
#
# url = "https://jsonplaceholder.typicode.com/comments"
# my_params = {"postId": 4}
#
#
# response = requests.get(url, params=my_params)
# print(f"{response.status_code=}")
# print(f"{response.json()=}")
# url_1 = "https://jsonplaceholder.typicode.com/comments?postId=4"
# response = requests.get(url_1)
# with open("comments.txt", "w") as f:
#     f.write(response.text)


# Request the profile picture of the OP:
response = requests.get("https://www.codeitbro.com/wp-content/uploads/2020/07/funny-python-meme-27-python-is-fun.jpg")
with open("mem.jpg", "wb") as f:
    f.write(response.content)