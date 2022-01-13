#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 可视化进度条一
#
#                   @File Name    : progress_1.py
#
#                   @Programmer   : autofelix
#
#                   @Start Date   : 2022/01/13 13:14
#
#                   @Last Update  : 2022/01/13 13:14
#
#-------------------------------------------------------------------
'''

import sys, time

class progress:
    '''
     This is a main Class, the file contains all documents.
     One document contains paragraphs that have several sentences
     It loads the original file and converts the original file to new content
     Then the new content will be saved by this class
    '''
    def __init__(self):
        pass

    def hello(self):
        '''
        This is a welcome speech
        :return: self
        '''
        print('*' * 50)
        print(' ' * 20 + '可视化进度条一')
        print(' ' * 5 + '作者: autofelix  Date: 2022-01-13 13:14')
        print(' ' * 5 + '主页: https://autofelix.blog.csdn.net')
        print('*' * 50)
        return self

    def run(self):
        '''
        The program entry
        '''
        for i in range(1, 101):
            print('\r', end='')
            print('Download progress: {}%: '.format(i), '▋' * (i // 2), end='')
            sys.stdout.flush()
            time.sleep(0.05)

if __name__ == '__main__':
    progress().hello().run()