# 5a Find the frequency of a character in a string.
user_str = input("Enter a string: ")

for i in user_str:
    f = user_str.count(i)
    print(i + " - " + str(f))

