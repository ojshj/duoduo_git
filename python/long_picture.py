#!/usr/bin/env python
# ‐*‐ coding:utf‐8 ‐*‐
"""code_info
@Time : 2020 2020/7/15 10:44
@Author : Oj
@File : game.py
"""

from PIL import Image
import glob


# 计算特定宽度下缩放得到的高度和总高度
def get_height(img, pic_width, all_len=0):
    pic_height = pic_width * img.size[1] // img.size[0]
    # 返回图片拼接总长度
    all_len = all_len + pic_height
    return pic_height, all_len


def join(pic_names, choice='1'):
    pic_heights = []  # 图长
    im_list = [Image.open(f) for f in pic_names]
    all_len = 0
    wid = 0
    # 遍历图片，修改图片大小
    for i, im in enumerate(im_list):
        if i == 0:  # 第一张图只需要读取宽度
            pic_heights.append(0)
            img = im_list[0]
            wid, pic_height = img.size[0], img.size[1]
            all_len = pic_height
            print("图{}的size为: ".format(i + 1), img.size)

        else:  # 第二张图片开始，更改图片大小
            img = im_list[i]
            print("图{}的size为: ".format(i + 1), img.size)
            pic_heights.append(pic_height)
            pic_height, all_len = get_height(img, wid, all_len)
            # 将图片等比例放大或缩小
            img = img.resize((wid, pic_height), Image.ANTIALIAS)
            print("修改后图{}的size为: ".format(i + 1), img.size)
            # 保存修改后的图片
            img.save(pic_names[i])

    # 创建空白图
    result = Image.new("RGB", (wid, all_len))

    # 拼接图片
    for i, im in enumerate(im_list):
        result.paste(im, box=(0, pic_heights[i]))

    # 保存图片
    result.show()
    if choice == '1':
        result.save('out.png')
    if choice == '2':
        result.save('out.jpg')


def join_all():
    pic_names = []  # 图片名
    choice = input('拼接.png文件输入1，拼接.jpg文件图输入2：')
    while choice not in ['1', '2']:
        choice = input('请重新选择：')
    else:
        if choice == '1':
            # 读取当前目录下所有图片
            for file in glob.glob("*.png"):
                print(file)
                pic_names.append(file)
            # 拼接
            join(pic_names)
        if choice == '2':
            for file in glob.glob("*.jpg"):
                print(file)
                pic_names.append(file)
            # 拼接
            join(pic_names, '2')


def join_some():
    pic_num = input('拼接图片数为：')
    pic_num = int(pic_num)
    pic_names = []  # 图片名
    # 获取图片名称
    for i in range(1, pic_num + 1):
        # 输入要被拼接的图片名
        pic_name = input('输入第{}张图片名：'.format(i))
        pic_names.append(pic_name)
    # 拼接
    join(pic_names)


def main():
    print('请将本代码文件放入需要拼接的图片目录中执行')
    choice = input('拼接当前文件夹下全图输入1，拼接自定义图输入2：')
    while choice not in ['1', '2']:
        choice = input('请输入范围内的选择：')
    else:
        if choice == '1':
            join_all()
        if choice == '2':
            join_some()


main()
