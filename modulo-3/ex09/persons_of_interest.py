def get_year(cientista: dict) -> int:
    '''retorna o ano em inteiro'''
    return int(cientista["ano_de_nascimento"])

def famous_births(cientistas: dict[str, dict[str, str]]) -> list[str]:
    '''Recebe um dicionário com nomes e ano de nascimento e retorna uma lista
    com os nomes completos e ano de nascimento ordenados por ano'''

    ordenados = sorted(cientistas.values(), key=get_year)

    return [f"{s['nome']} é um grande cientista nascido em {s['ano_de_nascimento']}." for s in ordenados]


# >>> from persons_of_interest import famous_births
# >>> cientistas = {"cecilia": {"nome": "Cecila Payne", "ano_de_nascimento": "1900"},"lise": {"nome": "Lise Meitner", "ano_de_nascimento": "1878"},"grace": {"nome": "Grace Hopper", "ano_de_nascimento": "1906"},"ada": {"nome": "Ada Lovelace", "ano_de_nascimento": "1815"}}
# >>> for cientista in famous_births(cientistas): print(cientista)
# Ada Lovelace é um grande cientista nascido em 1815.
# Lise Meitner é um grande cientista nascido em 1878.
# Cecila Payne é um grande cientista nascido em 1900.
# Grace Hopper é um grande cientista nascido em 1906.

