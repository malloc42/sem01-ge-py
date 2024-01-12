def quadratic_roots(a, b, c):
    D = b**2 - 4*a*c
    x1 = (-b + D**.5)/(2*a)
    x2 = (-b - D**.5)/(2*a)
    return x1, x2

def main():
    print("Program to calculate the roots of ax^2 + bx + c = 0")
    a = eval(input("Enter the coefficient of x^2 (a) : "))
    b = eval(input("Enter the coefficient of x   (b) : "))
    c = eval(input("Enter the constant term      (c) : "))

    roots = quadratic_roots(a, b, c)
    print("The roots are:", roots[0], "and", roots[1])

if (__name__ == "__main__"):
    main()