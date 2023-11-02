n = int(input("Enter a positive number: "))

if (n > 1):
    while (n != 1):
        flag = 0
        if (n > 1):
            for i in range(2, n):
                if (n % i == 0):
                    flag = 1
        if (flag == 0):
            print(n)
        n -= 1
