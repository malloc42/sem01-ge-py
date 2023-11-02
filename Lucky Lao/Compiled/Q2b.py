def primes_till(x):
    n = 2
    while (n <= x):
        flag = True
        
        for i in range(2, n):
            if (n % i == 0):
                flag = False
                break

        if (flag):
            print(n)

        n += 1

def main():
    n = int(input("Enter a number: "))

    if (n > 1):
        print("Prime number(s) till", n, "are as follows:")
        primes_till(n)
    else:
        print("Please enter an integer greater than 1.")

    print("Program Finished.")

if (__name__ == "__main__"):
    main()