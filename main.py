import pygame
from pygame.locals import *
from sys import exit
import math, time

pygame.init()

tela_width = 800
tela_height = 600

tela = pygame.display.set_mode((tela_width, tela_height))
pygame.display.set_caption("Shrek - A Volta as Aulas")

font = pygame.font.Font(None, 48)

pygame.mixer.music.set_volume(0.15)
som_principal = pygame.mixer.music.load('06. Snowboard Mountain Theme.mp3')
pygame.mixer.music.play(-1)

som_acertos = pygame.mixer.Sound('smw_coin.wav')
som_acertos.set_volume(1)

som_erros = pygame.mixer.Sound('smw_lemmy_wendy_incorrect.wav')
som_erros.set_volume(1)

relogio = pygame.time.Clock()
class Shrek(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        for i in range(0, 8):
            self.sprites.append(pygame.image.load(f"img/shrek2ofilme/sprite_{i}.png"))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (64*2, 64*2))
        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100
        self.animar = False
    def banana(self):
        self.animar = True
    def update(self):
        if self.animar == True:
            self.atual += 0.4
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (64*2, 64*2))
            
    
shrek = Shrek()
toad_sprites = pygame.sprite.Group()
toad_sprites.add(shrek)
    
class Desafio:
    def __init__(self, pergunta, opcoes, resposta_correta):
        self.pergunta = pergunta
        self.opcoes = opcoes
        self.resposta_correta = resposta_correta

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)
               
def get_font(size):
    return pygame.font.Font("img/font (1).ttf", size)

