Organizador Acadêmico — Ciência da Computação

Sistema desenvolvido em Python para auxiliar estudantes de Ciência da Computação na organização de tarefas, avaliações, notas, faltas, horas complementares e materiais acadêmicos.

O projeto pode ser executado localmente com Python ou por meio de Docker e Docker Compose, facilitando a configuração do ambiente.

Requisitos
Execução local
Python 3.10 ou superior
pip
Execução com Docker
Docker Desktop ou Docker Engine
Docker Compose
Instalação e execução local
1. Clone o repositório
bash
git clone https://github.com/carlossNascimento/bootcamp.git
cd bootcamp

2. Crie um ambiente virtual

Windows (PowerShell):

powershell
python -m venv venv
.\venv\Scripts\Activate.ps1


Linux/macOS:

bash
python3 -m venv venv
source venv/bin/activate

3. Instale as dependências
bash
pip install -r requirements.txt

Executando com Docker

O projeto possui um Dockerfile que define o ambiente Python e um arquivo compose.yaml para simplificar a construção e a execução do container.

1. Construa a imagem

Na raiz do projeto, execute:

bash
docker build -t taskanalyzer .

2. Consulte a ajuda
bash
docker run --rm taskanalyzer

3. Calcule uma média
bash
docker run --rm taskanalyzer media 8 7 9


Resultado esperado:

text
Média: 8.00

4. Consulte uma tarefa
bash
docker run --rm taskanalyzer tarefa --titulo "Prova de Algoritmos" --disciplina "Algoritmos" --entrega 2026-11-10


O sistema exibirá os dados da tarefa e a quantidade de dias restantes até a entrega.

Executando com Docker Compose

O arquivo compose.yaml permite construir e executar o serviço sem precisar informar o nome da imagem em cada comando.

Construir a imagem
bash
docker compose build

Executar o programa
bash
docker compose run --rm taskanalyzer

Calcular uma média
bash
docker compose run --rm taskanalyzer media 8 7 9

Criar uma tarefa
bash
docker compose run --rm taskanalyzer tarefa --titulo "Prova de Algoritmos" --disciplina "Algoritmos" --entrega 2026-11-10

O projeto é uma aplicação de linha de comando e, portanto, não necessita de portas de rede. O comando run --rm remove o container ao terminar a execução.
Funcionalidades
Gestão de tarefas: criação de tarefas acadêmicas com título, disciplina, prazo e status.
Calendário de entregas: cálculo dos dias restantes ou de atraso.
Cálculo de notas: médias simples e ponderadas.
Horas complementares: acompanhamento das horas realizadas e restantes.
Contador de faltas: controle de faltas com base em um limite informado.
Progresso acadêmico: atualização do status das tarefas.
Organização de arquivos: separação de materiais por categoria, como PDFs, apresentações, documentos, textos e imagens.
Persistência de dados: funções para armazenamento e carregamento de informações em arquivos JSON.
Containerização: execução do projeto em um ambiente Python isolado com Docker.
Docker Compose: configuração simplificada para construir a imagem e executar o programa.
Testes automatizados

O projeto utiliza pytest para verificar o funcionamento das funcionalidades implementadas.

Para executar os testes localmente:

bash
python -m pytest -v


Se as dependências estiverem instaladas e os testes estiverem preparados para execução no container, também é possível executá-los usando a imagem:

bash
docker compose run --rm --entrypoint python taskanalyzer -m pytest -v

Para executar os testes no container, o pytest precisa estar listado no requirements.txt, e os arquivos de teste precisam ser copiados para a imagem pelo Dockerfile.
Estrutura do projeto
text
bootcamp/
├── README.md
├── Dockerfile
├── compose.yaml
├── .dockerignore
├── .gitignore
├── requirements.txt
├── CONTEXT_RULES.md
├── specs/
│   └── task_analyser_spec.md
├── src/
│   └── taskAnalyser.py
└── tests/
    └── test_harness.py


A estrutura acima representa a organização esperada. Os nomes dos arquivos devem corresponder aos existentes no repositório.

Regras de negócio
O sistema é destinado a estudantes de Ciência da Computação.
Somente disciplinas cadastradas no catálogo permitido são aceitas.
As notas devem estar entre 0 e 10.
As datas de entrega devem seguir o formato AAAA-MM-DD.
As tarefas podem ter os status pendente, em andamento ou concluída.
As horas e faltas não podem assumir valores negativos.
A organização de arquivos copia os arquivos por padrão, preservando os originais.
Arquivos com extensões desconhecidas são classificados na categoria Outros.
Escopo e limitações

Esta versão implementa funções centrais de cálculo, validação, controle de tarefas e organização de arquivos.

Ainda estão previstas melhorias como:

Interface interativa para cadastro e consulta.
Calendário acadêmico integrado.
Gerenciamento completo de múltiplas disciplinas.
Integração das tarefas, notas, faltas e horas complementares em um único fluxo de utilização.
Integração completa da persistência JSON com os comandos da aplicação.
Persistência dos dados entre containers por meio de volumes Docker, quando necessário.
Governança e qualidade

O desenvolvimento segue práticas de documentação, testes automatizados e revisão humana do código gerado com auxílio de inteligência artificial.

A homologação depende da execução dos testes e da validação das funcionalidades.

Tecnologias utilizadas
Python
pytest
JSON
Docker
Docker Compose
Git e GitHub
Status do projeto

Em desenvolvimento.
