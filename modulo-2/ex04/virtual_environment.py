import os

def is_virtual_environment() -> bool:
    return 'VIRTUAL_ENV' in os.environ

if __name__ == "__main__":
    '''Valida se o ambiente virtual está ativo ou inativo
    Para criar o ambiente virtual executar o comando: 
        cd ~
        python3 -m venv virtual_env
    Para ativar o ambiente virtual executar o comando: 
        source ~/virtual_env/bin/activate
    Para desativar o ambiente virtual executar o comando: 
        deactivate'''

    if is_virtual_environment():
        print("Virtual environment active")
    else:
        print("Virtual environment inactive")
