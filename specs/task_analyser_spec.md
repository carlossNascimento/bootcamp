
# Especificação — Organizador Acadêmico

## 1. Objetivo
Gerenciar tarefas, entregas, notas, faltas, horas complementares
e arquivos relacionados às disciplinas de Ciência da Computação.

## 2. Usuários
Estudantes de Ciência da Computação.

## 3. Entradas
- Título, disciplina, status e data de entrega de tarefas.
- Notas entre 0 e 10 e respectivos pesos, quando aplicável.
- Horas complementares realizadas e necessárias.
- Quantidade atual de faltas e limite informado.
- Arquivos PDF, apresentações, documentos, textos e imagens.

## 4. Saídas
- Dias restantes ou dias de atraso de uma entrega.
- Média simples ou ponderada.
- Saldo de horas complementares.
- Faltas restantes e indicação de limite excedido.
- Tarefas classificadas por status.
- Arquivos organizados por categoria.
- Dados acadêmicos salvos em JSON.

## 5. Regras de negócio
1. Somente disciplinas presentes no catálogo de Ciência da Computação
   são aceitas.
2. O título de uma tarefa não pode ser vazio.
3. As datas devem usar o formato ISO: AAAA-MM-DD.
4. Os status permitidos são: pendente, em andamento e concluída.
5. Notas devem estar entre 0 e 10.
6. Pesos devem ser não negativos e sua soma deve ser maior que zero.
7. Horas e faltas não podem ser negativas.
8. O limite de faltas é informado pelo estudante e não substitui
   as regras oficiais da instituição.
9. A organização de arquivos copia os arquivos por padrão.
10. Os dados são restritos ao contexto acadêmico.

## 6. Critérios de aceitação
- CA01: criar tarefa válida.
- CA02: rejeitar disciplina não cadastrada.
- CA03: calcular dias até a entrega.
- CA04: calcular médias simples e ponderadas.
- CA05: calcular saldo de horas complementares.
- CA06: contabilizar faltas e identificar excesso.
- CA07: atualizar o status de uma tarefa.
- CA08: organizar arquivos por tipo.
- CA09: salvar e carregar dados JSON.
- CA10: executar os testes automatizados com pytest.
