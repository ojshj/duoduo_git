def sum_difference(num):
    sum_of_square=sum([i**2 for i in range(1,num+1)])
    sum_=sum([j for j in range(1,num+1)])
    square_of_sum=sum_**2 

    return square_of_sum - sum_of_square

if __name__ == '__main__':
    num=100
    print (sum_difference(num))

#25164150