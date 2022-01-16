#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 高级图片转换特效之流年
#
#                   @File Name    : effects_7.py
#
#                   @Programmer   : autofelix
#
#                   @Start Date   : 2022/01/14 13:14
#
#                   @Last Update  : 2022/01/14 13:14
#
#-------------------------------------------------------------------
'''
import cv2, math
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
        print(' ' * 20 + '高级图片转换特效之流年')
        print(' ' * 5 + '作者: autofelix  Date: 2022-01-16 13:14')
        print(' ' * 5 + '主页: https://autofelix.blog.csdn.net')
        print('*' * 50)
        return self

    def run(self):
        # 读取原始图像
        img = cv2.imread(self.path)
        # 获取图像行和列
        rows, cols = img.shape[:2]
        # 新建目标图像
        dst = np.zeros((rows, cols, 3), dtype="uint8")
        # 图像流年特效
        for i in range(rows):
            for j in range(cols):
                # B通道的数值开平方乘以参数12
                B = math.sqrt(img[i, j][0]) * 12
                G = img[i, j][1]
                R = img[i, j][2]
                if B > 255:
                    B = 255
                dst[i, j] = np.uint8((B, G, R))

        # 显示图像
        cv2.imshow('src', img)
        cv2.imshow('dst', dst)
        cv2.waitKey()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    picture().hello().run()