import random

def palavra_aleatoria(lista):
    return random.choice(lista)

def localizar(texto, caractere):
    return [i for i, l in enumerate(texto) if l == caractere]

def desenho_forca(tentativas):
    estagios = [
        """
           -----
           |   |
               |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        """
    ]
    return estagios[tentativas]

def obter_caractere(caracteres_usados):
    while True:
        caractere_digitado = input('Digite somente um caractere: ').upper()
        if len(caractere_digitado) != 1:
            print("Por favor, digite apenas um único caractere.")
        elif caractere_digitado in caracteres_usados:
            print("Você já usou esse caractere. Tente outro.")
        else:
            return caractere_digitado

def jogo_da_forca():
    print('----x----x---- JOGO DA FORCA ----x----x----')

    temas = {
        'frutas': ['LIMAO', 'ABACAXI', 'JABUTICABA', 'UVA', 'MELANCIA', 'ABACATE', 'MORANGO', 'LARANJA', 'PEQUI'],
        'animais': ['CACHORRO', 'GATO', 'ELEFANTE', 'GIRAFA', 'ZEBRA'],
        'paises': ['BRASIL', 'ARGENTINA', 'CANADA', 'JAPAO', 'EGITO']
    }

    dicas = {
        'frutas': "É algo que você pode comer.",
        'animais': "É um ser vivo que se move por conta própria.",
        'paises': "É um lugar onde as pessoas vivem."
    }

    tema = random.choice(list(temas.keys()))
    print(f'----- ADIVINHE O NOME DE UM(A) {tema.upper()} -----\n')

    palavra = palavra_aleatoria(temas[tema])
    print(f'DICA: {dicas[tema]} A palavra tem {len(palavra)} caracteres')

    pal_secreta = ['_' for _ in palavra]
    fim_do_jogo = False
    caracteres_usados = []
    tentativas = 0

    while not fim_do_jogo:
        print(desenho_forca(tentativas))
        print(f'Caracteres usados: {", ".join(caracteres_usados)}')
        print(' '.join(pal_secreta))  # Parêntese de fechamento estava faltando aqui

        caractere_digitado = obter_caractere(caracteres_usados)
        caracteres_usados.append(caractere_digitado)

        if caractere_digitado in palavra:
            print(f'O caractere {caractere_digitado} está contido na palavra')
            posicoes = localizar(palavra, caractere_digitado)

            for i in posicoes:
                pal_secreta[i] = caractere_digitado
        else:
            tentativas += 1

        if '_' not in pal_secreta:
            fim_do_jogo = True
            print("Parabéns, você ganhou!")
            print(f"A palavra era {palavra}")
        elif tentativas == 6:
            fim_do_jogo = True
            print("Você perdeu!")
            print(f"A palavra era {palavra}")

    # Adicione o link para o GitHub
    print("\nPara dar seu feedback e contribuir com o código, acesse: https://github.com/aldapandre/PYTHON-GITHUB/tree/main")

jogo_da_forca()