def tela_inicial():
    while True:
        tela.fill((0, 0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXTO = get_font(30).render("SHREK - BACK TO SCHOOL", True, "#2F922F")
        MENU_RECT = MENU_TEXTO.get_rect(center=(420, 100))

        BOTAO_JOGAR = Button(image=pygame.image.load("img/Play Rect.png"), pos=(394, 250), 
                            text_input="JOGAR", font=get_font(25), base_color="#d7fcd4", hovering_color="Green")
        BOTAO_SAIR = Button(image=pygame.image.load("img/Quit Rect.png"), pos=(394, 420), 
                            text_input="SAIR", font=get_font(25), base_color="#d7fcd4", hovering_color="Green")

        tela.blit(MENU_TEXTO, MENU_RECT)

        for button in [BOTAO_JOGAR, BOTAO_SAIR]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(tela)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BOTAO_JOGAR.checkForInput(MENU_MOUSE_POS):
                    caixa_dialogo()
                if BOTAO_SAIR.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()

        pygame.display.update()

def caixa_dialogo():
    cenario = pygame.transform.scale(pygame.image.load("img/background.webp"), (tela_width, tela_height))
    font = pygame.font.Font(None,25)
    mensagens = ['Era uma vez um ogro muito solitário.', 'Ele gostava muito de comer, de dormir, cantar e ficar dentro de sua casa.', 'Sua comida favorita é o mel, apenas doce como algodão e leve como o voar das abelhas.', 'Certo dia, seus amigos, burro e gato de botas, notaram sua ausência nos encontros mensais', '"Hey Shrek, o que anda acontecendo, amigo?"', "- Disse seu amigo, burro.", '"Não é nada, burro, apenas me deixe em paz."', '-Retrucou o ogro', '"Ora, ogro, teñes brigado com tu dama, Fiona, mas una vez? Meow."', '-Brincou gato de botas', '"Fiona está perfeitamente bem. Eu apenas estou com problemas sérios."', '"Mas cuanta formalidade para um ogrito, huh? Deixe gato de botas resolver o problema!"', '"Gato, não se trata de perigo, eu fui condenado, não existo mais no conto de fadas."', '"O que?!" -Exclamou o burro.', '"Desde que falhei no ensino médio, Marcelo e Patrícia rasgaram meu conto de fadas."', '"A única maneira de remontar minha história é respondendo os desafios."', '"Ora mas que dessssafios son esses, huh?" -indagou gato de botas', '"Precisamos, digo, preciso responder as prguntas que Marcelo e Patrícia fizeram."', '"Caso contrário, as crianças esquecerão de mim!"', '"Bom... eu sei que sou um burro, mas posso ajudar."', '"Este desafio não é páreo para o gato!"', '"Haha! Obrigado meus amigos."', '"Espere... eu sei quem pode ajudar." - Sugeriu o burro.', '"Ora, mas quem?" - Perguntou Shrek', '"Exatamente este usuário que está ouvindo nossa conversa!"', 'DESEJA ACEITAR O DESAFIO? [sim(pressione M)] [não(pressione ENTER)]', 'Haha! Era uma pegadinha! Não existe a opção de declinar. Boa sorte!']
    if not mensagens:
         jogo()
         return
    snip = font.render('', True, 'white')
    contador = 0
    velo_texto = 3
    done = False
    timer = pygame.time.Clock()
    mensagem = font.render("Aperte E para pular o diálogo", True, (169,169,169))
    mensagem_ativa = 0
    message = mensagens[mensagem_ativa]

    while True:
        tela.blit(cenario, (0, 0))
        tela.blit(mensagem, (30, 0))
        pygame.draw.rect(tela, 'black', [0, 400, 800, 200])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit() 
                
            if event.type == pygame.KEYDOWN:
                if event.key == K_e:
                    jogo() 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done:
                    mensagem_ativa += 1
                    if mensagem_ativa < len(mensagens):
                        done = False
                        message = mensagens[mensagem_ativa]
                        contador = 0
                    else:
                        jogo()
                        return
                         
                 
        if contador < velo_texto * len(message):
                    contador += 1
        elif contador >= velo_texto * len(message):
                    done = True
        snip = font.render(message[0:contador//velo_texto], True, 'white')
        tela.blit(snip, (10, 410))

        pygame.display.flip()
        timer.tick(60)
            

def jogo():
    player = pygame.Rect(shrek)
    professor_matematica = pygame.image.load("img/marcelo.png")
    professor_matematica = pygame.transform.scale(professor_matematica, (90, 90))
    professor_rect = professor_matematica.get_rect(topright=(tela_width, 40))
    velocidade = 8
    toad_sprites.draw(tela)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            player.x -= velocidade
            shrek.banana()
            shrek.image = pygame.transform.flip(shrek.image, True, False)    
        if keys[K_RIGHT]:
            player.x += velocidade
            shrek.banana()
        if keys[K_UP]:
            player.y -= velocidade
            shrek.banana()
        if keys[K_DOWN]:
            player.y += velocidade
            shrek.banana()
        if not keys[K_DOWN] and not keys[K_RIGHT] and not keys[K_UP] and not keys[K_LEFT]:
            shrek.animar = False
        if player.colliderect(professor_rect):
            perguntas_mat()  # Chama as perguntas quando o player encosta no professor

        tela.fill((255, 235, 205))  # Limpa a tela
        tela.blit(professor_matematica, professor_rect.topleft) 
        tela.blit(shrek.image, player.topleft)
        
        toad_sprites.update()
        relogio.tick(30)
        pygame.display.flip()

def perguntas_mat():
    desafios_matematica = [
        Desafio("Qual é a média de 9, 9 e 9?", {'a': '9', 'b': '10', 'c': '8', 'd': '7'}, 'a'),
        Desafio("Quanto é 70 + 20?", {'a': '90', 'b': '91', 'c': '89', 'd': '88'}, 'a'),
        Desafio("Qual é a soma de 90 e 10?", {'a': '100', 'b': '99', 'c': '101', 'd': '102'}, 'a'),
        Desafio("Quanto é 100 ÷ 2?", {'a': '50', 'b': '51', 'c': '49', 'd': '48'}, 'a'),
        Desafio("Qual é a média de 4, 6 e 8?", {'a': '6', 'b': '7', 'c': '5', 'd': '4'}, 'a'),
        Desafio("Quanto é 45 + 55?", {'a': '100', 'b': '99', 'c': '101', 'd': '102'}, 'a'),
        Desafio("Qual é a soma de 5 e 5?", {'a': '10', 'b': '9', 'c': '8', 'd': '7'}, 'a'),
        Desafio("Quanto é 16 - 8?", {'a': '8', 'b': '7', 'c': '6', 'd': '5'}, 'a'),
        Desafio("Qual é a soma de 14 e 5?", {'a': '19', 'b': '18', 'c': '20', 'd': '17'}, 'a'),
        Desafio("Quanto é 8 + 6?", {'a': '14', 'b': '13', 'c': '12', 'd': '11'}, 'a'),
    ]

    player_vidas = 3
    indice_desafio = 0

    while True:
        tela.fill((222, 255, 154))  # Preenche a tela com amarelo claro

        if indice_desafio >= len(desafios_matematica):
            break  # Sai do loop se todos os desafios foram respondidos

        desafio_atual = desafios_matematica[indice_desafio]

        
        pergunta_surface = font.render(desafio_atual.pergunta, True, (0, 0, 0))
        tela.blit(pergunta_surface, (50, 50))

        
        y_offset = 100
        for key, value in desafio_atual.opcoes.items():
            opcao_surface = font.render(f"{key}) {value}", True, (0, 0, 0))
            tela.blit(opcao_surface, (50, y_offset))
            y_offset += 50

        # Renderiza as vidas
        vidas_surface = font.render(f'Vidas: {player_vidas}', True, (255, 0, 0))
        tela.blit(vidas_surface, (650, 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key in [K_a, K_b, K_c, K_d]:
                    resposta = chr(event.key)  # Converte a tecla pressionada para a letra
                    if resposta == desafio_atual.resposta_correta:
                        som_acertos.play()
                        indice_desafio += 1
                    else:
                        som_erros.play()
                        player_vidas -= 1  # Diminui a vida se a resposta estiver errada
                        if player_vidas <= 0:
                            fim_de_jogo()  # Chama a tela de fim de jogo

    tela_branca()  # Chama a próxima tela se todas as perguntas forem certas

def tela_branca():
    player = pygame.Rect(shrek)
    velocidade = 8
    professora_portugues = pygame.image.load("img/patricia.png")
    professora_portugues = pygame.transform.scale(professora_portugues, (90,90))
    professora_rect = professora_portugues.get_rect(topleft=(80, 500))  # Coloca a professora no canto superior esquerdo
    toad_sprites.draw(tela)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            shrek.banana()
            shrek.image = pygame.transform.flip(shrek.image, True, False) 
            player.x -= velocidade
        if keys[K_RIGHT]:
            shrek.banana()
            player.x += velocidade
        if keys[K_UP]:
            shrek.banana()
            player.y -= velocidade
        if keys[K_DOWN]:
            shrek.banana()
            player.y += velocidade
        if not keys[K_DOWN] and not keys[K_RIGHT] and not keys[K_UP] and not keys[K_LEFT]:
            shrek.animar = False   

        if player.colliderect(professora_rect):
            perguntas_port()  # Chama as perguntas de portugues ao colidir

        tela.fill((255, 235, 205))  # Limpa a tela
        tela.blit(professora_portugues, professora_rect.topright)
        tela.blit(shrek.image, player.topleft)
        
        toad_sprites.update()
        relogio.tick(30)
        pygame.display.flip()

def perguntas_port():
    desafios_portugues = [
        Desafio("Qual a forma correta da palavra: 'excessão'?", {'a': 'exceção', 'b': 'excessão', 'c': 'exessão', 'd': 'excessão'}, 'a'),
        Desafio("Qual é o sinônimo de 'feliz'?", {'a': 'triste', 'b': 'contente', 'c': 'descontente', 'd': 'irritado'}, 'a'),
        Desafio("Qual a forma correta da palavra: 'excessão'?", {'a': 'exceção', 'b': 'excessão', 'c': 'exessão', 'd': 'excessão'}, 'a'),
        Desafio("Qual é o sinônimo de 'feliz'?", {'a': 'triste', 'b': 'contente', 'c': 'descontente', 'd': 'irritado'}, 'a'),
        Desafio("Como se escreve a forma correta do verbo: 'ele (verbo) os amigos'?", {'a': 'viu', 'b': 'ver', 'c': 'vi', 'd': 'vê'}, 'a'),
        Desafio("Qual é a palavra com erro de ortografia?", {'a': 'proffessor', 'b': 'professor', 'c': 'professora', 'd': 'professores'}, 'a'),
        Desafio("Qual é a forma correta do plural da palavra 'cidadão'?", {'a': 'cidadãos', 'b': 'cidadãs', 'c': 'cidadão', 'd': 'cidadões'}, 'a'),
        Desafio("Qual a frase correta?", {'a': 'Eu vou à praia.', 'b': 'Eu vou a praia.', 'c': 'Eu vou a praia', 'd': 'Eu vou a praia.'}, 'a'),
        Desafio("Qual é o antônimo de 'claro'?", {'a': 'luz', 'b': 'brilhante', 'c': 'escuro', 'd': 'transparente'}, 'a'),
        Desafio("Qual a forma correta da conjugação do verbo 'correr' na primeira pessoa do singular?", {'a': 'corri', 'b': 'corro', 'c': 'corre', 'd': 'correr'}, 'a'),
    ]
    
    indice_desafio = 0
    player_vidas = 3

    while True:
        tela.fill((255, 204, 255))  # Preenche a tela com a cor desejada

        if indice_desafio >= len(desafios_portugues):
            break

        desafio_atual = desafios_portugues[indice_desafio]

       
        pergunta_surface = font.render(desafio_atual.pergunta, True, (0, 0, 0))
        tela.blit(pergunta_surface, (20, 40))

       
        y_offset = 100
        for key, value in desafio_atual.opcoes.items():
            opcao_surface = font.render(f"{key}) {value}", True, (0, 0, 0))
            tela.blit(opcao_surface, (50, y_offset))
            y_offset += 50

        # Renderiza as vidas
        vidas_surface = font.render(f'Vidas: {player_vidas}', True, (255, 0, 0))
        tela.blit(vidas_surface, (650, 90))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key in [K_a, K_b, K_c, K_d]:
                    resposta = chr(event.key)
                    if resposta == desafio_atual.resposta_correta:
                        indice_desafio += 1
                        som_acertos.play()
                    else:
                        som_erros.play()
                        player_vidas -= 1  # Diminui a vida se a resposta estiver errada
                        if player_vidas <= 0:
                            fim_de_jogo()  # Chama a tela de fim de jogo

    tela_final() 

def fim_de_jogo():
    while True:
        tela.fill((0, 0, 0)) 
        mensagem = font.render("GAME OVER! :(", True, (255, 0, 0))
        mensagem2 = font.render("Pressione R para retornar a tela inicial", True, (255, 255, 255))
        tela.blit(mensagem, (120, 250))
        tela.blit(mensagem2, (120, 290))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_r:
                    tela_inicial()

def tela_final():
    while True:
        font = pygame.font.Font(None, 38)
        tela.fill((97, 7, 7)) 
        mensagem = font.render("PARABENS! VOCÊ COMPLETOU O JOGO", True, (255, 255, 255))
        tela.blit(mensagem, (120, 250))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    tela_inicial()  

rodando = True
while rodando:
    tela_inicial()  # Inicia a tela inicial