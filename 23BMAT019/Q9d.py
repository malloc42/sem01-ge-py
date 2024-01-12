def d():
    f = open("Python.txt", "r")
    lines = f.readlines()

    f1 = open("File1", "w")
    f2 = open("File2", "w")

    for i in range(len(lines)):
        if ((i + 1) % 2 == 0):
            f1.write(lines[i])
        else:
            f2.write(lines[i])

    f.close()
    f1.close()
    f2.close()

d()