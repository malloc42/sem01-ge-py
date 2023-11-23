import sys

def username():
    try:
        n = input("Enter your name: ")
        if (n.isalpha() == True):
            print(n)
        elif (n.isalnum() == True):
            raise ValueError("It contains digits")
        elif (n.isspace() == True):
            raise TypeError("It contains spaces")
        else:
            print("Name contains special characters")
    except ValueError:
        print("Invalid Input: ValueError")
        print(str(sys.exc_info()))
    except TypeError:
        print("Name contains only spaces")

username()
