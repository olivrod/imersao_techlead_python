def list_of_names(nomes: dict) -> None:
    '''retorna os nomes e sobrenomes com a primeira letra maiuscula'''
    nomes_capitalizados = []

    for nome, sobrenome in nomes.items():
        nome_completo = f"{nome.capitalize()} {sobrenome.capitalize()}"
        nomes_capitalizados.append(nome_completo)

    return nomes_capitalizados

# from your_namebook import list_of_names
# persons = {"jean": "valjean","grace": "hopper","xavier": "niel","fifi": "brindacier"}
# list_of_names(persons)