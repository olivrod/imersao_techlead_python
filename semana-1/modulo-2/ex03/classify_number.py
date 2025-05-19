import sys

def se_par(n: int) -> bool:
    '''verifica se o numero informado é par'''
    if n % 2 == 0:
        return True
    else:
        return False

def se_positivo(n: int) -> bool:
    '''verifica se o numero informado é positivo'''
    if n > 0:
        return True
    else:
        return False

def classify_number(n: int) -> str:
    '''classifica o numero informado'''
    if n == 0:
        return "zero"
    if se_par(n):
        par_impar = 'par'
    else:
        par_impar = 'impar'

    if se_positivo(n):
        positivo_negativo = 'positivo'
    else:
        positivo_negativo = 'negativo'

    return positivo_negativo + ' e ' + par_impar


if __name__ == "__main__":
    num = int(sys.argv[1])
    print(classify_number(num))
