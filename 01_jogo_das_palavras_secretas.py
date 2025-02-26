import os


palavra_secreta = 'perfume' #palavra secreta
letras_acertadas = '' #quantidade de letras que o jogador acertou
tentativas = 1 #quantidade de tentativas que o jogador fez
maxima_tentativas = 10 #numero maximo de tentativas que um jogador pode tentar

while True:
    letra_digitada = input('Dite uma letra: ')
    tentativas += 1 
    maxima_tentativas -= 1 

    if len(letra_digitada) > 1: #verifica se o jogador inseriu apenas uma letra
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta: #Verifica se a letra digitada esta contida na palavra secreta e caso True concatena na letras_acertadas
        letras_acertadas += letra_digitada

    palavra_formada = ''

    for letra_secreta in palavra_secreta: #Caro a letra estiver correta ele concatena na posição onde a letra se encontra dentro da plavra secreta, caso contrario exibe "*"
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    if maxima_tentativas == 0: #Caso o numero de tentativas chegue a 0 o programa fecha
        print('Suas tentativas acabaram')
        print('A palavra secreta era:', palavra_secreta)
        break

    print(palavra_formada)
    print("Tentativas restantes", maxima_tentativas)
    
    if palavra_formada == palavra_secreta: #Caso o usuario acerte todas as letras
        os.system('cls')
        print("Você acertou a palvra")
        print("A palavra secreta é:", palavra_secreta)
        print("Numero de tentativas:", tentativas)
        break

    