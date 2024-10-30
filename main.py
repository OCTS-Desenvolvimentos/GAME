import pygame
from pygame.locals import *
from sys import exit
import math, time
import random

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
    mensagens = ['Era uma vez um ogro muito solitário.(aperte enter para continuar)', 'Ele gostava muito de comer, de dormir, cantar e ficar dentro de sua casa.', 'Sua comida favorita é o mel, apenas doce como algodão e leve como o voar das abelhas.', 'Certo dia, seus amigos, burro e gato de botas, notaram sua ausência nos encontros mensais', '"Hey Shrek, o que anda acontecendo, amigo?"', "- Disse seu amigo, burro.", '"Não é nada, burro, apenas me deixe em paz."', '-Retrucou o ogro', '"Ora, ogro, teñes brigado com tu dama, Fiona, mas una vez? Meow."', '-Brincou gato de botas', '"Fiona está perfeitamente bem. Eu apenas estou com problemas sérios."', '"Mas cuanta formalidade para um ogrito, huh? Deixe gato de botas resolver o problema!"', '"Gato, não se trata de perigo, eu fui condenado, não existo mais no conto de fadas."', '"O que?!" -Exclamou o burro.', '"Desde que falhei no ensino médio, Marcelo e Patrícia rasgaram meu conto de fadas."', '"A única maneira de remontar minha história é respondendo os desafios."', '"Ora mas que dessssafios son esses, huh?" -indagou gato de botas', '"Precisamos, digo, preciso responder as prguntas que Marcelo e Patrícia fizeram."', '"Caso contrário, as crianças esquecerão de mim!"', '"Bom... eu sei que sou um burro, mas posso ajudar."', '"Este desafio não é páreo para o gato!"', '"Haha! Obrigado meus amigos."', '"Espere... eu sei quem pode ajudar." - Sugeriu o burro.', '"Ora, mas quem?" - Perguntou Shrek', '"Exatamente este usuário que está ouvindo nossa conversa!"', 'DESEJA ACEITAR O DESAFIO? [sim(pressione M)] [não(pressione ENTER)]', 'Haha! Era uma pegadinha! Não existe a opção de declinar. Boa sorte!']
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
    cenario = pygame.transform.scale(pygame.image.load("img/cenario1.jpg"), (tela_width, tela_height))

    while True:
        tela.blit(cenario, (0, 0))
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

  # Limpa a tela
        tela.blit(professor_matematica, professor_rect.topleft) 
        tela.blit(shrek.image, player.topleft)
        
        toad_sprites.update()
        relogio.tick(30)
        pygame.display.flip()

