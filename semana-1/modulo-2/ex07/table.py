import sys
from typing import List

def table(n: int) -> List[int]:
    # tabela de multiplicacao
    resultado = []
    i = 0
    while i <= 10:
        resultado.append(n * i)
        i += 1
    return resultado

if __name__ == "__main__":
    '''Exibe tabelas de multiplicacao. Se passado parametro exibe apenas a tabela
    do parametro informado, caso contrario exibe até 9'''
    # Verifica se tem alem do nome do arquivo o parametro passado no comando python3
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        resultado = table(n)
        print(f"Table of {n}:", * resultado)
    else:
        i = 0
        while i < 10:
            resultado = table(i)
            print(f"Table of {i}:", * resultado)
            i += 1
