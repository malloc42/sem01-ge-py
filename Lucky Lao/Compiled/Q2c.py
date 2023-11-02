def prime_gen(n):
    p = 2
    count = 0

    while (count != n):
        flag = True
        for i in range(2, p):
            if (p % i == 0):
                flag = False
                break

        if (flag):
            print(p)
            count += 1

        p += 1

def main():
    n = int(input("Enter a number: "))

    if (n > 0):
        print("First", n, "Prime number(s) are as follows:")
        prime_gen(n)
    else:
        print("Please enter an integer greater than 0.")

    print("Program Finished.")

if (__name__ == "__main__"):
    main()