letter = input("Enter a letter: ")

if (letter >= "a" and letter <= "z"):
    print(letter, "is in lowercase.")

elif (letter >= "A" and letter <= "Z"):
    print(letter, "is in UPPERCASE.")

else:
    print(letter, "is not a letter.")
