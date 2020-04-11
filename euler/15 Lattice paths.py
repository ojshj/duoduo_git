def path(num):
    a=1
    for i in range(1,2*num+1):
        a *= i
    for i in range(1,num+1):
        a /= i
        a /= i
    return a
print (path(20))
