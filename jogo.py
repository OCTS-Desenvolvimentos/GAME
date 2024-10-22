import pygame
import random, math, time, sys

# Configurações iniciais do Pygame
pygame.init()

pygame.mixer.music.set_volume(0.4)
main_sound = pygame.mixer.music.load('06. Snowboard Mountain Theme.mp3')
pygame.mixer.music.play(-1)

som_acertos = pygame.mixer.Sound('smw_coin.wav')
som_acertos.set_volume(1)

som_erros = pygame.mixer.Sound('smw_lemmy_wendy_incorrect.wav')
som_erros.set_volume(1)

game_over_sound = pygame.mixer.Sound('smw_thunder.wav')

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Desafio de Perguntas")
font = pygame.font.Font(None, 36)

class Desafio:
    def __init__(self, pergunta, opcoes, resposta_certa):
        self.pergunta = pergunta
        self.opcoes = opcoes
        self.resposta_certa = resposta_certa
       
    def mostrar(self):
        return self.pergunta, list(self.opcoes.items())

def desenhar_mapa(jogador_pos, professor_pos):
    for x in range(0, 800, 40):
        for y in range(0, 600, 40):
            rect = pygame.Rect(x, y, 40, 40)
            pygame.draw.rect(screen, (200, 200, 200), rect, 1)
   
    # Desenhar o jogador
    pygame.draw.rect(screen, (0, 255, 0), (jogador_pos[0] * 40, jogador_pos[1] * 40, 40, 40))
    # Desenhar o professor
    pygame.draw.rect(screen, (255, 0, 0), (professor_pos[0] * 40, professor_pos[1] * 40, 40, 40))

def tela_inicial():
    while True:
        screen.fill([(math.sin(n + time.time()) + 1) * 127 for n in range(3)])  # Preencher com preto
        titulo = font.render("Shrek - A Volta as Aulas", True, (255, 255, 255))
        instrucoes = font.render("Pressione Enter para jogar", True, (255, 255, 255))
        
        screen.blit(titulo, (250, 250))
        screen.blit(instrucoes, (250, 300))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Chama a função jogar()

