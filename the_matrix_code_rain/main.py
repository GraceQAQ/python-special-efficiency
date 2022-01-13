#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date  : 2019/7/23
import random
import pygame

PANEL_width = 1800
PANEL_highly = 1000
FONT_PX = 15

pygame.init()

# 创建一个可是窗口
winSur = pygame.display.set_mode((PANEL_width, PANEL_highly))

font = pygame.font.SysFont('SimHei', 22)

bg_suface = pygame.Surface((PANEL_width, PANEL_highly), flags=pygame.SRCALPHA)

pygame.Surface.convert(bg_suface)

bg_suface.fill(pygame.Color(0, 0, 0, 28))

winSur.fill((0, 0, 0))

# 数字版
# texts = [font.render(str(i), True, (0, 255, 0)) for i in range(10)]

# 字母版
letter = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c',
          'v', 'b', 'n', 'm']
texts = [
    font.render(str(letter[i]), True, (0, 255, 0)) for i in range(26)
]

# 按屏幕的宽带计算可以在画板上放几列坐标并生成一个列表
column = int(PANEL_width / FONT_PX)
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
    winSur.blit(bg_suface, (0, 0))

    for i in range(len(drops)):
        text = random.choice(texts)

        # 重新编辑每个坐标点的图像
        winSur.blit(text, (i * FONT_PX, drops[i] * FONT_PX))

        drops[i] += 1
        if drops[i] * 10 > PANEL_highly or random.random() > 0.95:
            drops[i] = 0

    pygame.display.flip()