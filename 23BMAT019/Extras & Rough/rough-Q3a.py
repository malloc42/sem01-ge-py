#n = int(input("Enter a number: "))
n = 10
#for i in range(1, n+1):
#    print(" "*(i-1)+"  "*(n-i)+" *"*i)

# Alternative:
def pyra(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("*", end=" ")
        print()

#pyra(5)

# Reverse
def rpyra(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print("*", end=" ")
        print()

def rpyra_2(n):
    for i in range(n+1, 0, -1):
        for j in range(0, i -1):
            print("*", end=" ")
        print()

#rpyra(5)
#print("-"*40)
#rpyra_2(5)


# MAIN
def pyra_2(n):
    for i in range(1, n, 2):
        m = int((n-i+1)/2)
        for k in range(1, m):
            print(" ", end=" ")
        for j in range(1, i+1):
            print("*", end=" ")
        #print("\n")
        print()

pyra_2(10)
