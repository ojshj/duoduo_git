# -*- coding: utf-8 -*-
prime=[];
i=2
#得到100以内的所有素数
for i in range(2,100):
   j=2
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      prime.append(i)
      
#每三个素数相乘，
result=[]
for a in range(0,len(prime)):
    for b in range(1,len(prime)):
        if(b==a):
            continue
        for c in range(2,len(prime)):
            if(c==b):
                continue
            result.append(prime[a]*prime[b]*prime[c])
 
#排序，打印       
result.sort()
k=0
flag=0
for k in range(0,10):
    if(flag==5):
        break
    if(result[k]!=result[k+1]):
        print(result[k])
        flag+=1