fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()

for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:

        di[w] = di.get(w,0) + 1

#print(di)

#x = sorted(di.items())   #sorting first five tuples alphabetically
#print(x[:5])

tmp = list()    # create new empty list
for k, v in di.items():
    newt = (v, k)
    tmp.append(newt)

#print('Flipped', tmp)

tmp = sorted(tmp, reverse=True)
#print("Sorted", tmp[:5])

for v,k in tmp[:5] :
    print(k,v)





