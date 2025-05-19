from read_file import le_arquivo

def test_arquivo_nao_encotrado():
    nome_arquivo = "./unknown_file.txt"
    assert le_arquivo(nome_arquivo) == "Arquivo não encontrado."

def test_arquivo_permissao():
    nome_arquivo = "./secure_file.txt"
    assert le_arquivo(nome_arquivo) == "Permissão negada para ler o arquivo."

def test_diretorio():
    nome_arquivo = "/bin/"
    assert le_arquivo(nome_arquivo) == "O argumento enviado é um diretório."

def test_erro_inesperado():
    nome_arquivo = "./erro_nao_tratado.pdf"
    assert le_arquivo(nome_arquivo).startswith("Erro inesperado:")


