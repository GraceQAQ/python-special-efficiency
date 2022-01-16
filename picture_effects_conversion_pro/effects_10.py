#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 高级图片转换特效之滤镜
#
#                   @File Name    : effects_10.py
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
        print(' ' * 20 + '高级图片转换特效之滤镜')
        print(' ' * 5 + '作者: autofelix  Date: 2022-01-16 13:14')
        print(' ' * 5 + '主页: https://autofelix.blog.csdn.net')
        print('*' * 50)
        return self

    def run(self):
        pass

if __name__ == '__main__':
    picture().hello().run()