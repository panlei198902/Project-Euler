a=[1,2]
i=0
while True:
    b=a[i]+a[i+1]
    a.append(b)
    i+=1
    if max(a)>=4000000:
        a.pop()
        break
b=a[1::3]
print sum(b)
