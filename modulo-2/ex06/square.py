import sys

def retangulo(n: int) -> None:
    topo_base = '%---%'
    
    print(topo_base)
    i = 0
    while i < n - 2:
        j = 0
        linha = ''
        while j < n:
            if j == 0:
                linha += '|'
            elif j == n - 1:
                linha += '|'
            else:
                linha += ' '
            j += 1
        print(linha)
        i += 1
    print(topo_base)

if __name__ == "__main__":
    '''Printa um retangulo conforme os lados enviados'''
    n = int(sys.argv[1])
    retangulo(n)

