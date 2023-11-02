def a(str1, str2):
    l1 = []
    for i in range(0, len(str1)):
        if (str1[i:i+len(str2)] == str2):
            l1.append(i)
    
    if l1:
        print(l1)
    else:
        print("-1")

x = input("Enter the first string: ")
y = input("Enter the second string: ")
a(x, y)
