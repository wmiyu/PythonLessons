# ************************************************************************** */
#
#                                                        :::      ::::::::  
#   less27_pygame2.py                                  :+:      :+:    :+:
#                                                    +:+ +:+         +:+    
#   By: wmiyu <wmiyu@student.21-school.ru>         +#+  +:+       +#+   
#                                                +#+#+#+#+#+   +#+        
#   Created: 07.02.2023 A.D.                          #+#    #+#       
#                                                    #+#   #+#+#+#+#  
#   Description: Use <- ARROW -> KEYS to move, ESC for Exit
# ************************************************************************** */

import pygame
import random

from pygame import Surface, SurfaceType

W_WIDTH = 1024
W_HEIGHT = 768
IMG_SIZE = 96


def random_bg_color():
    return random.randint(0, 30), random.randint(0, 30), random.randint(0, 30)


def show_text(on_screen: Surface, w_bg_color: pygame.Color):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text_surf: Surface | SurfaceType = font.render('Use <- ARROW KEYS ->  to move, F for Fullscreen, ESC for Exit', True, (100,100,100), w_bg_color)
    text_surf.set_alpha(127)
    text_rect = text_surf.get_rect()
    text_rect.bottomleft = (20, W_HEIGHT)
    on_screen.blit(text_surf, text_rect)


pygame.init()
screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
pygame.display.set_caption("Welcome Player1 to game!")
game_over = False
bg_color = (0, 30, 0)
myimage = pygame.image.load("pycharm.bmp").convert()
myimage = pygame.transform.scale(myimage, (IMG_SIZE, IMG_SIZE))

x = (W_WIDTH - IMG_SIZE) / 2
y = (W_HEIGHT - IMG_SIZE) / 2

move_right = False
move_left = False
move_up = False
move_down = False
full_screen = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_f:
                if not full_screen:
                    screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT), pygame.FULLSCREEN)
                    full_screen = True
                else:
                    screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
                    full_screen = False
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
        if event.type == pygame.MOUSEMOTION:
            bg_color = random_bg_color()
    if move_right and x < W_WIDTH - IMG_SIZE:
        x += 1
    if move_left and x >= 1:
        x -= 1
    if move_up and y >= 1:
        y -= 1
    if move_down and y < W_HEIGHT - IMG_SIZE:
        y += 1
    screen.fill(bg_color)
    screen.blit(myimage, (x, y))
    show_text(screen, bg_color)
    pygame.display.flip()

