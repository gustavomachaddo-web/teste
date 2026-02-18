# Guia Rápido - Consulta de Indicadores

## 🎯 Indicadores Configurados

O sistema possui **8 indicadores (KPIs)** configurados:

### Indicadores Normais (maior é melhor)
1. **Vendas Mensais** - Meta: R$ 100.000,00
2. **Satisfação do Cliente** - Meta: 90%
3. **Taxa de Conversão** - Meta: 15%
4. **Retenção de Clientes** - Meta: 85%
5. **NPS (Net Promoter Score)** - Meta: 70
6. **Ticket Médio** - Meta: R$ 500,00

### Indicadores Inversos (menor é melhor)
7. **Tempo de Resposta** - Meta: 24 horas (menor é melhor)
8. **Churn Rate** - Meta: 5% (menor é melhor)

## 📊 Como Consultar Indicadores

### Opção 1: Modo Interativo
```bash
python consultar_indicadores.py
```
Apresenta um menu com opções:
1. Ver todos os indicadores configurados
2. Ver exemplo de medições
3. Ver como adicionar medições
4. Ver tudo
0. Sair

### Opção 2: Modo Automático
```bash
python consultar_indicadores.py --auto
```
Exibe tudo automaticamente sem interação.

### Opção 3: Exportar para JSON
```bash
python exportar_indicadores.py
```
Gera arquivo `indicadores_e_medicoes.json` com:
- Todos os indicadores e suas configurações
- Medições de exemplo
- Resumo estatístico

## 📈 Níveis de Status

Os indicadores são classificados automaticamente em 4 níveis:

- **✓ EXCELENTE** - Atingimento ≥ 100%
- **○ BOM** - Atingimento entre 80% e 99%
- **⚠ ATENÇÃO** - Atingimento entre 60% e 79%
- **✗ CRÍTICO** - Atingimento < 60%

## 💡 Exemplo de Saída

```
VENDAS_MENSAIS
  Valor Medido: 95,000.00
  Meta: 100,000.00
  Atingimento: 95.0%
  Status: ○ BOM

TEMPO_RESPOSTA (INVERSO)
  Valor Medido: 20.00 horas
  Meta: 24.00 horas
  Atingimento: 120.0%
  Status: ✓ EXCELENTE
```

## 🔧 Como Adicionar Medições

```python
from agent import DataMeasurementAgent
import json

# Carregar configuração
with open('config.json', 'r') as f:
    config = json.load(f)

# Criar agente
agente = DataMeasurementAgent(config)

# Adicionar medições
dados = {
    'vendas_mensais': 95000,
    'satisfacao_cliente': 88,
    'taxa_conversao': 12,
    'tempo_resposta': 20,
    'retencao_clientes': 82,
    'nps': 75,
    'ticket_medio': 520,
    'churn_rate': 4.2
}

# Processar
agente.mensurar_dados(dados)

# Exibir relatório
agente.imprimir_relatorio()

# Exportar para JSON
agente.exportar_json('meu_relatorio.json')
```

## 📁 Estrutura do JSON Exportado

```json
{
  "timestamp": "2026-02-18T15:01:49",
  "indicadores": {
    "vendas_mensais": {
      "descricao": "Meta de vendas mensais em R$",
      "meta": 100000,
      "tipo": "normal",
      "tipo_descricao": "maior é melhor"
    },
    ...
  },
  "medicoes_exemplo": {
    "vendas_mensais": {
      "valor_medido": 95000,
      "meta": 100000,
      "percentual_atingido": 95.0,
      "status": "bom"
    },
    ...
  },
  "resumo": {
    "total_kpis": 8,
    "media_atingimento": 102.43,
    "kpis_excelente": 4,
    "kpis_bom": 4,
    "kpis_atencao": 0,
    "kpis_criticos": 0
  }
}
```

## 🚀 Comandos Úteis

| Comando | Descrição |
|---------|-----------|
| `python consultar_indicadores.py` | Menu interativo |
| `python consultar_indicadores.py --auto` | Exibir tudo |
| `python exportar_indicadores.py` | Exportar para JSON |
| `python agent.py` | Exemplo básico |
| `python exemplos.py` | Exemplos avançados |
| `python processar_coordenadores.py` | Análise em lote |

## 📞 Integração com Outros Sistemas

O arquivo JSON gerado pode ser facilmente integrado com:
- APIs REST
- Dashboards (PowerBI, Tableau, etc.)
- Sistemas de BI
- Planilhas Excel
- Bancos de dados

Basta ler o arquivo `indicadores_e_medicoes.json` e processar os dados conforme necessário.
