#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 高级图片转换特效之毛玻璃
#
#                   @File Name    : effects_1.py
#
#                   @Programmer   : autofelix
#
#                   @Start Date   : 2022/01/14 13:14
#
#                   @Last Update  : 2022/01/14 13:14
#
#-------------------------------------------------------------------
'''
import cv2
import numpy as np

class picture:
    '''
     This is a main Class, the file contains all documents.
     One document contains paragraphs that have several sentences
     It loads the original file and converts the original file to new content
     Then the new content will be saved by this class
    '''
    def __init__(self):
        self.path = 'assets/picture.jpeg'

    def hello(self):
        '''
        This is a welcome speech
        :return: self
        '''
        print('*' * 50)
        print(' ' * 20 + '高级图片转换特效之毛玻璃')
        print(' ' * 5 + '作者: autofelix  Date: 2022-01-16 13:14')
        print(' ' * 5 + '主页: https://autofelix.blog.csdn.net')
        print('*' * 50)
        return self

    def run(self):
        # 读取原始图像
        src = cv2.imread(self.path)
        # 新建目标图像
        dst = np.zeros_like(src)
        # 获取图像行和列
        rows, cols = src.shape[:2]
        # 定义偏移量和随机数
        offsets = 5
        random_num = 0
        # 毛玻璃效果: 像素点邻域内随机像素点的颜色替代当前像素点的颜色
        for y in range(rows - offsets):
            for x in range(cols - offsets):
                random_num = np.random.randint(0, offsets)
                dst[y, x] = src[y + random_num, x + random_num]
        # 显示图像
        cv2.imshow('src', src)
        cv2.imshow('dst', dst)
        cv2.waitKey()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    picture().hello().run()