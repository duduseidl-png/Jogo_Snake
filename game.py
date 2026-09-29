import pygame

from pygame.locals import *
from sys import exit
from random import randint 

pygame.init()

pygame.mixer.music.set_volume(0.01)
musica_de_fundo = pygame.mixer.music.load('BoxCat_Games_–_CPU_Talk.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')
barulho_colisao.set_volume(0.1)

largura = 640 #Criação da variável largura (x) da tela
altura = 480 #Criação da variável altura (y) da tela
x_cobra = int(largura/2) #Criação da variável X da posição do objeto retangulo na tela. largura/2 igual ao meio. Canto superior esquero começa a criação x.
y_cobra = int(altura/2) #Criação da variável Y da posição do objeto retangulo na tela. altura/2 igual ao meio. Canto superior esquero começa a criação y.

velocidade = 10

x_controle = velocidade
y_controle = 0

x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake")
relogio = pygame.time.Clock() #FPS do jogo/rapidez de como acontece as coisas
lista_cobra = []
comprimento_inicial = 5
morreu = False

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, x_controle, y_controle, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura/2)
    y_cobra = int(altura/2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    x_controle = velocidade
    y_controle = 0
    morreu = False
    pygame.mixer.music.play(-1)


#Estrutura de repetição
while True:
    relogio.tick(30)
    tela.fill((255,255,255))

    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        #Definição de teclas apenas ao acionar
        
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
                
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
        
    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20)) #variáveis x_azul e y_azul mudam a posição conforme condição IF.

    #Verifica se o retangulo vermelho colidiu com o azul. SE colidiu a função randint vai mudar de posição.
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)

        pontos = pontos + 1

        barulho_colisao.play()

        comprimento_inicial = comprimento_inicial + 1

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem1 = 'Game Over!'
        mensagem2 = f'Pontuação Final: {pontos}'
        mensagem3 = 'Pressione R para reiniciar'
        
        
        texto_formatado1 = fonte2.render(mensagem1, True, (0,0,0))
        texto_formatado2 = fonte2.render(mensagem2, True, (0,0,0))
        texto_formatado3 = fonte2.render(mensagem3, True, (0,0,0))
        ret_texto1 = texto_formatado1.get_rect()
        ret_texto2 = texto_formatado2.get_rect()
        ret_texto3 = texto_formatado3.get_rect()
        morreu = True
        pygame.mixer.music.stop()
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto1.center = (largura//2, altura//2 - 40)
            ret_texto2.center = (largura//2, altura//2)
            ret_texto3.center = (largura//2, altura//2 + 40)
            tela.blit(texto_formatado1, ret_texto1)
            tela.blit(texto_formatado2, ret_texto2)
            tela.blit(texto_formatado3, ret_texto3)  
            pygame.display.update()

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0

            
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)
        
    tela.blit(texto_formatado, (10,10))
    pygame.display.update()
