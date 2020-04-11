def checkIsPalindromicNumber(number):
    s = "%d"%(number)
    len_s = len(s)
    for i in range(len_s//2):
        if s[i] != s[len_s - i -1]:
            return False
    return True

if __name__ == "__main__":
    max_number = 0
    for i in range(100,1000):
        for j in range(100,1000):
            a = i*j
            if checkIsPalindromicNumber(a)==True:
                if a > max_number:
                    max_number = a
    print(max_number)