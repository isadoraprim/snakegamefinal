
import pygame
import sys
import random

pygame.init()

# Configurações da tela
dis_width = 336
dis_height = 441
screen = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake Game")
snake_bloco = 15
snake_cabeca = pygame.image.load ("cabecadacobra1.png")
snake_speed = 8
clock = pygame.time.Clock()
fundo_imagem_menu = pygame.image.load('1.png')
fundo_imagem_over = pygame.image.load('fundo_imagem_over.png')

# Cores
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Fonte
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Função para desenhar texto na tela
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Função para a tela de início
def main_menu():
    while True:
        screen.fill(white)

        draw_text('            Início', score_font, black, screen, 50, 50)
        screen.blit(fundo_imagem_menu, (0, 0))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(100, 150, 150, 50)
        button_2 = pygame.Rect(100, 250, 150, 50)
        button_3 = pygame.Rect(100, 350, 150, 50)

        draw_text('  Jogar Agora', font_style, black, screen, 110, 160)
        draw_text('  Autores', font_style, black, screen, 130, 260)
        draw_text(' Sair', font_style, black, screen, 150, 360)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_1.collidepoint((mx, my)):
            if click:
                gameLoop()
        if button_2.collidepoint((mx, my)):
            if click:
                autores()
        if button_3.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.display.update()

# Função para a tela de autores
def autores():
    running = True
    while running:
        screen.fill(white)
        draw_text('Autores:', score_font, black, screen, 50, 50)
        draw_text('Arthur Zamboni', font_style, black, screen, 50, 150)
        draw_text('Isadora Prim', font_style, black, screen, 50, 200)
        draw_text('Mylena Cardoso', font_style, black, screen, 50, 250)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()

# Função para desenhar a cobra
def our_snake(snake_bloco, snake_list):
    for x in snake_list:
        screen.blit(snake_cabeca, [x[0], x[1], snake_bloco, snake_bloco])


# Função para exibir mensagens
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [dis_width / 3, dis_height / 3])

# Função principal do jogo
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_bloco) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_bloco) / 10.0) * 10.0

    while not game_over:

        while game_close is True:
            screen.blit(fundo_imagem_over, (0, 0))


            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_bloco
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_bloco
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_bloco
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_bloco
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(blue)
        pygame.draw.rect(screen, green, [foodx, foody, snake_bloco, snake_bloco])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_bloco, snake_List)

        pygame.display.update()

        # Criar retângulos para a cobra e a comida
        player_rect = pygame.Rect(x1, y1, snake_bloco, snake_bloco)
        food_rect = pygame.Rect(foodx, foody, snake_bloco, snake_bloco)

        # Verificar colisão entre os retângulos
        if player_rect.colliderect(food_rect):
            foodx = round(random.randrange(0, dis_width - snake_bloco) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_bloco) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Iniciar o jogo com a tela de início
main_menu()
