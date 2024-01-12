def a():
    no_words = 0
    no_lines = 0
    no_chars = 0

    f = open("Python.txt", "r")
    lines = f.readlines()

    for line in lines:
        no_words += len(line.split())
        no_lines += 1
        no_chars += len(line)

    print("No. of words:", no_words)
    print("No. of lines:", no_lines)
    print("No. of characters:", no_chars)

    f.close()

a()