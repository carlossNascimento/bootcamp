
from __future__ import annotations

import argparse
import json
import shutil
from datetime import date
from pathlib import Path
from typing import Any


DISCIPLINAS_PERMITIDAS = {
    "algoritmos",
    "estrutura de dados",
    "programação",
    "programação orientada a objetos",
    "banco de dados",
    "engenharia de software",
    "sistemas operacionais",
    "redes de computadores",
    "matemática discreta",
    "cálculo",
    "arquitetura de computadores",
    "inteligência artificial",
    "teoria da computação",
    "compiladores",
    "segurança da informação",
    "desenvolvimento web",
}

STATUS_TAREFA = {"pendente", "em andamento", "concluída"}

TIPOS_ARQUIVO = {
    ".pdf": "PDF",
    ".ppt": "Apresentacoes",
    ".pptx": "Apresentacoes",
    ".doc": "Documentos",
    ".docx": "Documentos",
    ".txt": "Textos",
    ".md": "Textos",
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".png": "Imagens",
    ".webp": "Imagens",
}


def validar_disciplina(disciplina: str) -> str:
    """Aceita somente disciplinas presentes no catálogo acadêmico."""
    nome = disciplina.strip().lower()

    if nome not in DISCIPLINAS_PERMITIDAS:
        raise ValueError(
            f"Disciplina não permitida: {disciplina!r}. "
            "Informe uma disciplina cadastrada de Ciência da Computação."
        )

    return nome


def criar_tarefa(
    titulo: str,
    disciplina: str,
    data_entrega: str,
    status: str = "pendente",
) -> dict[str, Any]:
    """Cria uma tarefa acadêmica validada."""
    titulo = titulo.strip()
    disciplina_validada = validar_disciplina(disciplina)
    entrega = date.fromisoformat(data_entrega)
    status = status.strip().lower()

    if not titulo:
        raise ValueError("O título da tarefa não pode ficar vazio.")

    if status not in STATUS_TAREFA:
        raise ValueError(f"Status inválido: {status}.")

    return {
        "titulo": titulo,
        "disciplina": disciplina_validada,
        "data_entrega": entrega.isoformat(),
        "status": status,
    }


def dias_ate_entrega(data_entrega: str, hoje: date | None = None) -> int:
    """Retorna os dias restantes. Valores negativos indicam atraso."""
    entrega = date.fromisoformat(data_entrega)
    referencia = hoje or date.today()
    return (entrega - referencia).days


def calcular_media(
    notas: list[float],
    pesos: list[float] | None = None,
) -> float:
    """Calcula a média simples ou ponderada das notas."""
    if not notas:
        raise ValueError("Informe pelo menos uma nota.")

    if any(not 0 <= nota <= 10 for nota in notas):
        raise ValueError("As notas devem estar entre 0 e 10.")

    if pesos is None:
        return sum(notas) / len(notas)

    if len(notas) != len(pesos):
        raise ValueError("Cada nota precisa ter um peso correspondente.")

    if any(peso < 0 for peso in pesos):
        raise ValueError("Os pesos não podem ser negativos.")

    soma_pesos = sum(pesos)
    if soma_pesos <= 0:
        raise ValueError("A soma dos pesos deve ser maior que zero.")

    return sum(nota * peso for nota, peso in zip(notas, pesos)) / soma_pesos


def calcular_horas_complementares(
    horas_realizadas: float,
    horas_necessarias: float,
) -> dict[str, float | bool]:
    """Calcula o total realizado e o saldo de horas complementares."""
    if horas_realizadas < 0 or horas_necessarias < 0:
        raise ValueError("As horas não podem ser negativas.")

    restantes = max(0.0, horas_necessarias - horas_realizadas)

    return {
        "realizadas": float(horas_realizadas),
        "necessarias": float(horas_necessarias),
        "restantes": restantes,
        "concluidas": restantes == 0,
    }


def calcular_faltas(
    faltas: int,
    limite: int,
) -> dict[str, int | bool]:
    """Informa quantas faltas restam até o limite definido."""
    if isinstance(faltas, bool) or isinstance(limite, bool):
        raise ValueError("Faltas e limite devem ser números inteiros.")

    if not isinstance(faltas, int) or not isinstance(limite, int):
        raise ValueError("Faltas e limite devem ser números inteiros.")

    if faltas < 0 or limite < 0:
        raise ValueError("Faltas e limite não podem ser negativos.")

    return {
        "faltas": faltas,
        "limite": limite,
        "restantes": max(0, limite - faltas),
        "limite_excedido": faltas > limite,
    }


