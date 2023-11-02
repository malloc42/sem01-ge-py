# 5b Replace a character by another character in a string
user_str = input("Enter a string: ")
chr_1 = input("Enter a character to replace: ")
chr_2 = input("Enter the new character: ")

new_str = user_str.replace(chr_1, chr_2)
print("The new string is:\n" + new_str)
