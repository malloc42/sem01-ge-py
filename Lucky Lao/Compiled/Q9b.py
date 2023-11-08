def b():
    freq = {}

    f = open("Python.txt", "r")
    chars = f.read()

    for i in chars:
        freq[i] = chars.count(i)

    print("Frequency of every character:")
    print(freq)

b()