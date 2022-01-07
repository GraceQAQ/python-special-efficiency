#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 千图成像_方法二
#
#                   @File Name    : hsv_main.py
#
#                   @Programmer   : autofelix
#
#                   @Start Date   : 2021-01-08 13:14
#
#                   @Last Update  : 2021-01-08 13:14
#
#-------------------------------------------------------------------
'''
from PIL import Image, ImageOps
from multiprocessing import Pool
# from pathos.multiprocessing import ProcessingPoll as Pool
import os
import random
from math import *
from colorsys import rgb_to_hsv
import time
import sys

# 写在最前

# 马赛克画照片采用了三种不同的算法，效果较好，
# 效率较高的方法为HSV颜色空间模型算法

# 这部分代码为HSV颜色模型的实现代码


# 一些全局变量，在主函数中会根据需要改变
IMAGE_DB_DIR = "D:/Python/PyQt/课程设计/wallpaper"
IMAGE_DB_DIR_NEW = "D:/Python/PyQt/课程设计/New_Ku/"

REP_DIS = 3

# 下面两个变量为生成的图库的图片的大小
# 推荐值为16:9，实测效果较好值为4:3
SIZE_WIDTH_db = 4
SIZE_HEIGHT_db = 3

# 下面两个变量为生成的马赛克图片的的大小
# 推荐值为1920:1080
SIZE_WIDTH = 1920
SIZE_HEIGHT = 1080

# 进度条
NUM = 0


def Cal_HSV(image):
    width, height = image.size
    pixels = image.load()
    pixs = []
    for x in range(width):
        for y in range(height):
            pix = pixels[x, y]
            pixs.append(pix)

    H = 0;
    S = 0;
    V = 0
    count = len(pixs)
    for i in range(count):  # 对每个像素块求HSV的平均值
        R = pixs[i][0]
        G = pixs[i][1]
        B = pixs[i][2]
        hsv = rgb_to_hsv(R / 255, G / 255, B / 255)
        # 将RGB格式转化为HSV格式
        H += hsv[0]
        S += hsv[1]
        V += hsv[2]

    HAvg = round(H / count, 3)
    SAvg = round(S / count, 3)
    VAvg = round(V / count, 3)
    return (HAvg, SAvg, VAvg)


def Find_Close(image, list_colors):
    sim = sys.maxsize
    for hsv in list_colors:
        temp_sim = sqrt((image[0] - hsv[0]) ** 2 + (image[1] - hsv[1]) ** 2 + (image[2] - hsv[2]) ** 2)
        # print(temp_sim)
        if temp_sim < sim:
            if hsv[3] < REP_DIS:
                sim = temp_sim
                hsv_min = hsv
                hsv[3] += 1
            else:
                hsv[3] = 0
    return tuple(hsv_min[0:3])


'''
def progress_bar(width_now, height_now):
    global NUM
    if height_now==0:
        NUM=round((width_now+SIZE_WIDTH_db)/(SIZE_WIDTH*SIZE_HEIGHT), 3)
    else:
        NUM=round(((height_now-1)*SIZE_WIDTH+width_now+SIZE_WIDTH_db)/(SIZE_WIDTH*SIZE_HEIGHT), 3)
    return NUM
