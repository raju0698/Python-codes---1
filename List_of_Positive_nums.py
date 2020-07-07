input_string = input("Enter a list elements separated by space ")
print("\n")
userList = input_string.split()
print("user list is ", userList)
i = 0
for num in userList:
    # checking condition
    if num >= 0:
        print(num, end=" ")
        i += 1