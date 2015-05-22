a=[1,2]
i=0
while True:
    b=a[i]+a[i+1]
    a.append(b)
    i+=1
    if len(a)>=4000000:
        break
print sum(a)
