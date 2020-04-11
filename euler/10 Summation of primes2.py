import math

def prime(number):
    #ceil 是向上取整, 因为number开根号可能是小数, 而range的参数只能是整数, 所以使用ceil
    #也可以写成    
    #for i in range(2, int(number**0.5 + 1)):  #int(xx)可以把一个小数取整数部分
    for i in range(2, math.ceil(number**0.5)):
        if number%i == 0:
                return False
        else:   
            i += 1
    return True

if __name__ == '__main__':
    l=[]
    for j in range(2, 200):
        if prime(j):
            print(j)
            l.append(j)

    #l可以直接取sum
    #[i for i in l] 其实就等于l
    print("sum is:", sum(l))


