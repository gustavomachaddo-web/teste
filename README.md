# Sistema de Análise de Cards do Planner

Este projeto implementa um sistema para analisar e gerar relatórios sobre cards de planejamento.

## 📋 Descrição

O sistema permite:
- Gerenciar cards do planner com informações detalhadas (título, descrição, status, prioridade, responsável, datas, tags)
- Analisar distribuição de cards por status, prioridade, responsável e tags
- Identificar cards atrasados
- Calcular taxa de conclusão
- Gerar relatórios detalhados em formato texto

## 🏗️ Estrutura do Projeto

```
.
├── planner_cards.py      # Estrutura de dados e gerenciamento de cards
├── card_analyzer.py      # Análise e estatísticas dos cards
├── report_generator.py   # Geração de relatórios formatados
├── sample_data.py        # Dados de exemplo para teste
├── main.py              # Script principal
└── README.md            # Este arquivo
```

## 🚀 Como Usar

### Executar com dados de exemplo:

```bash
python main.py
```

Ou:

```bash
python3 main.py
```

Isto irá:
1. Carregar dados de exemplo (10 cards)
2. Analisar os cards
3. Exibir o relatório na tela
4. Salvar o relatório em `relatorio_planner.txt`

### Usar no seu próprio código:

```python
from planner_cards import PlannerCard, PlannerCardManager, CardStatus, CardPriority
from report_generator import ReportGenerator
from datetime import datetime

# Criar gerenciador de cards
manager = PlannerCardManager()

# Adicionar um card
card = PlannerCard(
    id=1,
    title="Minha tarefa",
    description="Descrição da tarefa",
    status=CardStatus.IN_PROGRESS,
    priority=CardPriority.HIGH,
    assignee="João Silva",
    due_date=datetime(2026, 3, 1),
    tags=["desenvolvimento", "backend"]
)
manager.add_card(card)

# Gerar relatório
report_gen = ReportGenerator(manager)
report_text = report_gen.generate_text_report()
print(report_text)

# Salvar relatório
report_gen.save_report("meu_relatorio.txt")
```

## 📊 Recursos do Sistema

### Status dos Cards
- **Não Iniciado**: Card ainda não começou
- **Em Progresso**: Card está sendo trabalhado
- **Concluído**: Card finalizado
- **Bloqueado**: Card impedido por algum motivo

### Prioridades
- **Baixa**: Pode esperar
- **Média**: Prioridade normal
- **Alta**: Importante
- **Urgente**: Requer atenção imediata

### Análises Disponíveis
- Distribuição por status
- Distribuição por prioridade
- Carga de trabalho por responsável
- Taxa de conclusão
- Cards atrasados
- Distribuição por tags

## 📈 Exemplo de Relatório

O relatório gerado inclui:
- Resumo geral (total de cards, taxa de conclusão, cards atrasados)
- Distribuição por status e prioridade
- Carga de trabalho por responsável
- Lista de cards atrasados com detalhes
- Detalhamento completo de todos os cards

## 🛠️ Requisitos

- Python 3.6 ou superior
- Nenhuma dependência externa (usa apenas biblioteca padrão do Python)

## 📝 Licença

Este projeto é de código aberto e está disponível para uso livre.
