#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 高级图片转换特效之浮雕
#
#                   @File Name    : effects_2.py
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
        print(' ' * 20 + '高级图片转换特效之浮雕')
        print(' ' * 5 + '作者: autofelix  Date: 2022-01-16 13:14')
        print(' ' * 5 + '主页: https://autofelix.blog.csdn.net')
        print('*' * 50)
        return self

    def run(self):
        # 读取原始图像
        img = cv2.imread(self.path, 1)
        # 获取图像的高度和宽度
        height, width = img.shape[:2]
        # 图像灰度处理
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 创建目标图像
        dstImg = np.zeros((height, width, 1), np.uint8)
        # 浮雕特效算法：newPixel = grayCurrentPixel - grayNextPixel + 150
        for i in range(0, height):
            for j in range(0, width - 1):
                grayCurrentPixel = int(gray[i, j])
                grayNextPixel = int(gray[i, j + 1])
                newPixel = grayCurrentPixel - grayNextPixel + 150
                if newPixel > 255:
                    newPixel = 255
                if newPixel < 0:
                    newPixel = 0
                dstImg[i, j] = newPixel

        # 显示图像
        cv2.imshow('src', img)
        cv2.imshow('dst', dstImg)
        # 等待显示
        cv2.waitKey()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    picture().hello().run()