n = int(input("Enter an integer greater than 1: "))

flag = 0

if (n > 1):
    for i in range(2, n):
        if n % i == 0:
            flag = 1

else:
    flag = 1

if (flag == 0):
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")
