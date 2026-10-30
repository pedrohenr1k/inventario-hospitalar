import pytest
import app


@pytest.fixture
def banco_temporario(tmp_path, monkeypatch):
    banco = tmp_path / "teste.db"
    monkeypatch.setattr(app, "DB_NAME", str(banco))
    app.init_db()
    return banco


def test_cadastrar_ativo(banco_temporario):
    mensagem, ativos, *_ = app.add_asset(
        "Computador Dell",
        2,
        "Bancada A de Estoque",
        "Normal",
    )

    assert mensagem == "Ativo cadastrado com sucesso!"
    assert len(ativos) == 1
    assert ativos[0][1] == "Computador Dell"
    assert ativos[0][2] == 2


def test_rejeitar_nome_vazio(banco_temporario):
    mensagem, *_ = app.add_asset(
        "",
        1,
        "Bancada A de Estoque",
        "Normal",
    )

    assert mensagem == "Erro: Informe o nome do ativo."


def test_rejeitar_quantidade_fracionada(banco_temporario):
    mensagem, *_ = app.add_asset(
        "Monitor",
        1.5,
        "Bancada A de Estoque",
        "Normal",
    )

    assert mensagem == "Erro: Informe uma quantidade inteira."


def test_rejeitar_quantidade_negativa(banco_temporario):
    mensagem, *_ = app.add_asset(
        "Monitor",
        -1,
        "Bancada A de Estoque",
        "Normal",
    )

    assert mensagem == "Erro: A quantidade não pode ser negativa."


def test_rejeitar_local_vazio(banco_temporario):
    mensagem, *_ = app.add_asset(
        "Monitor",
        1,
        "",
        "Normal",
    )

    assert mensagem == "Erro: Selecione um local."


def test_rejeitar_status_vazio(banco_temporario):
    mensagem, *_ = app.add_asset(
        "Monitor",
        1,
        "Bancada A de Estoque",
        "",
    )

    assert mensagem == "Erro: Selecione um status."


def test_consultar_estoque_vazio(banco_temporario):
    assert app.list_assets() == []