import sys

def valida_par(x: int) -> bool:
    '''valida se o numero é par'''
    return x % 2 == 0

def quadrado(x: int) -> int:
    '''retorna o quadrado do numero'''
    return x ** 2

if __name__ == "__main__":
    '''retorna o quadrado dos valores pares da lista enviada'''
    valores = sys.argv[1]
    numeros = list(map(int, valores.split()))

    pares = filter(valida_par, numeros)
    quadrados = map(quadrado, pares)

    print(f"Squared evens: {list(quadrados)}")

# python3 transform.py "1 2 3 4 5 6 7 8 9 10"