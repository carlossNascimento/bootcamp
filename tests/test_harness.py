
import pytest
from datetime import date

from src.task_analyzer import (
    criar_tarefa,
    dias_ate_entrega,
    calcular_media,
    calcular_horas_complementares,
    calcular_faltas,
    atualizar_status_tarefa,
    organizar_arquivos,
    salvar_dados,
    carregar_dados,
)


# Cenário 1: operações acadêmicas válidas

def test_criar_tarefa_valida():
    tarefa = criar_tarefa(
        "Prova de algoritmos",
        "Algoritmos",
        "2026-11-10",
    )

    assert tarefa["titulo"] == "Prova de algoritmos"
    assert tarefa["disciplina"] == "algoritmos"
    assert tarefa["status"] == "pendente"


def test_calcular_dias_ate_entrega():
    resultado = dias_ate_entrega(
        "2026-11-10",
        hoje=date(2026, 11, 1),
    )

    assert resultado == 9


def test_calcular_media_simples():
    assert calcular_media([8.0, 6.0, 10.0]) == pytest.approx(8.0)


def test_calcular_media_ponderada():
    resultado = calcular_media([8.0, 6.0], [2.0, 1.0])

    assert resultado == pytest.approx(22 / 3)


def test_calcular_horas_complementares():
    resultado = calcular_horas_complementares(40, 100)

    assert resultado["realizadas"] == 40
    assert resultado["restantes"] == 60
    assert resultado["concluidas"] is False


def test_calcular_faltas():
    resultado = calcular_faltas(5, 10)

    assert resultado["restantes"] == 5
    assert resultado["limite_excedido"] is False


def test_atualizar_status():
    tarefa = criar_tarefa(
        "Trabalho de programação",
        "Programação",
        "2026-11-20",
    )

    atualizada = atualizar_status_tarefa(tarefa, "concluída")

    assert atualizada["status"] == "concluída"
    assert tarefa["status"] == "pendente"


# Cenário 2: validação de erros e persistência

def test_rejeitar_disciplina_fora_do_escopo():
    with pytest.raises(ValueError):
        criar_tarefa(
            "Consulta",
            "Medicina",
            "2026-11-10",
        )


def test_rejeitar_nota_fora_do_intervalo():
    with pytest.raises(ValueError):
        calcular_media([11.0, 7.0])


def test_rejeitar_pesos_invalidos():
    with pytest.raises(ValueError):
        calcular_media([8.0, 7.0], [0.0, 0.0])


def test_rejeitar_horas_negativas():
    with pytest.raises(ValueError):
        calcular_horas_complementares(-1, 100)


def test_identificar_excesso_de_faltas():
    resultado = calcular_faltas(12, 10)

    assert resultado["restantes"] == 0
    assert resultado["limite_excedido"] is True


def test_organizar_arquivos(tmp_path):
    origem = tmp_path / "entrada"
    destino = tmp_path / "organizados"
    origem.mkdir()

    (origem / "aula.pdf").write_text("PDF de teste")
    (origem / "slides.pptx").write_text("Slides de teste")
    (origem / "notas.xyz").write_text("Arquivo de teste")

    resultado = organizar_arquivos(origem, destino)

    assert resultado["PDF"] == 1
    assert resultado["Apresentacoes"] == 1
    assert resultado["Outros"] == 1

    # O modo padrão copia os arquivos.
    assert (origem / "aula.pdf").exists()
    assert (destino / "PDF" / "aula.pdf").exists()


def test_salvar_e_carregar_dados(tmp_path):
    caminho = tmp_path / "dados.json"
    dados = {
        "tarefas": [
            {
                "titulo": "Prova",
                "disciplina": "algoritmos",
                "data_entrega": "2026-11-10",
                "status": "pendente",
            }
        ],
        "horas_complementares": 20.0,
        "faltas": {},
    }

    salvar_dados(dados, caminho)

    assert carregar_dados(caminho) == dados
