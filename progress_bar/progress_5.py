#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 可视化进度条五
#
#                   @File Name    : progress_5.py
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
from alive_progress import alive_bar

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
  print(' ' * 20 + '可视化进度条五')
  print(' ' * 5 + '作者: autofelix  Date: 2022-01-13 13:14')
  print(' ' * 5 + '主页: https://autofelix.blog.csdn.net')
  print('*' * 50)
  return self

 def run(self):
  '''
  The program entry
  '''
  items = range(100)
  with alive_bar(len(items)) as bar:
   for item in items:
     bar()
     time.sleep(1)

if __name__ == '__main__':
 progress().hello().run()