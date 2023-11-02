str_1 = input("Enter first string: ")
str_2 = input("Enter second string: ")
n = int(input("Enter n: "))

if (n > min(len(str_1), len(str_2)) or n < 1):
    print("Please enter a valid value for n")
    exit()

str_3 = str_2[:n] + str_1[n:]
str_4 = str_1[:n] + str_2[n:]

print("The new first string is:\n" + str_3)
print("The new second string is:\n" + str_4)