def perguntas_mat():
    desafios_matematica = [
        Desafio("Qual é o valor de ∫₀¹ (3x² - 2x + 1) dx?", {'a': '1/3', 'b': '1/2', 'c': '5/6', 'd': '2/3'}, 'c'),
        Desafio("Qual é a derivada de f(x) = 4x³ - 3x² + 2x - 1?", {'a': '12x² - 6x + 2', 'b': '12x² - 6x', 'c': '8x² - 6x + 2', 'd': '12x² + 6x + 2'}, 'a'),
        Desafio("Qual é o limite de limₓ→₀ (sin(5x)/x)?", {'a': '0', 'b': '1', 'c': '5', 'd': '10'}, 'c'),
        Desafio("Qual é a soma dos ângulos internos de um hexágono?", {'a': '540°', 'b': '720°', 'c': '900°', 'd': '1080°'}, 'b'),
        Desafio("Qual é a equação da reta que passa pelos pontos (1, 2) e (3, 4)?", {'a': 'y = x + 1', 'b': 'y = 2x', 'c': 'y = x + 1', 'd': 'y = 2x - 1'}, 'a'),
        Desafio("Qual é a solução da equação x² - 5x + 6 = 0?", {'a': 'x = 2 ou x = 3', 'b': 'x = 1 ou x = 6', 'c': 'x = 0 ou x = 5', 'd': 'x = -2 ou x = -3'}, 'a'),
        Desafio("Qual é o valor de e⁰?", {'a': '0', 'b': '1', 'c': 'e', 'd': '∞'}, 'b'),
        Desafio("Qual é o valor de log₁₀(100)?", {'a': '1', 'b': '2', 'c': '3', 'd': '4'}, 'b'),
        Desafio("Qual é a integral de ∫ x⁴ dx?", {'a': '1/5 x⁵ + C', 'b': '1/4 x⁴ + C', 'c': '4x³ + C', 'd': '5x⁵ + C'}, 'a'),
        Desafio("Qual é o valor de √144?", {'a': '10', 'b': '11', 'c': '12', 'd': '14'}, 'c'),
        Desafio("Qual é o valor de f(1) se f(x) = 2x² + 3x - 5?", {'a': '0', 'b': '1', 'c': '2', 'd': '3'}, 'a'),
        Desafio("Qual é o valor de tan(45°)?", {'a': '0', 'b': '1', 'c': '2', 'd': '∞'}, 'b'),
        Desafio("Qual é a fórmula do termo geral de uma PA?", {'a': 'aₙ = a₁ + (n - 1)r', 'b': 'aₙ = a₁rⁿ', 'c': 'aₙ = a₁ + nr', 'd': 'aₙ = a₁ * r'}, 'a'),
        Desafio("Qual é o resultado de limₓ→∞ (1/x)?", {'a': '0', 'b': '1', 'c': '∞', 'd': 'Não existe'}, 'a'),
        Desafio("Qual é a equação da circunferência com centro na origem e raio 4?", {'a': 'x² + y² = 4', 'b': 'x² + y² = 16', 'c': 'x² - y² = 16', 'd': 'x² - y² = 4'}, 'b'),
        Desafio("Qual é a soma dos quadrados dos primeiros n números naturais?", {'a': 'n(n + 1)(2n + 1)/6', 'b': '(n²)(n + 1)/2', 'c': 'n(n + 1)/2', 'd': 'n²(n + 1)²/4'}, 'a'),
        Desafio("Qual é a fórmula do binômio de Newton?", {'a': '(a + b)ⁿ = Σₖ₌₀ⁿ C(n, k)aⁿ⁻ᵏbᵏ', 'b': '(a + b)ⁿ = aⁿ + bⁿ', 'c': '(a - b)ⁿ = Σₖ₌₀ⁿ C(n, k)aᵏbⁿ⁻ᵏ', 'd': '(a + b)ⁿ = n(a + b)'}, 'a'),
        Desafio("Qual é a razão áurea?", {'a': '(1 + √5)/2', 'b': '(1 - √5)/2', 'c': '√5/2', 'd': '√2'}, 'a'),
        Desafio("Qual é a solução da equação exponencial 2ˣ = 16?", {'a': '2', 'b': '3', 'c': '4', 'd': '5'}, 'c'),
        Desafio("Qual é a fórmula para a área de um triângulo?", {'a': 'base * altura / 2', 'b': 'base + altura', 'c': 'base * altura', 'd': '(base + altura) / 2'}, 'a'),
        Desafio("Qual é o coeficiente de x² na expansão de (x + 2)³?", {'a': '4', 'b': '6', 'c': '8', 'd': '12'}, 'b'),
        Desafio("Qual é a integral definida de f(x) = x entre 1 e 3?", {'a': '2', 'b': '3', 'c': '4', 'd': '5'}, 'd'),
        Desafio("Qual é a solução da equação 3x - 2 = 10?", {'a': '2', 'b': '4', 'c': '5', 'd': '6'}, 'c'),
        Desafio("Qual é o resultado de 5!/3!?", {'a': '10', 'b': '15', 'c': '20', 'd': '25'}, 'c'),
        Desafio("Qual é o valor de d/dx(e²ˣ)?", {'a': 'e²ˣ', 'b': '2e²ˣ', 'c': '3e²ˣ', 'd': '4e²ˣ'}, 'b'),
    ]
    random.shuffle(desafios_matematica)  # Embaralha as perguntas


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
        tela.blit(vidas_surface, (650, 90))

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
    Desafio("Qual é o antônimo de 'fácil'?", {'a': 'Simples', 'b': 'Difícil', 'c': 'Rápido', 'd': 'Prático'}, 'b'),
    Desafio("Qual das palavras abaixo está grafada corretamente?", {'a': 'Acento', 'b': 'Acêrto', 'c': 'Xegada', 'd': 'Estério'}, 'a'),
    Desafio("Qual a classe gramatical da palavra 'sorridente' na frase 'Ela estava sorridente'?", {'a': 'Substantivo', 'b': 'Verbo', 'c': 'Adjetivo', 'd': 'Advérbio'}, 'c'),
    Desafio("Assinale a frase em que o verbo foi utilizado no futuro do pretérito.", {'a': 'Eu vou estudar amanhã.', 'b': 'Eu estudaria se pudesse.', 'c': 'Eu estudarei com você.', 'd': 'Eu estou estudando agora.'}, 'b'),
    Desafio("Em 'Ele pediu para que você viesse', o verbo 'viesse' está no:", {'a': 'Pretérito perfeito', 'b': 'Futuro do presente', 'c': 'Futuro do pretérito', 'd': 'Pretérito imperfeito do subjuntivo'}, 'd'),
    Desafio("Qual das palavras abaixo leva acento diferencial?", {'a': 'Pera', 'b': 'Para', 'c': 'Pelo', 'd': 'Pôde'}, 'd'),
    Desafio("Qual é o plural da palavra 'cidadão'?", {'a': 'Cidadãos', 'b': 'Cidadões', 'c': 'Cidades', 'd': 'Cidadães'}, 'a'),
    Desafio("Qual das opções abaixo completa corretamente a frase 'Ela é _____ de todos'?", {'a': 'A mais simpática', 'b': 'A simpática mais', 'c': 'A mais simpatia', 'd': 'A simpatia mais'}, 'a'),
    Desafio("Assinale a frase com uso correto da crase.", {'a': 'Vou à casa da Maria.', 'b': 'Vou a escola.', 'c': 'Estarei a disposição.', 'd': 'Ele foi à pé.'}, 'a'),
    Desafio("Na frase 'A moça cantou e dançou alegremente', a palavra 'alegremente' é um:", {'a': 'Verbo', 'b': 'Advérbio', 'c': 'Substantivo', 'd': 'Adjetivo'}, 'b'),
    Desafio("Assinale a alternativa correta para o plural de 'carro-chefe'.", {'a': 'Carros-chefes', 'b': 'Carro-chefes', 'c': 'Carros-chefe', 'd': 'Carro-chefe'}, 'a'),
    Desafio("Qual é o sujeito da oração 'Vão chegar três novos alunos'?", {'a': 'Oculto', 'b': 'Indeterminado', 'c': 'Simples', 'd': 'Composto'}, 'c'),
    Desafio("Qual palavra completa a frase 'Ela tem medo de andar _____ escuro'?", {'a': 'Ao', 'b': 'À', 'c': 'No', 'd': 'Na'}, 'c'),
    Desafio("Assinale a alternativa onde o verbo está no modo subjuntivo.", {'a': 'Ela correu rápido.', 'b': 'Se ela correr rápido, vencerá.', 'c': 'Ela correrá rápido.', 'd': 'Ela está correndo.'}, 'b'),
    Desafio("Na frase 'A cidade parece vazia', a palavra 'vazia' funciona como:", {'a': 'Verbo', 'b': 'Predicativo do sujeito', 'c': 'Predicado', 'd': 'Objeto direto'}, 'b'),
    Desafio("Qual das palavras abaixo está incorreta quanto à acentuação?", {'a': 'Médica', 'b': 'Característica', 'c': 'Avós', 'd': 'Dificil'}, 'd'),
    Desafio("Qual o significado da palavra 'pródigo'?", {'a': 'Pobre', 'b': 'Econômico', 'c': 'Generoso', 'd': 'Eficiente'}, 'c'),
    Desafio("Assinale a frase com pontuação correta:", {'a': 'Hoje eu fui a feira e comprei maçãs laranjas e bananas.', 'b': 'Hoje, eu fui à feira, e comprei maçãs, laranjas e bananas.', 'c': 'Hoje eu fui à feira e comprei maçãs, laranjas e bananas.', 'd': 'Hoje eu fui a feira, e comprei maçãs laranjas, e bananas.'}, 'c'),
    Desafio("Qual das frases está correta quanto ao uso do 'porque'?", {'a': 'Ele não veio, por que estava chovendo.', 'b': 'Ele não veio porque estava chovendo.', 'c': 'Ele não veio porquê estava chovendo.', 'd': 'Ele não veio, porque estava chovendo.'}, 'b'),
    Desafio("Em 'O aluno estudava quando o professor chegou', qual a classificação da oração 'quando o professor chegou'?", {'a': 'Subordinada adjetiva', 'b': 'Subordinada substantiva', 'c': 'Subordinada adverbial temporal', 'd': 'Principal'}, 'c'),
    Desafio("Qual a função da palavra 'que' na frase 'O carro que comprei é novo'?", {'a': 'Pronome possessivo', 'b': 'Pronome demonstrativo', 'c': 'Pronome relativo', 'd': 'Pronome interrogativo'}, 'c'),
    Desafio("Qual o sinônimo de 'efêmero'?", {'a': 'Duradouro', 'b': 'Passageiro', 'c': 'Estável', 'd': 'Lento'}, 'b'),
    Desafio("Qual é a função da vírgula em 'Maria, venha aqui!'?", {'a': 'Enumeração', 'b': 'Vocativo', 'c': 'Aposto', 'd': 'Elipse'}, 'b'),
    Desafio("Qual das palavras está incorreta quanto ao uso do hífen?", {'a': 'Ex-aluno', 'b': 'Super-resistente', 'c': 'Vice-presidente', 'd': 'Anti-inflamatório'}, 'b'),
    Desafio("Na frase 'Estou com muito sono', a expressão 'muito sono' é:", {'a': 'Objeto direto', 'b': 'Objeto indireto', 'c': 'Complemento nominal', 'd': 'Predicativo do sujeito'}, 'a'),
    Desafio("Qual a classe gramatical de 'caminhando' em 'Ela estava caminhando'?", {'a': 'Substantivo', 'b': 'Verbo', 'c': 'Adjetivo', 'd': 'Advérbio'}, 'b'),
    Desafio("Assinale a frase em que ocorre ambiguidade:", {'a': 'A menina comprou uma bolsa nova.', 'b': 'Eles resolveram viajar no final de semana.', 'c': 'João viu o cachorro do irmão na varanda.', 'd': 'O professor estava explicando a matéria.'}, 'c'),
    Desafio("Na frase 'Ela própria organizou o evento', a palavra 'própria' é um:", {'a': 'Pronome reflexivo', 'b': 'Pronome possessivo', 'c': 'Pronome demonstrativo', 'd': 'Pronome enfático'}, 'd'),
    Desafio("Qual a figura de linguagem em 'Esse carro voa!'?", {'a': 'Metáfora', 'b': 'Antítese', 'c': 'Paradoxo', 'd': 'Ironia'}, 'a'),
    Desafio("Assinale a alternativa onde há uso correto da palavra 'mal':", {'a': 'Ele está se sentindo mau.', 'b': 'Ele sempre trata mal os amigos.', 'c': 'Ele acordou de bom mal.', 'd': 'Esse trabalho está muito mal feito.'}, 'b'),

    ]
    random.shuffle(desafios_portugues)
    
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

    tela_fisica()
     

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