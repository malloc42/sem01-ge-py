t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
t2 = (11, 13, 15)

print("Tuple t1:", t1)
print("Tuple t2:", t2)

for i in t1:
    t2 += (i,)

print("Tuple t2 concatenated with tuple t1:", t2)
