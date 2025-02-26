nome = input('Qual seu nome: ')

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])
print()

indice = 0 
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'

    #print(nome[indice])
    indice += 1 

novo_nome += '*'
print(novo_nome)
