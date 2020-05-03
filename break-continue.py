lists = [2,3,4]

for i in range(1,10):                              #i = [1,2,3,4,5,6,7,8,9]
    if (i in lists):                               #if lists (2,3,4) in i (range(1,10))
        continue                                   #back to the beginning of the loop
    print(i)                                       #does not print 2,3,4 because of continue command


