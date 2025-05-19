import sys
import chardet # type: ignore
import datetime
import json
from pathlib import Path
from sqlalchemy import create_engine, Column, String, Float, Date
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()
# Cria engine e tabela
engine = create_engine("sqlite:///accounts.db", echo=True)

class Accounts(Base): # type: ignore
    __tablename__ = 'accounts'
    id = Column(String, primary_key=True)
    titular = Column(String, nullable=False)
    saldo = Column(Float, nullable=False)
    limite = Column(Float, nullable=False)
    data_abertura = Column(Date, nullable=False)
    

def detectar_encoding(caminho_arquivo: Path, num_bytes: int = 1000) -> str | None:
    '''Detecta e retorna o encoding de um arquivo'''
    try:
        arquivo = Path(caminho_arquivo)
        with open(arquivo, 'rb') as f:
            amostra = f.read(num_bytes)
            resultado = chardet.detect(amostra)
            return resultado['encoding'] or 'Desconhecido'
    except Exception as e:
        raise e

def carregaArquivo(filename: str)-> list: # type: ignore
    encoding = detectar_encoding(filename) # type: ignore
    if encoding == "ascii":
        encoding = "unicode_escape"
    lista_linhas = []
    with open(filename, encoding=encoding) as file:
        for line in file:
            lista_linhas.append(line)
    return lista_linhas

def trabalha_csv(dados: list)-> list: # type: ignore
    lista_csv = []
    for linha in dados[1:]:
        linha_splitada = linha.split(',')
        input = linha_splitada[4][:-1]
        date = datetime.date(int(input.split('-')[0]),int(input.split('-')[1]),int(input.split('-')[2]))
        lista_csv.append(Accounts(
            id=linha_splitada[0],
            titular=linha_splitada[1],
            saldo=linha_splitada[2],
            limite=linha_splitada[3],
            data_abertura=date
            ))
    return lista_csv

def trabalha_json(dados: list)-> list: # type: ignore
    lista_json = []
    for linha in dados:
        dado = json.loads(linha)
        input = dado["data_abertura"]
        date = datetime.date(int(input.split('-')[0]),int(input.split('-')[1]),int(input.split('-')[2]))
        lista_json.append(Accounts(
            id=dado["numero"],
            titular=dado["titular"],
            saldo=dado["saldo"],
            limite=dado["limite"],
            data_abertura=date
            ))
    return lista_json

def remove_duplicatas_por_id(accounts: list) -> list: # type: ignore
    return list({account.id: account for account in accounts}.values())

def main()->None:
    Base.metadata.create_all(engine)
    if len(sys.argv) > 1:
        lista_argumentos = sys.argv
        lista_argumentos.pop(0)
        for arg in lista_argumentos:
            arquivo = arg
            lista_linhas = carregaArquivo(arquivo)
            if (arquivo.split(".")[1].lower() == "csv"):
                dadoscsv = trabalha_csv(lista_linhas)
            elif (arquivo.split(".")[1].lower() == "jsonl"):
                dadosjson = trabalha_json(lista_linhas)

        dados = dadoscsv + dadosjson
        print(f"dados antes:{len(dados)}")
        dados = remove_duplicatas_por_id(dados)
        print(f"dados depois:{len(dados)}")

        with Session(engine) as session:
            session.add_all(dados)
            session.commit()
            print("fiz commit")


if __name__ == "__main__":
    main()