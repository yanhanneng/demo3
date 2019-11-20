# -*- coding:utf-8 -*-

import pygame  # 导入动态模块(.dll .pyd .so) 不需要在包名后边跟模块名
from pygame.locals import *
import sys

# 定义常量(定义后,不再改值)
WINDOW_HEIGHT = 768
WINDOW_WIDTH = 512


def main():
    """主函数  一般将程序的入口"""
    pygame.init()
    # 创建窗口  set_mode((窗口尺寸))
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # 将图片加载到内存中  load(图片资源路径)
    bg_img = pygame.image.load("images/1.png")

    while True:
        # 贴图 把图片贴到窗口中  blit(图片对象, 相对原点的坐标)
        window.blit(bg_img, (0, 0))
        # 刷新界面  不刷新不会更新显示的内容
        pygame.display.update()
        # 获取事件，比如按键等  先显示界面,再根据获取的事件,修改界面效果
        for event in pygame.event.get():
            # 判断是否是点击了退出按钮
            if event.type == QUIT:
                sys.exit()  # 让程序终止
                pygame.quit()
            # 判断是否是按下了键
            elif event.type == KEYDOWN:
                # 检测按键是否是空格键
                if event.key == K_SPACE:
                    print("space")
                elif event.key == K_LEFT:
                    print("left")
                elif event.key == K_RIGHT:
                    print("right")

if __name__ == '__main__':  # 判断是否主动执行该文件
    main()