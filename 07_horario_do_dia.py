hora = input('Digite a hora em numeros inteiros: ')

try:
    horas = int(hora)

    if horas >= 0 and horas <= 11:
        print('bom dia')

    elif horas >= 12 and horas <= 17:
        print('boa tarde')
    
    elif horas >= 13 and horas <= 23:
        print('boa noite')
    
    else:
        print('Não conheço esta hora')

except:
    print('Não digitou um numero inteiro')
