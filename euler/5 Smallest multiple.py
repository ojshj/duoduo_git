def possible_number(number):
    data = [11,12,13,14,15,16,17,18,19,20]

    for i in data:
        if number%i!=0:
           return False
    return True

if __name__ == "__main__":
    j = 1
    while(True):
        if possible_number(j):
            print(j)
            break
        else:
            j+=1
 

 #answer: 232792560