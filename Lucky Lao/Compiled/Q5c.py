# 5c Remove the first occurrence of a character from a string
user_str = input("Enter a string: ")
user_chr = input("Enter the character: ")

new_str = user_str.replace(user_chr, "", 1)
print("The new string is:\n" + new_str)
