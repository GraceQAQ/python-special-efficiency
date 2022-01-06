#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 词云表白专用
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
from wordcloud import WordCloud
import cv2, jieba
import matplotlib.pyplot as plt

class wordCloud:
    '''
     This is a main Class, the file contains all documents.
     One document contains paragraphs that have several sentences
     It loads the original file and converts the original file to new content
     Then the new content will be saved by this class
    '''
    def __init__(self):
        self.bg_img = 'assets/back.jpeg'
        self.word_path = 'assets/word.txt'

    def hello(self):
        '''
        This is a welcome speech
        :return: self
        '''
        print('*' * 50)
        print(' ' * 20 + '词云表白专用')
        print(' ' * 5 + 'Author: autofelix  Date: 2021-01-06 13:14')
        print('*' * 50)
        return self

    def run(self):
        '''
        The program entry
        '''
        with open(self.word_path, 'r') as f:
            word = f.read()

        cut_word = ' '.join(jieba.cut(word))
        color_mask = cv2.imread(self.bg_img)

        word_cloud = WordCloud(
            # 设置字体，不指定就会出现乱码
            font_path='/System/Library/Fonts/PingFang.ttc',
            # 设置背景色
            background_color='white',
            # 词云形状
            mask=color_mask,
            # 允许最大词汇
            max_words=120,
            # 最大号字体
            max_font_size=2000
        )

        result = word_cloud.generate(cut_word)
        result.to_file('word_cloud.jpg')
        plt.imshow(result, interpolation='bilinear')
        plt.axis('off')
        plt.show()


if __name__ == '__main__':
    wordCloud().hello().run()


