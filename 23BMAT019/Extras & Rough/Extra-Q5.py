n = int(input("Enter n such that n is positive: "))
total = 0

for i in range(1, n+1):
  total += i

print("Sum of first", n, "positive no.s is", total)