def atualizar_status_tarefa(
    tarefa: dict[str, Any],
    novo_status: str,
) -> dict[str, Any]:
    """Atualiza o progresso de uma tarefa."""
    status = novo_status.strip().lower()

    if status not in STATUS_TAREFA:
        raise ValueError(f"Status inválido: {novo_status}.")

    atualizada = tarefa.copy()
    atualizada["status"] = status
    return atualizada


def organizar_arquivos(
    pasta_origem: str | Path,
    pasta_destino: str | Path,
    mover: bool = False,
) -> dict[str, int]:
    """
    Organiza arquivos por extensão.

    Por segurança, copia os arquivos por padrão. Para mover, use mover=True.
    Arquivos de extensões desconhecidas vão para Outros.
    """
    origem = Path(pasta_origem).resolve()
    destino = Path(pasta_destino).resolve()

    if not origem.is_dir():
        raise ValueError("A pasta de origem não existe.")

    if origem == destino or origem in destino.parents:
        raise ValueError(
            "A pasta de destino não pode ser a origem nem ficar dentro dela."
        )

    if destino in origem.parents:
        raise ValueError(
            "A pasta de destino não pode conter a pasta de origem."
        )

    contagem: dict[str, int] = {}

    for arquivo in sorted(origem.iterdir()):
        if not arquivo.is_file():
            continue

        categoria = TIPOS_ARQUIVO.get(arquivo.suffix.lower(), "Outros")
        pasta_categoria = destino / categoria
        pasta_categoria.mkdir(parents=True, exist_ok=True)

        caminho_final = pasta_categoria / arquivo.name

        if caminho_final.exists():
            raise FileExistsError(
                f"O arquivo de destino já existe: {caminho_final}"
            )

        if mover:
            shutil.move(str(arquivo), str(caminho_final))
        else:
            shutil.copy2(arquivo, caminho_final)

        contagem[categoria] = contagem.get(categoria, 0) + 1

    return contagem


def salvar_dados(
    dados: dict[str, Any],
    caminho: str | Path = "dados_academicos.json",
) -> None:
    """Salva os dados acadêmicos em formato JSON."""
    arquivo = Path(caminho)
    arquivo.parent.mkdir(parents=True, exist_ok=True)

    with arquivo.open("w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)


def carregar_dados(
    caminho: str | Path = "dados_academicos.json",
) -> dict[str, Any]:
    """Carrega os dados salvos ou retorna uma estrutura inicial."""
    arquivo = Path(caminho)

    if not arquivo.exists():
        return {"tarefas": [], "horas_complementares": 0.0, "faltas": {}}

    with arquivo.open("r", encoding="utf-8") as f:
        dados = json.load(f)

    if not isinstance(dados, dict):
        raise ValueError("O arquivo de dados precisa conter um objeto JSON.")

    return dados


def main() -> None:
    """Disponibiliza operações básicas pela linha de comando."""
    parser = argparse.ArgumentParser(
        description="Organizador acadêmico de Ciência da Computação"
    )
    subparsers = parser.add_subparsers(dest="comando", required=True)

    tarefa_parser = subparsers.add_parser("tarefa", help="Consultar uma entrega")
    tarefa_parser.add_argument("--titulo", required=True)
    tarefa_parser.add_argument("--disciplina", required=True)
    tarefa_parser.add_argument("--entrega", required=True)
    tarefa_parser.add_argument(
        "--status", default="pendente", choices=sorted(STATUS_TAREFA)
    )

    media_parser = subparsers.add_parser("media", help="Calcular média")
    media_parser.add_argument("notas", nargs="+", type=float)

    args = parser.parse_args()

    try:
        if args.comando == "tarefa":
            tarefa = criar_tarefa(
                args.titulo,
                args.disciplina,
                args.entrega,
                args.status,
            )
            dias = dias_ate_entrega(tarefa["data_entrega"])
            print(json.dumps(tarefa, ensure_ascii=False, indent=2))
            print(f"Dias até a entrega: {dias}")

        elif args.comando == "media":
            print(f"Média: {calcular_media(args.notas):.2f}")

    except (ValueError, OSError) as erro:
        parser.exit(1, f"Erro: {erro}\n")


if __name__ == "__main__":
    main()
