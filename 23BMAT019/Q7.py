def check_occur(a, b):
    indices = []
    for i in range(0, len(a)-len(b)+1):
        if (a[i:i+len(b)] == b):
            indices.append(i)

    if (indices):
        print(indices)
    else:
        print(-1)

def main():
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    
    print("Indices of occurrences of '" + str2 + "' in '" + str1+ "' (-1 if none):")
    check_occur(str1, str2)

if __name__ == "__main__":
    main()
