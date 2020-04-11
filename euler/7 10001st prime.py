def prime(number):
    for i in range(2,number+1):
        if number%i==0:
            return False
    return True
if __name__ == '__main__':
    l=[]
    j = 1
    while(True):
        if prime(j):
            l.append(j)
        else:
            j+=1
    l.sort(reverse=False)
    print(l[1000])
