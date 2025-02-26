while True:
    numero_1 = input("Digite o primeiro número: ")
    numero_2 = input("Digite o segundo número: ")
    operador = input("Digite o operador (+-/*): ")

    num_valid = None
    ope_valid = '+-/*'
    num_1 = 0
    num_2 = 0

    try:
        num_1 = float(numero_1)
        num_2 = float(numero_2)
        num_valid = True
        
    except Exception:
        num_valid = None

    if num_valid is None:
        print('Um dos números digitados são invalidos.')
        continue
    if operador not in ope_valid or len(operador) > 1 or operador == '':
        print('Operador invalido')
        continue
    
    print('Confira o resultado de sua operação abaixo')
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Não deveria chegar aqui')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break