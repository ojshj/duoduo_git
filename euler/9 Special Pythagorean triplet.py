def Special_Pythagorean_triplet(a,b):
    c=1000-a-b
    return a*a+b*b==c*c
    

if __name__ == '__main__':
    for i in range(1,1000):
        for j in range(i+1,1000):
            if Special_Pythagorean_triplet(i,j):
                print (i)
                print (j)