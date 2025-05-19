def format_cents(valor: int) -> str:
    '''formata valor com centavos'''
    try:
        #sinal = "-" if valor < 0 else "+"
        valor = abs(valor)
        reais = valor // 100
        centavos = valor % 100
        return(f"R$ {reais:,}".replace(",", ".") + f",{centavos:02d}".replace(".", ","))
    except Exception as e:
        return f'Erro inesperado: {type(e).__name__}'