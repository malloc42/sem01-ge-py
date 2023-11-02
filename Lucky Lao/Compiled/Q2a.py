def prime_check(x):
    flag = True
    for i in range(2, x):
        if (x % i == 0):
            flag = False
            break
    
    if (flag and x > 1):
        print(x, "is a prime number.")
    else:
        print(x, "is not a prime number.")

def main():
    n = int(input("Enter a number: "))
    prime_check(n)

if (__name__ == "__main__"):
    main()