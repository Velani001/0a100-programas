# função que multiplica x numeros 
def mult(*args):
    total = 1

    for number in args:
        total *= number 
    return total
        
multiplicar = mult(1,2,3,4,5)
print(multiplicar, '\n--------')

#-----------------------------
# função que verifica se um determinado numero é par ou impar
def par_impar(numero):
    verificador = numero % 2 == 0

    if verificador:
        return f'O {numero} par'
    return f'O {numero} é ímpar'

print(par_impar(3))
print(par_impar(10))
print(par_impar(35))
print(par_impar(102934), '\n--------')

#-----------------
# função que da saudações ao usuario
usuario = input('Qual seu nome: ')

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

bom_dia = criar_saudacao('Bom dia')
boa_noite = criar_saudacao("Boa noite")
boa_tarde = criar_saudacao("Boa tarde")

print(bom_dia(usuario))
print(boa_noite(usuario))
print(boa_tarde(usuario), '\n--------')

#-----------------
# função que multiplica um numero passado pelo usuario
num = input('Qual o numero a ser multiplicado: ')
num = int(num)

def multiplicator(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = multiplicator(2)
triplicar = multiplicator(3)
quadruplicar = multiplicator(4)
print(duplicar(num))
print(triplicar(num))
print(quadruplicar(num))

