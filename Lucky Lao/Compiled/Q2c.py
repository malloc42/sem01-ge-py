n = int(input("Enter a positive integer: "))

if (n >= 1):
    p = 2
    count = 0
    while (count != n):
        flag = 0        
        for i in range(2, p):
            if (p % i == 0):
                flag = 1

        if (flag == 0):
            print(p)
            count += 1
        p += 1
