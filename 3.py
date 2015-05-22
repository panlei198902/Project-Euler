x=input('insert your number:')
a=[]
for i in xrange(5,x):
    if x%i==0:
        for i2 in xrange(2,i):
            if i%i2==0:
                break
        else:
            a.append(i)
print a
