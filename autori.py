#read in user input
n = raw_input()
#initiate abbreviated output
abbrev = ""
#iterate to check if each character in input is a capital letter
for i in n:
    if i.isupper():
        #add letter to abbrev string if it is capital
        abbrev = abbrev + i
print abbrev
