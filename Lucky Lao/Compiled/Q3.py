def pyra(n):
    for i in range(1, n+1):
        l_space = " "*(n-i)
        row_stars = "*"*(2*i-1)
        print(l_space + row_stars)

def rpyra(n):
    for i in range(n, 0, -1):
        extra_l_space = " "*(2*n)
        l_space = " "*(n-i)
        row_stars = "*"*(2*i-1)
        print(extra_l_space + l_space + row_stars)

n = int(input("Enter the number of rows: "))
pyra(n)
rpyra(n)