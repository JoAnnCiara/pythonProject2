fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()

for lin in hand:
    line = lin.rstrip()
    print(lin)
    wds = lin.split()
    print(wds)
    for w in wds:
        # prints the word before
        print(w)
        # now starts inner loop
        if w in di :
            di[w] = di[w] + 1
            print('**Existing**')
        else:
            di[w] = 1
            print('**NEW**')
        # printing w ; words and di[w] ; the current value counter of inner loop  (key and value)
        print(w,di[w])
    #print counts in {dictionary}
    print(di)


