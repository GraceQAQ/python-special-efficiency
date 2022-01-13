#!/usr/bin/env python
# encoding: utf-8
'''
#-------------------------------------------------------------------
#                   CONFIDENTIAL --- CUSTOM STUDIOS
#-------------------------------------------------------------------
#
#                   @Project Name : 黑客帝国代码雨
#
#                   @File Name    : main.py
#
#                   @Programmer   : autofelix
#
#                   @Start Date   : 2022/01/14 13:14
#
#                   @Last Update  : 2022/01/14 13:14
#
#-------------------------------------------------------------------
'''
import random, pygame

class matrix:
    '''
     This is a main Class, the file contains all documents.
     One document contains paragraphs that have several sentences
     It loads the original file and converts the original file to new content
     Then the new content will be saved by this class
    '''
    def __init__(self):
        self.panel_width = 1800
        self.panel_height = 1000
        self.font_size = 15

    def hello(self):
        '''
        This is a welcome speech
        :return: self
        '''
        print('*' * 50)
        print(' ' * 20 + '黑客帝国代码雨')
        print(' ' * 5 + '作者: autofelix  Date: 2022-01-14 13:14')
        print(' ' * 5 + '主页: https://autofelix.blog.csdn.net')
        print('*' * 50)
        return self

    def run(self):
        '''
        The program entry
        '''
        print('\033[1;31;0m')
        print('↓' * 20 + ' 类型选择: ' + '↓' * 20)
        print('0：数字代码雨 1：字符代码雨')
        print('\033[0m')
        type = input('请选择代码雨类型：')
        self.rain(type)

    def rain(self, type):
        pygame.init()
        win = pygame.display.set_mode((self.panel_width, self.panel_height))

        font = pygame.font.SysFont('SimHei', 22)
        rain_type = type if type in [0, 1] else 0
        texts = self.digital_text(font) if rain_type == 0 else self.word_text(font)

        bg_surface = pygame.Surface((self.panel_width, self.panel_height), flags=pygame.SRCALPHA)
        pygame.Surface.convert(bg_surface)
        bg_surface.fill(pygame.Color(0, 0, 0, 28))
        win.fill((0, 0, 0))

        # 按屏幕的宽带计算可以在画板上放几列坐标并生成一个列表
        column = int(self.panel_width / self.font_size)
        drops = [0 for i in range(column)]

        while True:
            # 从队列中获取事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:

                    chang = pygame.key.get_pressed()
                    if (chang[32]):
                        exit()

            # 将暂停一段给定的毫秒数
            pygame.time.delay(30)

            # 重新编辑图像第二个参数是坐上角坐标
            win.blit(bg_surface, (0, 0))

            for i in range(len(drops)):
                text = random.choice(texts)
                # 重新编辑每个坐标点的图像
                win.blit(text, (i * self.font_size, drops[i] * self.font_size))
                drops[i] += 1
                if drops[i] * 10 > self.panel_height or random.random() > 0.95:
                    drops[i] = 0

            pygame.display.flip()

    def digital_text(self, font):
        return [font.render(str(i), True, (0, 255, 0)) for i in range(10)]

    def word_text(self, font):
        letter = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
        return [font.render(str(letter[i]), True, (0, 255, 0)) for i in range(26)]

if __name__ == '__main__':
    matrix().hello().run()