n = input() #number of temperatures collected
T = raw_input().split(" ") #separates each input of T with a " "
sum = 0
for t in T:
    if int(t) < 0:
        sum += 1
print sum
