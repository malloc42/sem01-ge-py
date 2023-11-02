t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
t2 = (11, 13, 15)

for i in t1:
    t2 += (i,)

print("The concatenated tuple is: ", t2)
