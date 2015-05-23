def ssq(n):
    answer=0
    for i in range(n+1):
        answer+=pow(i,2)
    return answer
def sqs(m):
    answer=0
    for i in range(m+1):
        answer+=i
    return pow(answer,2)
print sqs(100)-ssq(100)
print sqs(100),ssq(100)
        
