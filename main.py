from random import choice
from random_words import palavras

print(' > JOGO DA FORCA < '.center(30, '='))

# Palavra secreta sorteada
palavra_secreta = choice(palavras)
# Chances do Usuário
chances = 4
# Tentativa de letras do Usuário
tentativas_usuario = []

# Loop principal
while True:
    # Estrutura para informar quantas chances o Usuário tem
    if chances > 1:
        print(f'Você tem {chances} chances')
    else:
        print(f'Você só tem {chances} chance')

    # Laço para imprimir as letras acertadas pelo usuário
    for letra in palavra_secreta:
        if letra in tentativas_usuario:
            print(letra, end=' ')
        else:
            print('_', end=' ')

    print()
    # Tentativa do Usuário
    letra_usuario = str(input('Digite uma letra: ')).strip().lower()

    # Estrutura para verificar e validar a tentativa do Usuário
    if letra_usuario.isalpha() and len(letra_usuario) == 1:
        if letra_usuario in tentativas_usuario:
            print('Você já tentou essa letra. Tente outra. ')
        elif letra_usuario in palavra_secreta:
            tentativas_usuario.append(letra_usuario)
        else:
            chances -= 1
    else:
        print('Por favor, digite somente letras')
    print('=' * 30)

    # Tratando o caso em que o jogador vence
    if set(palavra_secreta) == set(tentativas_usuario):
        print(f'Você venceu! A palavra secreta era {palavra_secreta.upper()}')
        break
    # Tratando o caso em que o jogador perde
    elif chances == 0:
        print(f'Você perdeu. A palavra secreta era {palavra_secreta.upper()}')
        break
