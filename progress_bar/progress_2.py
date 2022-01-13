#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 可视化进度条二
#
#                   @File Name    : progress_2.py
#
#                   @Programmer   : autofelix
#
#                   @Start Date   : 2022/01/13 13:14
#
#                   @Last Update  : 2022/01/13 13:14
#
#-------------------------------------------------------------------
'''

import time

class progress:
    '''
     This is a main Class, the file contains all documents.
     One document contains paragraphs that have several sentences
     It loads the original file and converts the original file to new content
     Then the new content will be saved by this class
    '''
    def __init__(self):
        self.scale = 50

    def hello(self):
        '''
        This is a welcome speech
        :return: self
        '''
        print('*' * 50)
        print(' ' * 20 + '可视化进度条二')
        print(' ' * 5 + '作者: autofelix  Date: 2022-01-13 13:14')
        print(' ' * 5 + '主页: https://autofelix.blog.csdn.net')
        print('*' * 50)
        return self

    def run(self):
        '''
        The program entry
        '''
        print('执行开始，祈祷不报错' . center(self.scale // 2, '-'))
        start = time.perf_counter()
        for i in range(self.scale + 1):
            a = '*' * i
            b = '.' * (self.scale - i)
            c = (i / self.scale) * 100
            dur = time.perf_counter() - start
            print('\r{:^3.0f}%[{}->{}]{:.2f}s' . format(c, a, b, dur), end='')
            time.sleep(0.1)
        print('\n执行结束，万幸' . center(self.scale // 2, '-'))

if __name__ == '__main__':
    progress().hello().run()