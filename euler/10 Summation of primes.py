def prime(number):
    i=2
    while i**2<=number:
        if number%i==0:
            return False
        i+=1
    return True
if __name__ == '__main__':
    l=[]
    for j in range(1,2000000):
        if prime(j)==True:
            l.append(j)
    Summation_of_primes=sum([z for z in l])
    print (Summation_of_primes)


