#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 图片转换特效之黑白
#
#                   @File Name    : effects_1.py
#
#                   @Programmer   : autofelix
#
#                   @Start Date   : 2022/01/13 13:14
#
#                   @Last Update  : 2022/01/13 13:14
#
#-------------------------------------------------------------------
'''
import numpy as np
from PIL import Image

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
        print(' ' * 20 + '图片转换特效之黑白')
        print(' ' * 5 + '作者: autofelix  Date: 2022-01-13 13:14')
        print(' ' * 5 + '主页: https://autofelix.blog.csdn.net')
        print('*' * 50)
        return self

    def run(self):
        '''
        The program entry
        '''
        im = self.to_black_white()
        im.show()
        im.save('assets/black_white.jpeg')

    def to_black_white(self):
        '''
        Picture to black white
        '''
        im = np.asarray(Image.open(self.path).convert('RGB'))
        trans = np.array([[0.299, 0.587, 0.114], [0.299, 0.587, 0.114], [0.299, 0.587, 0.114]]).transpose()
        im = np.dot(im, trans)
        return Image.fromarray(np.array(im).astype('uint8'))

if __name__ == '__main__':
    picture().hello().run()