#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 高级图片转换特效之素描
#
#                   @File Name    : effects_4.py
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
        print(' ' * 20 + '高级图片转换特效之素描')
        print(' ' * 5 + '作者: autofelix  Date: 2022-01-16 13:14')
        print(' ' * 5 + '主页: https://autofelix.blog.csdn.net')
        print('*' * 50)
        return self

    def run(self):
        # 读取原始图像
        img = cv2.imread(self.path)
        # 图像灰度处理
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 高斯滤波降噪
        gaussian = cv2.GaussianBlur(gray, (5, 5), 0)

        # Canny算子
        canny = cv2.Canny(gaussian, 50, 150)
        # 阈值化处理
        ret, result = cv2.threshold(canny, 100, 255, cv2.THRESH_BINARY_INV)
        # 显示图像
        cv2.imshow('src', img)
        cv2.imshow('result', result)
        cv2.waitKey()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    picture().hello().run()