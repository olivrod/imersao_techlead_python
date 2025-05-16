import sys
import chardet # type: ignore
from pathlib import Path

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

def converte_arquivo(arquivo_origem: str, arquivo_destino: str) -> str:
    '''Le arquivo informado e trata erros'''
    try:
        arquivo = Path(arquivo_origem)
        encoding = detectar_encoding(arquivo)
        if (encoding != 'Desconhecido'):
            conteudo = arquivo.read_text(encoding=encoding)
            novo_arquivo = arquivo.with_name(arquivo_destino)
            novo_arquivo.write_text(conteudo, encoding='utf-8')
            if novo_arquivo.is_file():
                return f"Arquivo '{novo_arquivo.name}' criado com sucesso."
            else:
                return "Arquivo não foi criado."
        else:
            return "Enconding desconhecido do arquivo origem."
    except FileNotFoundError:
        return 'Arquivo não encontrado.'
    except PermissionError:
        return 'Permissão negada para ler o arquivo.'
    except IsADirectoryError:
        return 'O argumento enviado é um diretório.'
    except UnicodeDecodeError as e:
        return f'Erro inesperado: {type(e).__name__}'
    except Exception as e:
        return f'Erro inesperado: {type(e).__name__}'


if __name__ == "__main__":
    '''Converte arquvio informado'''
    print(converte_arquivo(sys.argv[1], sys.argv[2]))


# ?> cat iso-8859-1_encoded.txt
# Convers?o de Codifica??o
# ?> file iso-8859-1_encoded.txt
# encoded.txt: ISO-8859 text
# ?> python3 utf8.py 'iso-8859-1_encoded.txt' 'utf-8_encoded.txt'
# Arquivo 'utf-8_encoded.txt' criado com sucesso.
# ?> cat utf-8_encoded.txt
# Conversão de Codificação