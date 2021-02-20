fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()

for lin in hand:
    line = lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(wds)
    for w in wds:

        # if key is not there, then the count is zero (long version)
        #oldcount = di.get(w,0)
        #print(w,'old', oldcount)
        #newcount = oldcount + 1
        #di[w] = newcount

        # create counter idiom to replace lines 15-18
        di[w] = di.get(w,0) + 1
        #print(w,'new', di[w])

    #print(di)

# now find most common word with maximum loop
    largest = -1
    theword = None
    for k,v in di.items() :
        print(k,v)
        if v > largest :
            largest = v
            theword = k

    print('Done', theword, largest)