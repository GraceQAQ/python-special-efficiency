#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 一行代码之打印爱心
#
#                   @File Name    : line_1.py
#
#                   @Programmer   : autofelix
#
#                   @Start Date   : 2022/01/13 13:14
#
#                   @Last Update  : 2022/01/13 13:14
#
#-------------------------------------------------------------------
'''
print('\n'.join([''.join([('Autofelix520'[(x-y)%10]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))