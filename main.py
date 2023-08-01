from pygame import *
from random import randint
init()

closeall = False
while closeall != True:
    w = display.set_mode((1500, 750))
    display.set_caption('snake game')
    head = rect.Rect(250, 100, 10, 10)
    body = []
    x = 240
    y = 100
    for i in range(6):
        body.append(rect.Rect(x, y, 10, 10))
        x -= 10
    food = rect.Rect((randint(0, 149) * 10), (randint(0, 74) * 10), 10, 10)
    clock = time.Clock()
    close = False
    move_up = False
    move_left = False
    move_down = False
    move_right = True
    while close != True:
        w.fill((0, 0, 0))
        for i in event.get():
            if i.type == QUIT:
                close = True
                closeall = True
            if i.type == KEYDOWN:
                if (i.key == K_w or i.key == K_UP) and move_down == False:
                    move_up = True
                    move_left = False
                    move_down = False
                    move_right = False
                if (i.key == K_a or i.key == K_LEFT) and move_right == False:
                    move_up = False
                    move_left = True
                    move_down = False
                    move_right = False
                if (i.key == K_s or i.key == K_DOWN) and move_up == False:
                    move_up = False
                    move_left = False
                    move_down = True
                    move_right = False
                if (i.key == K_d or i.key == K_RIGHT) and move_left == False:
                    move_up = False
                    move_left = False
                    move_down = False
                    move_right = True
        if move_up:
            head.y -= 10
        if move_left:
            head.x -= 10
        if move_down:
            head.y += 10
        if move_right:
            head.x += 10
        draw.rect(w, (0, 0, 255), head)
        xofpreviousrect = head.x
        yofpreviousrect = head.y
        for i in body:
            xofthisrect = i.x
            yofthisrect = i.y
            i.x = xofpreviousrect
            i.y = yofpreviousrect
            xofpreviousrect = xofthisrect
            yofpreviousrect = yofthisrect
            draw.rect(w, (0, 0, 255), i)
        counter = 0
        for i in body:
            if counter > 0:
                if i.colliderect(head):
                    close = True
            counter += 1
        if head.colliderect(food):
            body.append(rect.Rect(xofpreviousrect, yofpreviousrect, 10, 10))
            food.x = (randint(0, 149) * 10)
            food.y = (randint(0, 74) * 10)
        if head.x < 0 or head.x > 1490 or head.y < 0 or head.y > 740:
            close = True
        draw.rect(w, (0, 255, 0), food)
        display.update()
        clock.tick(20)
    score = len(body) - 6
    close = False
    while close != True:
        w.fill((0, 0, 0))
        w.blit(font.SysFont('Arial', 50).render('score: ' + str(score) + ' (1-try again)', True, (255, 0, 0)), (100, 100))
        if closeall:
            close = True
        for i in event.get():
            if i.type == QUIT:
                closeall = True
            if i.type == KEYDOWN and i.key == K_1:
                close = True
        display.update()
        clock.tick(60)