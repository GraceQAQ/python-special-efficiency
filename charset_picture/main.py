#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 图片转换为字符图片
#
#                   @File Name    : main.py
#
#                   @Programmer   : autofelix
#
#                   @Start Date   : 2022/01/07 13:14
#
#                   @Last Update  : 2022/01/07 13:14
#
#-------------------------------------------------------------------
'''
from PIL import Image

class charsetPicture:
    '''
     This is a main Class, the file contains all documents.
     One document contains paragraphs that have several sentences
     It loads the original file and converts the original file to new content
     Then the new content will be saved by this class
    '''
    def __init__(self):
        self.char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
        self.width = 60
        self.height = 60

    def hello(self):
        '''
        This is a welcome speech
        :return: self
        '''
        print('*' * 50)
        print(' ' * 18 + '图片转换为字符图片')
        print(' ' * 5 + 'Author: autofelix  Date: 2022-01-07 13:14')
        print('*' * 50)
        return self

    def get_char(self, r, g, b, alpha=256):
        '''
        将256灰度映射到70个字符上，也就是RGB值转字符的函数
        :alpha: 透明度
        :return: self
        '''
        if alpha == 0:
            return ' '
        length = len(self.char)
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
        unit = (256.0 + 1) / length
        return self.char[int(gray / unit)]

    def run(self):
        '''
        The program entry
        '''
        im = Image.open('assets/picture.jpeg')
        im = im.resize((self.width, self.height), Image.NEAREST)
        txt = ''
        for i in range(self.height):
            for j in range(self.width):
                txt += self.get_char(*im.getpixel((j, i)))
            txt += '\n'
        print(txt)
        with open('handler.txt', 'w') as f:
            f.write(txt)

if __name__ == '__main__':
    charsetPicture().hello().run()


