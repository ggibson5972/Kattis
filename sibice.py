#read in the number of matches and the dimensions of the box
N, W, H = map(int, raw_input().split(" "))
#calculate diagonal of box (pythagorean theorem)
d = int((W ** 2 + H ** 2) ** 0.5)

while N > 0:
    #read in length of each match
    L = input()
    #check if match is smaller than the longest part of box
    if int(L) <= d:
        print "DA"
    else:
        print "NE"
    N -= 1