'''


def Make_Mosaic(image, color_list):
    print("生成图片中...")
    print("生成的马赛克图片大小为", image.size)
    width, height = image.size
    count_images = round((width * height) / (SIZE_WIDTH_db * SIZE_HEIGHT_db))
    # 计算总共需要的马赛克块的数目，为了配合进度条使用
    # images
    new_image = Image.new('RGB', image.size)  # , (255, 255, 255))

    for y1 in range(0, height, SIZE_HEIGHT_db):
        for x1 in range(0, width, SIZE_WIDTH_db):
            y2 = y1 + SIZE_HEIGHT_db
            x2 = x1 + SIZE_WIDTH_db
            temp_image = image.crop((x1, y1, x2, y2))
            hsv = Cal_HSV(temp_image)
            close_image_name = Find_Close(hsv, color_list)
            # print(close_image_name)
            close_image_name = IMAGE_DB_DIR_NEW + str(close_image_name) + '.jpg'
            paste_image = Resize_Image(close_image_name, SIZE_WIDTH_db, SIZE_HEIGHT_db)
            # paste_image=Image.open(close_image_name)
            new_image.paste(paste_image, (x1, y1))
            '''
            progress_bar(x1, y1)
            '''
    return new_image


def Images_DIR():
    paths = []
    for filename in os.listdir(IMAGE_DB_DIR):
        image_temp_dir = IMAGE_DB_DIR + filename
        paths.append((image_temp_dir, IMAGE_DB_DIR_NEW))
    return paths


def Resize_Image(in_name, size_width, size_height):
    image = Image.open(in_name)
    image = ImageOps.fit(image, (size_width, size_height), Image.ANTIALIAS)
    return image


def Convert_Image_HSV(inf):
    # global IMAGE_DB_DIR_NEW
    path = inf[0]
    image_db_dir_new = inf[1]
    image = Resize_Image(path, 160, 90)
    # image=Resize_Image(path, SIZE_WIDTH_db, SIZE_HEIGHT_db)
    hsv = Cal_HSV(image)
    image.save(str(image_db_dir_new) + str(hsv) + ".jpg")
    # print(IMAGE_DB_DIR_NEW)


def Make_New_Image_DB():
    print("生成配色方案中...")
    paths = Images_DIR()
    pool = Pool()
    pool.map(Convert_Image_HSV, paths)
    pool.close()
    pool.join()


def Read_Image_DB():
    image_db = []
    for filename in os.listdir(IMAGE_DB_DIR_NEW):
        if filename == 'None.jpg':
            pass
        else:
            filename = filename.split('.jpg')[0]
            filename = filename[1:-1].split(', ')
            filename = list(map(float, filename))
            filename.append(0)
            image_db.append(filename)
    return image_db


# 该函数用于传参后判断参数是否正确
# 要判断九个变量，传参时只传两个非全局变量
def Judge_Var():
    print("验证变量中...")
    if not os.path.exists(IMAGE_DB_DIR_NEW):
        os.mkdir(IMAGE_DB_DIR_NEW[:-1])
        # 不取最后一个是为了除去"/"
        # 这步肯定要做异常处理，为了调试方便先不写


def Mosaic_Image_HSV(size_width_db,
                     size_height_db,
                     size_width,
                     size_height,
                     IMAGE_DIR,
                     image_db_dir,
                     rep_dis,
                     COLOR_MODIFICATION
                     ):
    # 为了避免进程池不接受已改变的全局变量，在创建新图库成功后再改名为改变的图库的全局变量名
    global SIZE_WIDTH_db, SIZE_HEIGHT_db, SIZE_WIDTH, SIZE_HEIGHT
    global IMAGE_DB_DIR, IMAGE_DB_DIR_NEW, REP_DIS

    SIZE_WIDTH_db = size_width_db;
    SIZE_HEIGHT_db = size_height_db
    SIZE_WIDTH = size_width;
    SIZE_HEIGHT = size_height
    IMAGE_DB_DIR = image_db_dir
    IMAGE_DB_DIR_NEW = image_db_dir[0:-1] + str("DB_HSV/")
    IMAGE_SAVE_DIR = ("马赛克图_HSV" + ".").join(IMAGE_DIR.split("."))
    REP_DIS = rep_dis
    # 上述是修改七个全局变量的值
    # 使用这个程序目前需要九个参数，剩余两个参数是打开图片的路径和生成图片的保存路径

    # print(IMAGE_DB_DIR_NEW)
    start_time = time.time()
    Judge_Var()
    Make_New_Image_DB()

    image_turn = Resize_Image(IMAGE_DIR, SIZE_WIDTH, SIZE_HEIGHT)
    list_of_images = Read_Image_DB()
    image_mosaic = Make_Mosaic(image_turn, list_of_images)

    # 下面是未和原图混合的，如果想要可以保留该照片
    # image_mosaic.save(IMAGE_SAVE_DIR)

    # image_mosaic.save("D:/Python/PyQt/课程设计/Save_img/out96.jpg")
    print("hhh")
    image_mosaic_blend = Image.blend(image_mosaic, image_turn, COLOR_MODIFICATION)
    print("hhh")
    image_mosaic_blend.save(IMAGE_SAVE_DIR)  # 混合后的照片的保存
    print("hhh")
    end_time = time.time()
    print("总耗时: %0.2f" % (end_time - start_time))
    print("生成的马赛克图片已保存为%s" % IMAGE_SAVE_DIR)


if __name__ == '__main__':
    Mosaic_Image_HSV(size_width_db=16,
                     size_height_db=9,
                     size_width=1920,
                     size_height=1080,
                     IMAGE_DIR="F:/课设一/ptemp/“森林”中的一只猫鼬.jpg",
                     image_db_dir="D:/wallpaper/",
                     rep_dis=3,
                     COLOR_MODIFICATION=0.5
                     )




