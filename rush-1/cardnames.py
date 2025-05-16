def fit_tamanho(name: str ) -> bool:
    """  Verifica tamanho do nome
    """
    if len(name) <= 26:
        return True
    return False

def fit_preposicao(name: str ) -> str:
    """ Busca preposição no nome
    """
    name = name.replace(" de "," ")
    name = name.replace(" da "," ")
    name = name.replace(" dos "," ")
    name = name.replace(" e "," ")
    return name


def fit_maria(name: str ) -> str:
    """ Busca Maria no nome
    """
    if name.startswith("Maria "):
        return "M" + name[5:]
    return name

def fit_junior(name: str ) -> str:
    """ Busca Junior no nome
    """
    name_list = name.split()
    if (name_list[-1].upper() == "JUNIOR"):
        name_list[-1] = "Jr"
        return " ".join(name_list)
    else:
        return name
    
def fit_nomes_intermediarios(name: str) -> str:
    """ Abreviacao da parte intermediaria do nome
    """
    name_list = name.split()
    i = 0
    tam = len(name_list)
    meio = []
    for i in range(1,(tam-1)):
        meio.append(name_list[i])
    
    maior = str(max(meio,key=len))
    name_list[name_list.index(maior)] = maior[0]

    return(" ".join(name_list))


def fit(name: str) -> str:
    """ Retorna no nome a ser impresso no cartão
    """
    nome_formatado = name

    if(fit_tamanho(name)):
       return name

    nome_formatado = fit_preposicao(name)
   
    if fit_tamanho(nome_formatado):
        return nome_formatado

    nome_formatado = fit_maria(nome_formatado)
    if fit_tamanho(nome_formatado):
        return nome_formatado

    nome_formatado = fit_junior(nome_formatado)
    if fit_tamanho(nome_formatado):
        return nome_formatado 
    
    i = 0 
    while(not fit_tamanho(nome_formatado)):
        nome_formatado = fit_nomes_intermediarios(nome_formatado)  
        i += 1
        if i >=20:
            return nome_formatado



    return nome_formatado 
    



if __name__ == "__main__":
    print(fit("Antonia dos Santos Oliveira"))


