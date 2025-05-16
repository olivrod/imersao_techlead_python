import sys

def shrink(valor: str) -> str:
    ''' retorna as 8 primeiras posicoes da string '''
    return valor[slice(0, 8)]

def enlarge(valor: str) -> str:
    ''' retorna Z nos espaços em branco até 8 posicoes totais da string'''
    return valor.ljust(8, "Z")

if __name__ == "__main__":
    '''Complementa com Z qndo menos de 8 caracteres na string ou apenas imprime
    a string caso maior q 8 caracteres'''
    valores = sys.argv[1:]

    if not valores:
        print(None)
    else:
        for valor in valores:
            if len(valor) > 8:
                print(shrink(valor))
            elif len(valor) < 8:
                print(enlarge(valor))
            elif len(valor) == 8:
                print(valor)
    
