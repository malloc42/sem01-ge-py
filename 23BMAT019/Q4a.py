ch = input("Enter a letter or number or special character: ")

if ((ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z")):
    print(ch, "is a letter.")

elif (ch >= "0" and ch <= "9"):
    print(ch, "is a number.")

else:
    print(ch, "is a special character.")
