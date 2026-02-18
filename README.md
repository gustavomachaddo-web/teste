# Agente de Mensuração de Dados e KPIs

Este projeto implementa um agente inteligente que pode mensurar dados, calcular KPIs (Indicadores-Chave de Performance) e fornecer indicações de plano de ação baseadas nos resultados.

## Funcionalidades

- **Mensuração de Dados**: Coleta e processa dados de diferentes fontes
- **Cálculo de KPIs**: Calcula indicadores de performance baseados em metas definidas
- **Análise de Status**: Classifica KPIs em diferentes níveis (Excelente, Bom, Atenção, Crítico)
- **Geração de Plano de Ação**: Cria recomendações automáticas baseadas no desempenho dos KPIs
- **Relatórios**: Gera relatórios detalhados em formato console e JSON
- **Processamento de Dados Tabulares**: Analisa dados de múltiplos coordenadores/equipes com relatórios consolidados
- **Suporte a KPIs Inversos**: Métricas onde valores menores são melhores
- **Consulta de Indicadores**: Visualização fácil de todos os indicadores configurados e medições
- **Exportação de Dados**: Exporta indicadores e medições para JSON

## Instalação

### Requisitos

- Python 3.7 ou superior

### Instalação das Dependências

```bash
pip install -r requirements.txt
```

## Uso

### Consultar Indicadores e Medições

Para visualizar os indicadores configurados e suas medições:

```bash
# Modo interativo (menu)
python consultar_indicadores.py

# Modo automático (exibe tudo)
python consultar_indicadores.py --auto
```

Este script permite:
- Ver todos os indicadores (KPIs) configurados
- Ver exemplos de medições com status
- Aprender como adicionar novas medições

### Exportar Indicadores para JSON

Para exportar todos os indicadores e medições para um arquivo JSON:

```bash
# Exporta para indicadores_e_medicoes.json
python exportar_indicadores.py

# Especificar arquivo de saída
python exportar_indicadores.py meu_arquivo.json
```

O arquivo JSON gerado contém:
- Lista completa de indicadores com metas e descrições
- Medições de exemplo com status
- Resumo estatístico

### Uso Rápido - Processar Dados de Coordenadores

Para analisar dados de performance de múltiplos coordenadores:

```bash
python processar_coordenadores.py
```

Este script irá:
- Processar dados tabulares de coordenadores
- Calcular KPIs individuais para cada um
- Gerar relatório consolidado com ranking
- Identificar coordenadores que requerem atenção
- Exportar relatório completo em JSON

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
├── agent.py                      # Código principal do agente
├── consultar_indicadores.py      # Script para consultar indicadores e medições
├── exportar_indicadores.py       # Script para exportar indicadores para JSON
├── processar_coordenadores.py    # Processador de dados tabulares
├── exemplos.py                   # Exemplos avançados de uso
├── config.json                   # Configuração de KPIs (exemplo)
├── README.md                     # Este arquivo
└── requirements.txt              # Dependências do projeto
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

## Processamento de Dados Tabulares

O módulo `processar_coordenadores.py` permite analisar dados de múltiplos coordenadores/equipes de uma só vez.

### Funcionalidades:

- **Análise em Massa**: Processa dados de dezenas de coordenadores simultaneamente
- **Relatório Consolidado**: Gera ranking e estatísticas gerais
- **Identificação de Problemas**: Detecta automaticamente quem precisa de atenção
- **Relatórios Individuais**: Detalha performance de cada coordenador
- **Exportação JSON**: Salva todos os dados para análise posterior

### Exemplo de Uso:

```python
from processar_coordenadores import processar_dados_coordenadores, gerar_relatorio_consolidado

# Dados em formato tabular (TSV/CSV)
dados_csv = """Coordenador\tAtendimento\t% Atendimento\t% Conversão\tTKM
JOAO SILVA\t100\t100,00%\t2,5%\t5500
MARIA SANTOS\t98\t98,00%\t1,8%\t4800"""

# Processar
relatorios = processar_dados_coordenadores(dados_csv)

# Gerar relatório consolidado
gerar_relatorio_consolidado(relatorios)
```

### Saída do Relatório:

O relatório consolidado inclui:

1. **Top Performers**: Os 10 coordenadores com melhor performance média
2. **Coordenadores que Requerem Atenção**: Lista priorizada de quem precisa de suporte
3. **Relatórios Individuais**: Análise detalhada com KPIs e planos de ação específicos
4. **Exportação JSON**: Dados completos para análises customizadas

### Métricas Suportadas:

- **% Atendimento**: Taxa de atendimento (meta: 100%)
- **% Consultas Motor**: Taxa de consultas ao sistema (meta: 67%)
- **% Conversão**: Taxa de conversão de contratos (meta: 2.09%)
- **TKM**: Tonelada por Quilômetro (meta: 5043)

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está disponível sob a licença MIT.
