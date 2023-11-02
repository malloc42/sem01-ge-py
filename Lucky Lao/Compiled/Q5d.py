# 5d Remove all occurrences of a character from a string
user_str = input("Enter a string: ")
user_chr = input("Enter the character to remove: ")

new_str = user_str.replace(user_chr, "")
print("The new string is:\n" + new_str)
