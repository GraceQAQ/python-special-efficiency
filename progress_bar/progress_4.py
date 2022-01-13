#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 可视化进度条四
#
#                   @File Name    : progress_4.py
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
from progress.bar import IncrementalBar

class progress:
    '''
      This is a main Class, the file contains all documents.
      One document contains paragraphs that have several sentences
      It loads the original file and converts the original file to new content
      Then the new content will be saved by this class
     '''
    def __init__(self):
        self.table = [1, 2, 3, 4, 5, 6, 7, 8]

    def hello(self):
        '''
        This is a welcome speech
        :return: self
        '''
        print('*' * 50)
        print(' ' * 20 + '可视化进度条四')
        print(' ' * 5 + '作者: autofelix  Date: 2022-01-13 13:14')
        print(' ' * 5 + '主页: https://autofelix.blog.csdn.net')
        print('*' * 50)
        return self

    def run(self):
        '''
        The program entry
        '''
        bar = IncrementalBar('Countdown', max=len(self.table))
        for item in self.table:
            bar.next()
            time.sleep(1)
            bar.finish()

if __name__ == '__main__':
    progress().hello().run()