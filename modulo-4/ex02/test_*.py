import pytest
import tempfile
import chardet # type: ignore
from pathlib import Path
from utf8 import converte_arquivo, detectar_encoding 

def test_arquivo_nao_encotrado():
    assert converte_arquivo("unknown_file.txt", "destino.txt") == "Arquivo não encontrado."

def test_diretorio():
    nome_arquivo = "/bin/"
    assert converte_arquivo(nome_arquivo, "destino.txt") == "O argumento enviado é um diretório."

# def test_erro_inesperado():
#     nome_arquivo = "./erro_nao_tratado.pdf"
#     assert converte_arquivo(nome_arquivo, "destino.txt").startswith("Erro inesperado:")

def test_detectar_encoding_iso():
    conteudo = "Conversão de Codificação"
    with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='iso-8859-1') as temp:
        temp.write(conteudo)
        caminho = Path(temp.name)

    encoding = detectar_encoding(caminho)
    assert encoding.lower().startswith("iso-8859-1")

def test_detectar_encoding_arquivo_vazio():
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        caminho = Path(temp.name)

    encoding = detectar_encoding(caminho)
    assert encoding == "Desconhecido"

