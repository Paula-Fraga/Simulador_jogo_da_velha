import numpy as np
import random

def criar_tabuleiro() :
     tabuleiro_vazio = np.array([
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ])  
     return tabuleiro_vazio
 
def possibilidades_restantes(tabuleiro):
    campos_vazios = []
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro)):
            if (tabuleiro[linha][coluna] == 0):
                campos_vazios.append((linha, coluna))
    return campos_vazios

def jogada_aleatoria(tabuleiro, jogador):
    campos_vazios = possibilidades_restantes(tabuleiro)
    campo_escolhido = random.choice(campos_vazios)
    tabuleiro[campo_escolhido] = jogador
    return tabuleiro

def analise_de_match_no_tabuleiro(tabuleiro, jogador):
        
    # Vertical e Horizontal
    for linha in range(len(tabuleiro)):
        match_linha = True
        match_coluna = True
        
        for coluna in range(len(tabuleiro)):
            
            # Analisa a linha
            if tabuleiro[linha][coluna] != jogador:
                match_linha = False
            
            # Analisa a coluna 
            if tabuleiro[coluna][linha] != jogador:
                match_coluna = False           
        
        if match_linha == True or match_coluna == True:
            return True
                 
    # Diagonais
    match_direita = True
    match_esquerda = True
    for x in range(len(tabuleiro)):
        
        if tabuleiro[x, x] != jogador:
            match_direita = False
            
        y = -1 -x
        if tabuleiro[x, y] != jogador:
            match_esquerda = False      
    
    
    if match_direita == True or match_esquerda == True:
        return True   
        
    return False

def ver_vencedor(tabuleiro):
    vencedor = False
    
    
    jogadores = [1, 2]
    for jogador in jogadores:
        
        venceu = analise_de_match_no_tabuleiro(tabuleiro, jogador)
        
        if venceu :
            vencedor = jogador
            break
    
    return vencedor

def play_game():
    tabuleiro = criar_tabuleiro()
    ganhador = ver_vencedor(tabuleiro)
    jogada = 1
    
    while(ganhador == False):
        
        for jogador in [1, 2]:
            if jogada != 9:
                tabuleiro = jogada_aleatoria(tabuleiro, jogador)
                ganhador = ver_vencedor(tabuleiro)
                jogada = jogada + 1
            else:
                ganhador = -1
                break
    return ganhador

print("Jogo com 500 partidas:")

palmeiras = 0
corinthians = 0
empate = 0
count = 0

while (count < 500):
    vencedor = play_game()
    
    if vencedor == 1:
        palmeiras = palmeiras + 1
    elif vencedor == 2:
        corinthians = corinthians + 1
    else:
        empate = empate + 1
        
    count = count + 1
        
print("Palmeiras ganhou: ", palmeiras, " vezes.")
print("Corinthians: ", corinthians, " vezes.")
print("Deu Empate: ", empate, " vezes.")

print("====================================")

print("Jogo com 1000 partidas:")

palmeiras = 0
corinthians = 0
empate = 0
count = 0

while (count < 1000):
    vencedor = play_game()
    
    if vencedor == 1:
        palmeiras = palmeiras + 1
    elif vencedor == 2:
        corinthians = corinthians + 1
    else:
        empate = empate + 1
        
    count = count + 1
        
print("Palmeiras ganhou: ", palmeiras, " vezes.")
print("Corinthians: ", corinthians, " vezes.")
print("Deu Empate: ", empate, " vezes.")

print("====================================")

print("Jogo com 2000 partidas:")

palmeiras = 0
corinthians = 0
empate = 0
count = 0

while (count < 2000):
    vencedor = play_game()
    
    if vencedor == 1:
        palmeiras = palmeiras + 1
    elif vencedor == 2:
        corinthians = corinthians + 1
    else:
        empate = empate + 1
        
    count = count + 1
        
print("Palmeiras ganhou: ", palmeiras, " vezes.")
print("Corinthians: ", corinthians, " vezes.")
print("Deu Empate: ", empate, " vezes.")

print("====================================")

print("Jogo com 5000 partidas:")

palmeiras = 0
corinthians = 0
empate = 0
count = 0

while (count < 5000):
    vencedor = play_game()
    
    if vencedor == 1:
        palmeiras = palmeiras + 1
    elif vencedor == 2:
        corinthians = corinthians + 1
    else:
        empate = empate + 1
        
    count = count + 1
        
print("Palmeiras ganhou: ", palmeiras, " vezes.")
print("Corinthians: ", corinthians, " vezes.")
print("Deu Empate: ", empate, " vezes.")


        
        
        
        