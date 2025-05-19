import pytest
import datetime
from pathlib import Path
from sqlalchemy import select
from sqlalchemy.orm import Session
from loader import (
    detectar_encoding,
    carregaArquivo,
    trabalha_csv,
    trabalha_json,
    remove_duplicatas_por_id,
    Accounts,
    Base,
    engine
)

@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


def test_detectar_encoding_utf8(tmp_path: Path):
    file_path = tmp_path / "arquivo.txt"
    file_path.write_text("algum conteúdo com acentuação", encoding="utf-8")
    assert detectar_encoding(file_path).lower().startswith("utf")


def test_carregaArquivo_ascii(tmp_path: Path):
    file_path = tmp_path / "test_ascii.txt"
    file_path.write_text("linha1\nlinha2", encoding="ascii")
    linhas = carregaArquivo(str(file_path))
    assert linhas == ["linha1\n", "linha2"]


def test_trabalha_csv():
    data = [
        "id,titular,saldo,limite,data_abertura",
        "001,Ana,1500.0,500.0,2024-05-01\n"
    ]
    contas = trabalha_csv(data)
    assert len(contas) == 1
    assert contas[0].id == "001"
    assert contas[0].titular == "Ana"
    assert contas[0].data_abertura == datetime.date(2024, 5, 1)


def test_trabalha_json():
    data = [
        '{"numero": "002", "titular": "Carlos", "saldo": 2000.0, "limite": 600.0, "data_abertura": "2023-12-01"}'
    ]
    contas = trabalha_json(data)
    assert len(contas) == 1
    assert contas[0].id == "002"
    assert contas[0].titular == "Carlos"
    assert contas[0].data_abertura == datetime.date(2023, 12, 1)


def test_remove_duplicatas_por_id():
    a1 = Accounts(id="001", titular="Ana", saldo=100, limite=50, data_abertura=datetime.date.today())
    a2 = Accounts(id="001", titular="Ana", saldo=100, limite=50, data_abertura=datetime.date.today())
    a3 = Accounts(id="002", titular="Beto", saldo=200, limite=100, data_abertura=datetime.date.today())
    lista = [a1, a2, a3]
    deduplicado = remove_duplicatas_por_id(lista)
    assert len(deduplicado) == 2


def test_insercao_no_banco(setup_database: None):
    conta = Accounts(id="003", titular="Duda", saldo=300, limite=150, data_abertura=datetime.date(2024, 1, 1))
    with Session(engine) as session:
        session.add(conta)
        session.commit()
        resultado = session.execute(select(Accounts).where(Accounts.id == "003")).scalar_one()
        assert resultado.titular == "Duda"
