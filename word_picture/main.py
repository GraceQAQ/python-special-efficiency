#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 文字成像
#
#                   @File Name    : main.py
#
#                   @Programmer   : autofelix
#
#                   @Start Date   : 2021-01-06 13:14
#
#                   @Last Update  : 2021-01-06 13:14
#
#-------------------------------------------------------------------
'''
from PIL import Image, ImageDraw, ImageFont

class digitalPicture:
    '''
     This is a main Class, the file contains all documents.
     One document contains paragraphs that have several sentences
     It loads the original file and converts the original file to new content
     Then the new content will be saved by this class
    '''
    def __init__(self):
        self.font_size = 7
        self.picture = 'assets/picture.jpeg'

    def hello(self):
        '''
        This is a welcome speech
        :return: self
        '''
        print('*' * 50)
        print(' ' * 20 + '文字成像')
        print(' ' * 5 + 'Author: autofelix  Date: 2021-01-06 13:14')
        print('*' * 50)
        return self

    def run(self):
        '''
        The program entry
        '''
        word = input('请输入你想说的：') or '我喜欢你！'

        resource = Image.open(self.picture)
        img_array = resource.load()

        image_new = Image.new('RGB', resource.size, (0, 0, 0))
        draw = ImageDraw.Draw(image_new)
        font = ImageFont.truetype('/System/Library/Fonts/PingFang.ttc', self.font_size)

        yield_word = self.character_generator(word)

        for y in range(0, resource.size[1], self.font_size):
            for x in range(0, resource.size[0], self.font_size):
                draw.text((x, y), next(yield_word), font=font, fill=img_array[x, y], direction=None)

        image_new.convert('RGB').save('result.jpeg')

    def character_generator(self, text):
        while True:
            for i in range(len(text)):
                yield text[i]


if __name__ == '__main__':
    digitalPicture().hello().run()


