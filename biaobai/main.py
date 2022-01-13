import pygame
import random

# 设置游戏屏幕大小 这是一个常量
WIDTH, HEIGHT = 640, 480

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('FROM一个喜欢你很久的小哥哥')


# 标题
def title(text, screen, scale, color=(255, 0, 0)):
    font = pygame.font.SysFont('SimHei', WIDTH // (len(text) * 2))
    textRender = font.render(text, True, color)

    # 获取此图片的矩形框
    # textRect = textRender.get_rect()
    # textRect.midtop = (WIDTH/scale[0], HEIGHT/scale[1])
    # screen.blit(textRender, textRect)

    # 初始化文字的坐标
    screen.blit(textRender, (WIDTH / scale[0], HEIGHT / scale[1]))


# 按钮
def button(text, x, y, w, h, color, screen):
    pygame.draw.rect(screen, color, (x, y, w, h))
    font = pygame.font.SysFont('SimHei', 20)
    textRender = font.render(text, True, (0, 0, 0))
    textRect = textRender.get_rect()
    textRect.center = ((x + w / 2), (y + h / 2))
    screen.blit(textRender, textRect)


# 生成随机的位置坐标
def get_random_pos():
    x, y = random.randint(20, 620), random.randint(20, 460)
    return x, y


# 点击喜欢按钮后显示的页面
def show_like_interface(text, screen, color=(255, 0, 0)):
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont('SimHei', WIDTH // (len(text)))
    textRender = font.render(text, True, color)
    textRect = textRender.get_rect()
    textRect.midtop = (WIDTH / 2, HEIGHT / 2)
    screen.blit(textRender, textRect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


def main():
    pygame.init()
    clock = pygame.time.Clock()
    unlike_pos_x = 330
    unlike_pos_y = 250
    unlike_pos_width = 80
    unlike_pos_height = 40
    unlike_color = (0, 191, 255)

    like_pos_x = 180
    like_pos_y = 250
    like_pos_width = 80
    like_pos_height = 40
    like_color = (0, 191, 255)

    running = True
    while running:
        # 填充窗口
        screen.fill((255, 255, 255))

        img = pygame.image.load('d:/love2.png')
        imgRect = img.get_rect()
        imgRect.midtop = int(WIDTH / 1.3), HEIGHT // 7
        screen.blit(img, imgRect)

        # 获取坐标
        pos = pygame.mouse.get_pos()
        if pos[0] < unlike_pos_x + unlike_pos_width + 5 and pos[0] > unlike_pos_x - 5 and pos[
            1] < unlike_pos_y + unlike_pos_height + 5 and pos[1] > unlike_pos_y - 5:
            while True:
                unlike_pos_x, unlike_pos_y = get_random_pos()
                if pos[0] < unlike_pos_x + unlike_pos_width + 5 and pos[
                    0] > unlike_pos_x - 5 and \
                        pos[1] < unlike_pos_y + unlike_pos_height + 5 and pos[
                    1] > unlike_pos_y - 5:
                    continue
                break

        title('小姐姐，我观察你很久了', screen, scale=[5, 8])
        title('做我女朋友好不好呀', screen, scale=[5, 4])
        button('好呀', like_pos_x, like_pos_y, like_pos_width, like_pos_height, like_color, screen)
        button('算了吧', unlike_pos_x, unlike_pos_y, unlike_pos_width, unlike_pos_height, unlike_color, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if pos[0] < like_pos_x + like_pos_width + 5 and pos[0] > like_pos_x - 5 and pos[
            1] < like_pos_y + like_pos_height + 5 and pos[1] > like_pos_y - 5:
            show_like_interface('我就知道小姐姐你也喜欢我~', screen, color=(255, 0, 0))

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)


main()