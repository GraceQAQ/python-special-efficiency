#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 高级图片转换特效之油漆
#
#                   @File Name    : effects_3.py
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
        print(' ' * 20 + '高级图片转换特效之油漆')
        print(' ' * 5 + '作者: autofelix  Date: 2022-01-16 13:14')
        print(' ' * 5 + '主页: https://autofelix.blog.csdn.net')
        print('*' * 50)
        return self

    def run(self):
        # 读取原始图像
        src = cv2.imread(self.path)
        # 图像灰度处理
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        # 自定义卷积核
        kernel = np.array([[-1, -1, -1], [-1, 10, -1], [-1, -1, -1]])
        # kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
        # 图像浮雕效果
        output = cv2.filter2D(gray, -1, kernel)
        # 显示图像
        cv2.imshow('Original Image', src)
        cv2.imshow('Emboss_1', output)
        # 等待显示
        cv2.waitKey()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    picture().hello().run()