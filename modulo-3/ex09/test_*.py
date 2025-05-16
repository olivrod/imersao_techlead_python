from persons_of_interest import famous_births

def test_famous_births_ordered():
    cientistas = {
        "ada": {"nome": "Ada Lovelace", "ano_de_nascimento": "1815"},
        "cecilia": {"nome": "Cecila Payne", "ano_de_nascimento": "1900"},
        "lise": {"nome": "Lise Meitner", "ano_de_nascimento": "1878"},
        "grace": {"nome": "Grace Hopper", "ano_de_nascimento": "1906"}
    }

    expected = [
        "Ada Lovelace é um grande cientista nascido em 1815.",
        "Lise Meitner é um grande cientista nascido em 1878.",
        "Cecila Payne é um grande cientista nascido em 1900.",
        "Grace Hopper é um grande cientista nascido em 1906."
    ]

    assert famous_births(cientistas) == expected