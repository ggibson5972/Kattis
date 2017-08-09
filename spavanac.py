#read in hour and minute separated by a space
H, M = map(int, raw_input().split(" "))
t = 45  #time needed subtracted

#while the full t hasn't been subtracted
while t > 0:
    #subtract 1 minute
    M -= 1
    t -= 1
    #if the input minutes becomes 0
    if M == 0:
        #subtract an hour
        H -= 1
        #turn minutes positive
        M = M + 60
        #the the hour is negative, turn positive
        if H == -1:
            H = 23

print H, M
