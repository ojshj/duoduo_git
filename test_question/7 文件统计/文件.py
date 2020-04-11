
#函数, 输出将输入的字符串替换掉非字母字符后的字符串
def repalce_non_letter(a):
    b= ""
    for letter in a:
        if (letter >= 'a' and letter <= 'z' ) or (letter >= 'A' and letter <= 'Z' ) :
           b = b + letter
        else:
           b = b + " "
    return b

#main函数, 代码从这个函数开始运行
if __name__== "__main__":
    #1打开costmap_model.cpp 这个文件
    f=open('d:\\new\\costmap_model.cpp')

    #打印第一行
    #print(f.readlines()[0])

    #存储我们转换后的新行
    new_lines = []

    for old_line in f.readlines():
        #替换非字母字符
        new_line = repalce_non_letter(old_line)
        #print(newline)
        #加入到新行中, 这里使用append方法完成加入
        new_lines.append(new_line)

    #print(new_lines)

    #存储单词出现的次数
    word_dict = {}
    #遍历每一行
    for line in new_lines:
      #在每一行遍历每个单词, 注意这里要用split将单词根据空格分隔开
      for word in line.split(" "):
          #如果单词已存储在字典中
         if word in word_dict:
             #计数加1
             word_dict[word] = word_dict[word] + 1
         else:
             #初始化计数为1
             word_dict[word] = 1
    print(word_dict)