def jogar():
    # Desafios de Matemática
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
        Desafio("Qual é a média de 7, 7 e 7?", {'a': '7', 'b': '6', 'c': '8', 'd': '9'}, 'a'),
        Desafio("Quanto é 100 - 25?", {'a': '75', 'b': '74', 'c': '76', 'd': '77'}, 'a'),
        Desafio("Qual é a soma de 10 e 10?", {'a': '20', 'b': '19', 'c': '21', 'd': '22'}, 'a'),
        Desafio("Quanto é 2 x 5?", {'a': '10', 'b': '11', 'c': '9', 'd': '8'}, 'a'),
        Desafio("Qual é a média de 3, 3 e 3?", {'a': '3', 'b': '2', 'c': '4', 'd': '1'}, 'a'),
        Desafio("Quanto é 6 x 6?", {'a': '36', 'b': '35', 'c': '34', 'd': '33'}, 'a'),
        Desafio("Qual é a soma de 9 e 10?", {'a': '19', 'b': '20', 'c': '18', 'd': '17'}, 'a'),
        Desafio("Quanto é 10 - 5?", {'a': '5', 'b': '4', 'c': '6', 'd': '3'}, 'a'),
    ]

    # Desafios de Português
    desafios_portugues = [
        Desafio("Qual a forma correta da palavra: 'excessão'?", {'a': 'exceção', 'b': 'excessão', 'c': 'exessão', 'd': 'excessão'}, 'a'),
        Desafio("Qual é o sinônimo de 'feliz'?", {'a': 'triste', 'b': 'contente', 'c': 'descontente', 'd': 'irritado'}, 'b'),
        Desafio("Qual a forma correta da palavra: 'excessão'?", {'a': 'exceção', 'b': 'excessão', 'c': 'exessão', 'd': 'excessão'}, 'a'),
        Desafio("Qual é o sinônimo de 'feliz'?", {'a': 'triste', 'b': 'contente', 'c': 'descontente', 'd': 'irritado'}, 'b'),
        Desafio("Como se escreve a forma correta do verbo: 'ele (verbo) os amigos'?", {'a': 'viu', 'b': 'ver', 'c': 'vi', 'd': 'vê'}, 'a'),
        Desafio("Qual é a palavra com erro de ortografia?", {'a': 'proffessor', 'b': 'professor', 'c': 'professora', 'd': 'professores'}, 'a'),
        Desafio("Qual é a forma correta do plural da palavra 'cidadão'?", {'a': 'cidadãos', 'b': 'cidadãs', 'c': 'cidadão', 'd': 'cidadões'}, 'a'),
        Desafio("Qual a frase correta?", {'a': 'Eu vou à praia.', 'b': 'Eu vou a praia.', 'c': 'Eu vou a praia', 'd': 'Eu vou a praia.'}, 'a'),
        Desafio("Qual é o antônimo de 'claro'?", {'a': 'luz', 'b': 'brilhante', 'c': 'escuro', 'd': 'transparente'}, 'c'),
        Desafio("Qual a forma correta da conjugação do verbo 'correr' na primeira pessoa do singular?", {'a': 'corri', 'b': 'corro', 'c': 'corre', 'd': 'correr'}, 'b'),
        Desafio("Como se chama a divisão de sílabas na palavra 'computador'?", {'a': 'hiato', 'b': 'ditongo', 'c': 'sílaba', 'd': 'diptongo'}, 'c'),
        Desafio("Qual é a forma correta: 'fazer ele' ou 'fazer ele mesmo'?", {'a': 'fazer ele', 'b': 'fazer ele mesmo', 'c': 'fazer ele mesmo que', 'd': 'fazer ele mesma'}, 'b'),
        Desafio("Qual das palavras é um advérbio?", {'a': 'rapidamente', 'b': 'rápido', 'c': 'rápida', 'd': 'rapidez'}, 'a'),
        Desafio("Qual a forma correta do uso do pronome: 'Ela gosta de (ele, ele mesmo)'?", {'a': 'ele', 'b': 'ele mesmo', 'c': 'ele mesma', 'd': 'ele mesmo que'}, 'b'),
        Desafio("Como se escreve a forma correta do verbo: 'Eles (verbo) ao cinema'?", {'a': 'foram', 'b': 'fui', 'c': 'vão', 'd': 'vai'}, 'a'),
        Desafio("Qual é o erro na frase: 'A gente vamos ao parque.'?", {'a': 'gente', 'b': 'vamos', 'c': 'ao', 'd': 'parque'}, 'b'),
        Desafio("Qual a forma correta do plural da palavra 'cão'?", {'a': 'cães', 'b': 'cãos', 'c': 'cãoes', 'd': 'cão'}, 'a'),
        Desafio("Qual é o antônimo de 'diferente'?", {'a': 'igual', 'b': 'semelhante', 'c': 'variante', 'd': 'diverso'}, 'a'),
        Desafio("Qual é a frase correta?", {'a': 'Eles foram embora.', 'b': 'Eles foi embora.', 'c': 'Eles vão embora.', 'd': 'Ele foram embora.'}, 'a'),
        Desafio("Qual é a forma correta: 'Mais vale um pássaro na mão do que dois a (sol)'?", {'a': 'sol', 'b': 'sorte', 'c': 'correr', 'd': 'nada'}, 'a'),
        
    ]

    # Lista de professores e suas vidas
    professores = [("Marcelo", 10), ("Patricia", 15)]
    professor_atual = 0
    jogador_pos = [5, 5]
    professor_pos = [3, 3]  # Posição do professor
    sherek_vidas = 3
    running = True

    while running:
        screen.fill((255, 255, 255))
        desenhar_mapa(jogador_pos, professor_pos)

        # Verifica se o jogador encontrou o professor
        if jogador_pos == professor_pos:
            desafios_aleatorios = random.sample(desafios_matematica if professor_atual == 0 else desafios_portugues, len(desafios_matematica if professor_atual == 0 else desafios_portugues))
            current_question_index = 0
            current_question = desafios_aleatorios[current_question_index]
            pergunta, opcoes = current_question.mostrar()

            while True:  # Loop do quiz
                screen.fill((255, 255, 255))
                question_text = font.render(pergunta, True, (0, 0, 0))
                screen.blit(question_text, (50, 50))

                # Mostra as opções
                for i, (letra, opcao) in enumerate(opcoes):
                    option_text = font.render(f"{letra}) {opcao}", True, (0, 0, 0))
                    screen.blit(option_text, (50, 100 + i * 40))

                # Exibir vidas
                vida_professor_text = font.render(f"Vidas do {professores[professor_atual][0]}: {professores[professor_atual][1]}", True, (255, 0, 0))
                screen.blit(vida_professor_text, (500, 50))

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    elif event.type == pygame.KEYDOWN:
                        if event.key in [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d]:
                            resposta = chr(event.key)

                            # Verifica a resposta
                            if resposta == current_question.resposta_certa:
                                # Reduz uma vida do professor
                                professores[professor_atual] = (professores[professor_atual][0], professores[professor_atual][1] - 1)
                                som_acertos.play()
                                print("Resposta correta!")
                                if professores[professor_atual][1] == 0:
                                    print(f"Você derrotou {professores[professor_atual][0]}!")
                                    professor_atual += 1
                                    if professor_atual >= len(professores):
                                        print("Você derrotou todos os professores!")
                                        return  # Fim do jogo
                                    else:
                                        # Transição para o próximo professor
                                        professor_pos = [5, 5]  # Nova posição do próximo professor
                                        jogador_pos = [9, 10]  # Reseta a posição do jogador
                                        break  # Sai do loop do quiz
                                current_question_index += 1
                                if current_question_index >= len(desafios_aleatorios):
                                    print("Você completou todas as perguntas!")
                                    return
                                current_question = desafios_aleatorios[current_question_index]
                                pergunta, opcoes = current_question.mostrar()
                            else:
                                sherek_vidas -= 1
                                som_erros.play()
                                print("Resposta errada!")
                                if sherek_vidas == 0:
                                    game_over_sound.play()
                                    print("Game over! O Professor te reprovou!")
                                    return

        pygame.display.flip()

        # Checa eventos do teclado para movimento
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and jogador_pos[0] > 0:
                    jogador_pos[0] -= 1
                elif event.key == pygame.K_RIGHT and jogador_pos[0] < 19:
                    jogador_pos[0] += 1
                elif event.key == pygame.K_UP and jogador_pos[1] > 0:
                    jogador_pos[1] -= 1
                elif event.key == pygame.K_DOWN and jogador_pos[1] < 14:
                    jogador_pos[1] += 1

    pygame.quit()

# Iniciar o jogo
tela_inicial()  
jogar()