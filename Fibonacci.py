#Code that generates Fibonacci Series
n = int(input("Enter the value of n:"))
a = 0
b = 1
i = 0
for i in range(0, n):
    print(a, end=' ')
    a, b = b, a + b
    i += 1






