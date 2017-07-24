#prompt user for n-value (number of test cases)
n = input()
i = 1
while i <= n:
    x = input()
    if x % 2 == 0:
        print x, "is even"
    else:
        print x, "is odd"
    i += 1
