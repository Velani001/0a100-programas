frase = input("Digite uma palavra ou frase: ")

i = 0
ap_vezes = 0
letra_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i+=1
        continue
    
    ap_letra = frase.count(letra_atual)

    if ap_vezes < ap_letra:
        ap_vezes = ap_letra
        letra_vezes = letra_atual

                           
    #print(letra_atual, ap_letra)
    i+=1

print(f'A letra que apareceu mais vezes foi "{letra_vezes}" {ap_vezes}x')