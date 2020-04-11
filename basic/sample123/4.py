spam=3
while spam<4:
    print('yes')
    spam=spam+1
    
    
tick=1
while tick<5:
    tick=tick+1
    if tick==3:
        #continue
        pass
    print(' tick is',tick)
    
    
height=int(input('how tall is the tree: '))
spaces=height-1
hashes=1
while height !=0:
    for i in range(spaces):
        print(' ',end='')
    for i in range(hashes):
        print('#',end='')
    print()
    spaces-=1
    hashes+=2
    height-=1