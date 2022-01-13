#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 可视化进度条六
#
#                   @File Name    : progress_6.py
#
#                   @Programmer   : autofelix
#
#                   @Start Date   : 2022/01/13 13:14
#
#                   @Last Update  : 2022/01/13 13:14
#
#-------------------------------------------------------------------
'''
import PySimpleGUI as sg
import time


class progress:
 '''
  This is a main Class, the file contains all documents.
  One document contains paragraphs that have several sentences
  It loads the original file and converts the original file to new content
  Then the new content will be saved by this class
 '''

 def __init__(self):
  self.mylist = [1, 2, 3, 4, 5, 6, 7, 8]

 def hello(self):
  '''
  This is a welcome speech
  :return: self
  '''
  print('*' * 50)
  print(' ' * 20 + '可视化进度条六')
  print(' ' * 5 + '作者: autofelix  Date: 2022-01-13 13:14')
  print(' ' * 5 + '主页: https://autofelix.blog.csdn.net')
  print('*' * 50)
  return self

 def run(self):
  '''
  The program entry
  '''
  for i, item in enumerate(self.mylist):
   sg.one_line_progress_meter('This is my progress meter!', i + 1, len(self.mylist), '-key-')
   time.sleep(1)


if __name__ == '__main__':
 progress().hello().run()