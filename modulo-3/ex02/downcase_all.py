import sys

def downcase_it(valor: str) -> None:
    '''Retorna string em maiusculo'''
    return valor.lower()

if __name__ == "__main__":
    ''''Retorna a string em maiusculo'''
    # ignora o primeiro argumento que é o nome do arquivo python e pega todos os demais
    valores = sys.argv[1:]

    if not valores:
        print(None)
    else:
        for valor in valores:
            print(downcase_it(valor))

