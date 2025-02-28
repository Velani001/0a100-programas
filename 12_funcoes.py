def mult(*args):
    total = 1

    for number in args:
        total *= number 
    return total
        
multiplicar = mult(1,2,3,4,5)
print(multiplicar, '\n--------')

#-----------------------------

def par_impar(numero):
    verificador = numero % 2 == 0

    if verificador:
        return f'O {numero} par'
    return f'O {numero} é ímpar'

print(par_impar(3))
print(par_impar(10))
print(par_impar(35))
print(par_impar(102934))