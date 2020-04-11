import os
import sys
import shutil  

#获取当前文件所在目录
current_path = sys.path[0] + "/"

#遍历当前目录所有文件 and 文件夹
for file in os.listdir(current_path):
    #删除指定文件夹
    if file == "Debug" or file == "ipch":
          #注意:删除文件需要绝对路径, 而folder是相对路径
          shutil.rmtree(current_path + file)
    #删除指定文件
    if file[-3:] == ".db":
         os.remove(current_path + file) 


    