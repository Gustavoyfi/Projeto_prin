import pygame
import sys

#iniciando tela
pygame.init()


#configurando tela
largura = 800
altura = 500
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("JOGO BÃO")


#imagem de fundo da tela
background_imagem = pygame.image.load('puc.jpg')

#Largura e altura dos botões
botao_largura, botao_altura = 120, 120

#Carregando a foto
personagem_adryan = pygame.image.load('adryan.jpg').convert_alpha()
personagem_gustavo = pygame.image.load('gustavo.png').convert_alpha()
personagem_kelvin = pygame.image.load('kelvin.jpg').convert_alpha()
personagem_caio = pygame.image.load('zeca.jpeg').convert_alpha()

#Lista dos personagens
personagens = [personagem_adryan, personagem_gustavo, personagem_kelvin, personagem_caio]

#classe do botão
class Button():
    def __init__(self, x, y, imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (x, y)
    def draw(self):
        #Desenhando borda preta
        pygame.draw.rect(tela, (0, 0, 0), self.rect.inflate(8, 8))
        #desenhando o botão na tela
        tela.blit(self.imagem, (self.rect.x, self.rect.y))
    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

#Calculando a coordenada x
espacamento_horizontal = 20
total_largura_botoes = botao_largura * len(personagens) + espacamento_horizontal * (len(personagens) - 1)
x_inicial = (largura - total_largura_botoes) // 2

# Criando botões para cada personagem
botoes = []
x = x_inicial
for i, personagem in enumerate(personagens):
    personagem_redimensionada = pygame.transform.scale(personagem, (botao_largura, botao_altura))
    botao = Button(x, 200, personagem_redimensionada)
    botoes.append(botao)
    x += botao_largura + espacamento_horizontal

#loop do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for botao in botoes:
                    if botao.is_clicked(event.pos):
                        if botao == botoes[0]:
                            print("Adryan selecionado!")
                        elif botao == botoes[1]:
                            print("Gustavo selecionado!")
                        elif botao == botoes[2]:
                            print("Kelvin selecionado!")
                        elif botao == botoes[3]:
                            print("Caio selecionado!")
    tela.blit(background_imagem, (0, 0))
    for botao in botoes:
        botao.draw()
    pygame.display.update()
