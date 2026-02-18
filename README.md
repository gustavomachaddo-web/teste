# Agente de Mensuração de Dados e KPIs

Este projeto implementa um agente inteligente que pode mensurar dados, calcular KPIs (Indicadores-Chave de Performance) e fornecer indicações de plano de ação baseadas nos resultados.

## Funcionalidades

- **Mensuração de Dados**: Coleta e processa dados de diferentes fontes
- **Cálculo de KPIs**: Calcula indicadores de performance baseados em metas definidas
- **Análise de Status**: Classifica KPIs em diferentes níveis (Excelente, Bom, Atenção, Crítico)
- **Geração de Plano de Ação**: Cria recomendações automáticas baseadas no desempenho dos KPIs
- **Relatórios**: Gera relatórios detalhados em formato console e JSON

## Instalação

### Requisitos

- Python 3.7 ou superior

### Instalação das Dependências

```bash
pip install -r requirements.txt
```

## Uso

### Exemplo Básico

```python
from agent import DataMeasurementAgent

# Criar configuração de KPIs
config = {
    'kpis': {
        'vendas_mensais': {
            'meta': 100000,
            'descricao': 'Meta de vendas mensais em R$',
            'inverso': False
        },
        'satisfacao_cliente': {
            'meta': 90,
            'descricao': 'Score de satisfação do cliente (%)',
            'inverso': False
        },
        'tempo_resposta': {
            'meta': 24,
            'descricao': 'Tempo médio de resposta em horas',
            'inverso': True  # Valores menores são melhores
        }
    }
}

# Inicializar agente
agente = DataMeasurementAgent(config)

# Mensurar dados
dados = {
    'vendas_mensais': 85000,
    'satisfacao_cliente': 92,
    'tempo_resposta': 18  # Menor que a meta = melhor
}

agente.mensurar_dados(dados)

# Gerar relatório
agente.imprimir_relatorio()

# Exportar para JSON
agente.exportar_json('relatorio.json')
```

### Executar Exemplo

```bash
python agent.py
```

## Estrutura do Projeto

```
.
├── agent.py           # Código principal do agente
├── config.json        # Configuração de KPIs (exemplo)
├── README.md          # Este arquivo
└── requirements.txt   # Dependências do projeto
```

## Classes Principais

### `DataMeasurementAgent`

Classe principal que gerencia a mensuração de dados e KPIs.

**Métodos principais:**

- `definir_kpi(nome, meta, descricao, inverso)`: Define um novo KPI. Use `inverso=True` para KPIs onde valores menores são melhores (ex: erros, tempo de resposta)
- `mensurar_kpi(nome, valor)`: Mensura um KPI específico
- `mensurar_dados(dados)`: Mensura múltiplos KPIs de uma vez
- `gerar_plano_acao()`: Gera plano de ação baseado nos resultados
- `gerar_relatorio()`: Gera relatório completo
- `imprimir_relatorio()`: Imprime relatório formatado
- `exportar_json(caminho)`: Exporta relatório para JSON
- `limpar_resultados()`: Limpa todas as medições e planos de ação

### `KPIResult`

Representa o resultado da mensuração de um KPI.

**Atributos:**
- `nome`: Nome do KPI
- `valor`: Valor medido
- `meta`: Meta definida
- `status`: Status (Excelente, Bom, Atenção, Crítico)
- `percentual_atingido`: Percentual da meta atingido
- `timestamp`: Data/hora da mensuração

### `ActionPlan`

Representa um plano de ação recomendado.

**Atributos:**
- `prioridade`: Prioridade (Alta, Média, Baixa)
- `kpi`: KPI relacionado
- `acao`: Descrição da ação recomendada
- `prazo`: Prazo sugerido
- `responsavel`: Responsável pela ação (opcional)

## Classificação de Status

O agente classifica automaticamente os KPIs baseado no percentual da meta atingido:

- **Excelente** (≥100%): Meta atingida ou superada
- **Bom** (80-99%): Próximo da meta, desempenho satisfatório
- **Atenção** (60-79%): Requer atenção e melhorias
- **Crítico** (<60%): Requer ação urgente

### KPIs Inversos

Alguns KPIs são melhores quando têm valores menores (ex: tempo de resposta, taxa de erros, churn rate). Para estes casos, use o parâmetro `inverso: True` na configuração:

```python
# Exemplo de KPI inverso
agente.definir_kpi('tempo_resposta', meta=24, descricao='Tempo médio em horas', inverso=True)

# Com um valor de 18 horas (menor que 24), o cálculo será:
# percentual_atingido = (24 / 18 * 100) = 133% → Status: EXCELENTE
```

KPIs comuns que devem usar `inverso=True`:
- Tempo de resposta
- Taxa de erros
- Taxa de cancelamento (churn rate)
- Custos operacionais
- Tempo de inatividade (downtime)

## Planos de Ação

O agente gera automaticamente planos de ação com:

- **Prioridade**: Alta, Média ou Baixa baseada no status
- **Descrição**: Ação específica recomendada
- **Prazo**: Sugestão de tempo para implementação

## Formato do Relatório

O relatório inclui:

1. **Resumo Geral**: Estatísticas agregadas de todos os KPIs
2. **Detalhamento dos KPIs**: Valores, metas e status de cada KPI
3. **Plano de Ação**: Recomendações priorizadas

## Personalização

### Adicionar Novos KPIs

```python
# KPI normal (valores maiores são melhores)
agente.definir_kpi('novo_kpi', meta=50, descricao='Descrição do KPI', inverso=False)

# KPI inverso (valores menores são melhores)
agente.definir_kpi('tempo_processamento', meta=10, descricao='Tempo em segundos', inverso=True)
```

### Configuração via JSON

Crie um arquivo `config.json`:

```json
{
  "kpis": {
    "nome_kpi": {
      "meta": 100,
      "descricao": "Descrição do KPI",
      "inverso": false
    },
    "tempo_resposta": {
      "meta": 24,
      "descricao": "Tempo de resposta em horas",
      "inverso": true
    }
  }
}
```

E carregue:

```python
import json

with open('config.json', 'r') as f:
    config = json.load(f)

agente = DataMeasurementAgent(config)
```

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está disponível sob a licença MIT.
