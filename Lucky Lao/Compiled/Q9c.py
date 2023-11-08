def c():
    f = open("Python.txt", "r")
    lines = f.readlines()

    for line in lines[::-1]:
        for word in line.split()[::-1]:
            print(word, end=" ")
        print()

c()