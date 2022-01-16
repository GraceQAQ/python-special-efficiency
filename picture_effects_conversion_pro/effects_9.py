#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 高级图片转换特效之卡通
#
#                   @File Name    : effects_9.py
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
        print(' ' * 20 + '高级图片转换特效之卡通')
        print(' ' * 5 + '作者: autofelix  Date: 2022-01-16 13:14')
        print(' ' * 5 + '主页: https://autofelix.blog.csdn.net')
        print('*' * 50)
        return self

    def run(self):
        # 读取原始图像
        img = cv2.imread(self.path)
        # 定义双边滤波的数目
        num_bilateral = 7
        # 用高斯金字塔降低取样
        img_color = img
        # 双边滤波处理
        for i in range(num_bilateral):
            img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=9, sigmaSpace=7)
        # 灰度图像转换
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # 中值滤波处理
        img_blur = cv2.medianBlur(img_gray, 7)
        # 边缘检测及自适应阈值化处理
        img_edge = cv2.adaptiveThreshold(img_blur, 255,
                                         cv2.ADAPTIVE_THRESH_MEAN_C,
                                         cv2.THRESH_BINARY,
                                         blockSize=9,
                                         C=2)
        # 转换回彩色图像
        img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
        # 与运算
        img_cartoon = cv2.bitwise_and(img_color, img_edge)
        # 显示图像
        cv2.imshow('src', img)
        cv2.imshow('dst', img_cartoon)
        cv2.waitKey()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    picture().hello().run()