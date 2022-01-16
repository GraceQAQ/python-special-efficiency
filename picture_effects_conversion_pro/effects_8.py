#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 高级图片转换特效之水波
#
#                   @File Name    : effects_8.py
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
        print(' ' * 20 + '高级图片转换特效之水波')
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
        # 定义水波特效参数
        wavelength = 20
        amplitude = 30
        phase = math.pi / 4
        # 获取中心点
        centreX = 0.5
        centreY = 0.5
        radius = min(rows, cols) / 2
        # 设置水波覆盖面积
        icentreX = cols * centreX
        icentreY = rows * centreY

        # 图像水波特效
        for i in range(rows):
            for j in range(cols):
                dx = j - icentreX
                dy = i - icentreY
                distance = dx * dx + dy * dy

                if distance > radius * radius:
                    x = j
                    y = i
                else:
                    # 计算水波区域
                    distance = math.sqrt(distance)
                    amount = amplitude * math.sin(distance / wavelength * 2 * math.pi - phase)
                    amount = amount * (radius - distance) / radius
                    amount = amount * wavelength / (distance + 0.0001)
                    x = j + dx * amount
                    y = i + dy * amount
                # 边界判断
                if x < 0:
                    x = 0
                if x >= cols - 1:
                    x = cols - 2
                if y < 0:
                    y = 0
                if y >= rows - 1:
                    y = rows - 2
                p = x - int(x)
                q = y - int(y)

                # 图像水波赋值
                dst[i, j, :] = (1 - p) * (1 - q) * img[int(y), int(x), :] + p * (1 - q) * img[int(y), int(x), :]
                + (1 - p) * q * img[int(y), int(x), :] + p * q * img[int(y), int(x), :]

        # 显示图像
        cv2.imshow('src', img)
        cv2.imshow('dst', dst)
        cv2.waitKey()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    picture().hello().run()