# file = open("sample.txt", "w")
# try:
    # file.write("Hello, Gabriel!!")
# finally:
    # file.close()

with open("sample.txt", "w") as file:
    file.write("Hello, Gabriel")