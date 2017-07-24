#Prompt user to enter a number between 1 and 100
N = input()
#Provide route if number isn't within range
if N < 1 or N > 100:
    print "Number not within range."
    number = input('Enter a number between 1 and 100: ')
i = 1
while i <= N:
    print i, "Abracadabra"
    i += 1
