#Este é o robô adversário. Você não precisa modificar este arquivo,
#a menos que você queira testar sua estratégia contra alguma outra.
import random

nome = 'Robô 1'

def jogar(arena, frutas, robo, adversarios):
    return random.choice(['BAIXO', 'CIMA', 'DIREITA', 'ESQUERDA'])