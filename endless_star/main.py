#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 无限五角星
#
#                   @File Name    : main.py
#
#                   @Programmer   : autofelix
#
#                   @Start Date   : 2022/01/13 13:14
#
#                   @Last Update  : 2022/01/13 13:14
#
#-------------------------------------------------------------------
'''
import turtle

class star:
    '''
     This is a main Class, the file contains all documents.
     One document contains paragraphs that have several sentences
     It loads the original file and converts the original file to new content
     Then the new content will be saved by this class
    '''
    def __init__(self):
        self.sides = 6
        self.circle = 360
        self.colors = ['red', 'yellow', 'green', 'blue', 'orange', 'purple']

    def hello(self):
        '''
        This is a welcome speech
        :return: self
        '''
        print('*' * 50)
        print(' ' * 20 + '无限五角星')
        print(' ' * 5 + '作者: autofelix  Date: 2022-01-13 13:14')
        print(' ' * 5 + '主页: https://autofelix.blog.csdn.net')
        print('*' * 50)
        return self

    def run(self):
        turtle.bgcolor('black')
        t = turtle.Pen()
        for x in range(self.circle):
            t.pencolor(self.colors[x % self.sides])
            t.forward(x * 3 / self.sides + x)
            t.left(360 / self.sides + 1)
            t.width(x * self.sides / 180)
            t.left(91)

if __name__ == '__main__':
    star().hello().run()