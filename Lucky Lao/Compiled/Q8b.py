raw_list = [10, 20, 40.5, "Hello", "7", 'abc,']
print("Old List:", raw_list)

cubes = [elt ** 3 for elt in raw_list if ((isinstance(elt, int) == True) and (elt % 2 == 0))]
print("The cube of the even integers are:")
print(cubes)
