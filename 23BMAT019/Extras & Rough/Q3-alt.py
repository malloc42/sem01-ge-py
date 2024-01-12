def pyra(n):
    for i in range(1, n, 2):
        m = int((n-i+1)/2)  # To adjust the cursor
        for k in range(1, m):
            print(" ", end=" ")
        for j in range(1, i+1):
            print("*", end=" ")
        print()

pyra(5)

def rpyra(n):
    for i in range(n-1, 0, -2):
        m = int((n-i+1)/2)  # To adjust the cursor
        print("\t"*int(n/3), end="")
        for k in range(1, m):
            print(" ", end=" ")
        
        for j in range(1, i+1):
            print("*", end=" ")
        print()

rpyra(10)

