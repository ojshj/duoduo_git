import sys #sys是一个包, 包含系统相关操作
print(sys.path[0])  #打印当前文件位置

txt_path = sys.path[0] + "/" + "test.txt"

print(txt_path)

#fo称为一个句柄=handle, 
fo = open(txt_path, "r")  #r = read , w = write
lines = fo.readlines()
print(lines)

#对于lines中的每个line , 遍历list的方法
for line in lines:
    print(line)

#用写的方式打开文件
fo = open(txt_path, 'a+')
fo.writelines(["cccc\n", "ddd\n"])