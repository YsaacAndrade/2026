user = input("Word: ")
p = []
print(f"This word has {len(user)}")
if user[::-1] == user:
    print("Is a palindrome")
else:
    print("Is not a palindrome")
