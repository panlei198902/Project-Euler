x=11
n=0
while True:
    for i in range(1,21):
        if x % i !=0:
            break
    else:
        n=x
    x+=1
    if n>0:
        print n
        break
    
            
