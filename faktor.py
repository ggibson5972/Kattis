import math
#Prompt user to enter number of articles and impact factor
A, I = raw_input().split()
#calculate minimum number of citations needed
B = math.ceil(int(A) * (int(I) - 1) + 1)
print int(B)
