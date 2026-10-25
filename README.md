Organizador Acadêmico — Ciência da Computação

Sistema desenvolvido em Python para auxiliar estudantes de Ciência da Computação na organização de tarefas, avaliações, notas, faltas, horas complementares e materiais acadêmicos.

Requisitos
Python 3.10 ou superior
pip
Instalação
1. Clone o repositório
git clone https://github.com/carlossNascimento/bootcamp
cd bootcamp


2. Crie um ambiente virtual

Windows:

python -m venv venv
venv\Scripts\activate


Linux/macOS:

python3 -m venv venv
source venv/bin/activate

3. Instale as dependências
pip install -r requirements.txt

Como executar
Calcular a média de uma disciplina
python -m src.task_analyzer media 8 7 9


Resultado esperado:

Média: 8.00

Consultar uma tarefa
python -m src.task_analyzer tarefa --titulo "Prova de Algoritmos" --disciplina "Algoritmos" --entrega 2026-11-10


O sistema exibirá os dados da tarefa e a quantidade de dias restantes até a entrega.

Funcionalidades
Gestão de tarefas: criação de tarefas acadêmicas com título, disciplina, prazo e status.
Calendário de entregas: cálculo dos dias restantes ou de atraso.
Cálculo de notas: médias simples e ponderadas.
Horas complementares: acompanhamento das horas realizadas e restantes.
Contador de faltas: controle de faltas com base em um limite informado.
Progresso acadêmico: atualização do status das tarefas.
Organização de arquivos: separação de materiais por categoria, como PDFs, apresentações, documentos e imagens.
Persistência de dados: armazenamento de informações em arquivos JSON.
Testes automatizados

O projeto utiliza pytest para verificar o funcionamento das funcionalidades implementadas.

Para executar os testes, utilize:

python -m pytest -v

Estrutura do projeto
organizador-academico/
├── README.md
├── CONTEXT_RULES.md
├── .gitignore
├── requirements.txt
├── specs/
│   └── task_analyzer_spec.md
├── tests/
│   └── test_harness.py
└── src/
    └── task_analyzer.py

Regras de negócio
O sistema é destinado a estudantes de Ciência da Computação.
Somente disciplinas cadastradas no catálogo permitido são aceitas.
As notas devem estar entre 0 e 10.
As datas de entrega devem seguir o formato AAAA-MM-DD.
As tarefas podem ter os status pendente, em andamento ou concluída.
As horas e faltas não podem assumir valores negativos.
A organização de arquivos copia os arquivos por padrão, preservando os originais.
Escopo e limitações

Esta versão implementa as funções centrais de cálculo, validação, controle de tarefas e organização de arquivos.

Ainda estão previstas melhorias como:

Interface interativa para cadastro e consulta.
Calendário acadêmico integrado.
Gerenciamento completo de múltiplas disciplinas.
Integração das tarefas, notas, faltas e horas complementares em um único fluxo de utilização.
Governança e qualidade

O desenvolvimento segue práticas de documentação, testes automatizados e revisão humana do código gerado com auxílio de inteligência artificial.

A homologação depende da execução dos testes e da validação das funcionalidades.

Tecnologias utilizadas
Python
pytest
JSON
Git e GitHub
Status do projeto

Em desenvolvimento.
