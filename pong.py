import pygame, sys, random

def ball_animation():
    global ball_speed_x,ball_speed_y, player_score, opponent_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top<=0 or ball.bottom>=screen_heigth:
        ball_speed_y *= -1

    if ball.left<=0 or ball.right>=screen_width:
        if ball.left<=0:
            player_score+=1
        if ball.right>=screen_width:
            opponent_score+=1
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top=0
    if player.bottom >= screen_heigth:
        player.bottom=screen_heigth

def opponent_ai():
    if opponent.top<ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top=0
    if opponent.bottom >= screen_heigth:
        opponent.bottom=screen_heigth

def ball_restart():
    global ball_speed_x,ball_speed_y
    ball.center = (screen_width/2, screen_heigth/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))

pygame.init()

clock = pygame.time.Clock()

screen_width=800
screen_heigth=600
fuente=pygame.font.SysFont('Arial',30)
texto=fuente.render("[0-0]",0,(255,255,255))

screen=pygame.display.set_mode((screen_width, screen_heigth))

pygame.display.set_caption('Pong')

ball = pygame.Rect(screen_width/2-15, screen_heigth/2-15,30,30)
player = pygame.Rect(screen_width-20, screen_heigth/2-70,10,140)
opponent = pygame.Rect(10, screen_heigth/2-70, 10,140)

bg_color = pygame.Color('grey12')
ligth_grey=pygame.Color(200,200,200)
red=pygame.Color(255,0,0)

ball_speed_x=7*random.choice((1,-1))
ball_speed_y=7*random.choice((1,-1))
player_speed=0
opponent_speed=20
player_score=0
opponent_score=0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed+=7
            if event.key == pygame.K_UP:
                player_speed-=7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed-=7
            if event.key == pygame.K_UP:
                player_speed+=7

    ball_animation()
    player_animation()
    opponent_ai()

    screen.fill(bg_color)
    pygame.draw.rect(screen, ligth_grey, player)
    pygame.draw.rect(screen, ligth_grey, opponent)
    pygame.draw.rect(screen, red, ball)
    pygame.draw.aaline(screen, ligth_grey, (screen_width/2,0), (screen_width/2,screen_heigth))
    texto=fuente.render("[{}-{}]".format(opponent_score, player_score),0,(255,255,255))
    screen.blit(texto,((screen_width/2)-30,15))

    pygame.display.flip()
    clock.tick(60)