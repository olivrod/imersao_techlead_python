import sys

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # a numero anterio
    # b numero atual
    a, b = 0, 1
    count = 1
    while count < n:
        # O novo a vira o valor anterior de b (avanço da sequência)
        # O novo b vira a soma de a + b (o próximo número de Fibonacci)
        a, b = b, a + b
        # a linha acima é a mesma coisa do que:
        # temp = b
        # b = a + b
        # a = temp

        count += 1
    return b
    # Quando o loop termina, b contém o valor de F(n) (o n-ésimo número de Fibonacci)

if __name__ == "__main__":
    '''programa que recebe um número n inteiro como parâmetro e imprime o n-ésimo elemento da sequencia fibonacci'''
    n = int(sys.argv[1])
    print(fibonacci(n))
