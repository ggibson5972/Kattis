#read in megabytes per month
mega = int(raw_input())
#read in number of months
N = int(raw_input())
t = 1
#leftover megabytes
L = 0
while t <= N:
    P = input()
    L = L + (mega - P)
    t += 1
print L + mega
