# ************************************************************************** */
#
#                                                        :::      ::::::::  
#   less26_pygame2.py                                  :+:      :+:    :+:
#                                                    +:+ +:+         +:+    
#   By: wmiyu <wmiyu@student.21-school.ru>         +#+  +:+       +#+   
#                                                +#+#+#+#+#+   +#+        
#   Created: 07.02.2023 A.D.                          #+#    #+#       
#                                                    #+#   #+#+#+#+#  
#   Description:
# ************************************************************************** */

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My first Less26 window")
game_over = False
bg_color = (0, 30, 0)
myimage = pygame.image.load("pycharm.bmp").convert()
myimage = pygame.transform.scale(myimage, (64, 64))



x = 10
y = 20
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                x -= 20
            if event.key == pygame.K_RIGHT:
                x += 20
            if event.key == pygame.K_UP:
                y -= 20
            if event.key == pygame.K_DOWN:
                y += 20
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
    screen.fill(bg_color)
    screen.blit(myimage, (x, y))
    pygame.display.flip()

