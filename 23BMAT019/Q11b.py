t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
t2 = ()

for i in t1:
    if (i % 2 == 0):
        t2 += (i,)

print("The new tuple is:", t2)
