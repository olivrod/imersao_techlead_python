import sys
from pathlib import Path

def le_arquivo(caminho: str) -> str | None:
    '''Le arquivo informado e trata erros'''
    try:
        arquivo = Path(caminho)
        return arquivo.read_text(encoding='utf-8')
    except FileNotFoundError:
        return 'Arquivo não encontrado.'
    except PermissionError:
        return 'Permissão negada para ler o arquivo.'
    except IsADirectoryError:
        return 'O argumento enviado é um diretório.'
    except UnicodeDecodeError as e:
        return f'Erro inesperado: {type(e).__name__}'

if __name__ == "__main__":
    '''Le arquvio informado e printa seu conteudo'''
    print(le_arquivo(sys.argv[1]))


# ?> python3 read_file.py './unknown_file.txt'
# Erro: Arquivo não encontrado.
# ?> python3 read_file.py './secure_file.txt'
# Erro: Permissão negada para ler o arquivo.
# ?> python3 read_file.py '/bin/'
# Erro: O argumento enviado é um diretório.
# ?> python3 read_file.py './erro_nao_tratado.pdf'
# Erro inesperado: UnicodeDecodeError
# python3 read_file.py './arquivo.txt'