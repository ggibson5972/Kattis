#Prompt user to enter the amount of numbers
N = input()
#if N isn't in range
if N < 1 or N > 10:
    print "N not within range."
    N = input()
#if N is in range
else:
    i = 1
    sum = 0
    while i <= N:
        P = input()
        #if P isn't in range
        if P < 10 or P > 9999:
            print "P not within range."
            P = input()
        else:
            sum = (P / 10) ** (P % 10) + sum
            i += 1
    print sum
