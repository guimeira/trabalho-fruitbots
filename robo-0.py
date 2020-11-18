#Modifique este arquivo para implementar seu robô.
#Para mais detalhes, leia a especificação do trabalho.

#Adicione aqui os imports que forem necessários:
import random

#Escolha um nome para o seu robô. Quanto mais zueira, melhor!
nome = 'Robô 0'

#Você deve implementar esta função para fazer a jogada do seu robô.
#Esta função recebe 4 parâmetros:
#arena: dicionário contendo as dimensões da arena.
#  Exemplo: {'linhas': 5, 'colunas': 7}
#
#frutas: lista de dicionários contendo a localização de cada fruta.
#  Exemplo: [
#    {'tipo': 0, 'linha': 3, 'coluna': 8},
#    {'tipo': 1, 'linha': 0, 'coluna': 2},
#    {'tipo': 1, 'linha': 3, 'coluna': 1}
#  ]
#  O parâmetro 'tipo' segue o padrão:
#    0 = melancia
#    1 = banana
#    2 = maçã
#
#robo: dicionário contendo o estado atual do robô.
#  Exemplo: {'linha': 4, 'coluna': 2, 'frutas': [2.0, 1.0, 0.0] }
#  O parâmetro 'frutas' contém a quantidade de cada fruta que o robô já coletou.
#  Esse parâmetro é uma lista. A posição 0 é o número de melancias, a posição 1
#  é o número de bananas e a posição 2 é o número de maçãs.
#
#adversarios: lista de dicionários contendo todos os robôs adversários.
#  Exemplo: [ {'linha': 0, 'coluna': 2, 'frutas': [3.0, 2.0, 1.0] } ]
#  Para este trabalho, você pode assumir que existe apenas um robô adversário.
#
#O retorno da função deve ser a direção escolhida para o movimento do seu robô.
#Os valores disponíveis são: 'BAIXO', 'CIMA', 'DIREITA' e 'ESQUERDA'.
def jogar(arena, frutas, robo, adversarios):
    return random.choice(['BAIXO', 'CIMA', 'DIREITA', 'ESQUERDA'])