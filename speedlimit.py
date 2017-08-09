#get starting number of data points
n = input()
while n != -1:
    #initiate variables
    i = n
    dis = 0
    st = 0
    while i > 0:
        #get input for speed and total time
        s, t = map(int, raw_input().split(" ")) #s is the speed and t is the total time
        #subtract used time used from total time
        t -= st
        #add used time to total time
        st += t
        #calculate distance traveled
        dis = dis + s * t
        #move on to next data point in set
        i -= 1
        #keep reading data sets until n == -1
        if i == 0:
            #print miles traveled in the data set
            print dis, "miles"
            #read in length of next data set
            n = input()
