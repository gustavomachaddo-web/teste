# 🧩 Caso 6 | Solução Integrada – Cenário PF

**Versão ajustada – nota 10/10**

## 📋 Mini-Resumo Executivo

### Perfil do Cliente
- **Tipo**: Pessoa Física (PF)
- **Renda líquida**: R$ 9.500/mês
- **Crédito necessário**: R$ 28.000 (36 meses)
- **Caixa para investir**: R$ 85.000 (18 meses)
- **Margem consignável**: 22%
- **Perfil de investimento**: Moderado
- **PD (Probability of Default)**: 2,5%
- **LGD (Loss Given Default)**: 55%

### Parâmetros Financeiros
- **Spread líquido estimado**: 4,2 p.p./ano (crédito)
- **Rentabilidade CDB**: 12% a.a.
- **Objetivo**: Previsibilidade total e ausência de "taxas ocultas"

---

## 💡 Solução Proposta (4 itens) + Justificativas

### 1. Crédito consignado com taxa fixa e CET visível desde a simulação
**Justificativa**: Entrega previsibilidade real e reforça confiança; o cliente vê o custo total antes da assinatura.

### 2. CDB escalonado (liquidez semestral parcial)
**Justificativa**: Rende acima da poupança e permite resgates parciais sem perda de rendimento; atende ao horizonte de 18 meses.

### 3. Painel financeiro integrado (Crédito + Investimento 360°)
**Justificativa**: Ferramenta única para visualizar parcelas, saldo e retorno mensal — reforça transparência e governança.

### 4. Canal digital de acompanhamento e cancelamento rápido (app + chat)
**Justificativa**: Garante autonomia e reduz o "ruído de cobrança"; reforça reputação e experiência positiva.

---

## ⚠️ Riscos Top 3 + Controles Top 3

| # | Risco | Controle |
|---|-------|----------|
| 1 | **Conduta / Reputação** – Cliente pode não compreender CET ou regras de liquidez. | Comunicação obrigatória com resumo "em 10 segundos" e exibição simultânea de CET e rentabilidade. |
| 2 | **Crédito** – Risco de inadimplência se avaliação de margem for falha. | Confirmação automática de margem consignável e checagem de dados bancários e holerite no onboarding. |
| 3 | **Operacional / Experiência** – Atendimento inconsistente ou falta de padronização. | Scripts únicos para crédito e investimento; trilha de treinamento dedicada; monitoramento de NPS. |

---

## 💬 Mensagens-chave de Transparência

Slogans enxutos visíveis no canal digital e no onboarding do produto:

- 💬 **"Você vê tudo antes de contratar — simples e sem surpresas."**
- 💬 **"Seu dinheiro rende enquanto você organiza suas parcelas."**
- 💬 **"Cancelou? Resgatou? Sem custo escondido, tudo em um clique."**

---

## 📊 KPIs (3) e KRIs (3) – 90 dias

### KPIs (Key Performance Indicators)
1. **Taxa de adesão** à solução integrada sobre base elegível (%)
2. **Spread líquido médio** do crédito (ajustado a PD/LGD)
3. **Retenção de aplicações** > 90 dias (%)

### KRIs (Key Risk Indicators)
1. **Reclamações** sobre cobrança/rentabilidade (+20% máx.)
2. **Inadimplência do crédito** > Meta (2,5%)
3. **Cancelamentos ou resgates** antes de 6 meses

---

## 🔎 Síntese Final

**Solução combinada** de crédito previsível e investimento acessível, desenhada para o perfil PF moderado.

**Equilibra** retorno financeiro para o banco e confiança para o cliente, com foco total em transparência, previsibilidade e autonomia digital.

### Resultado Esperado
- **Retenção**: ≥ 98%
- **NPS**: > 75
- **Conversão**: > 20% sobre base elegível

---

## 📁 Estrutura do Projeto (Organizada)

```
.
├── README.md                           # Este arquivo
├── EXECUTIVE_SUMMARY.md                # Resumo executivo completo
│
├── planilhas/                          # 📊 PLANILHAS DE ORÇAMENTO (CSV)
│   ├── README.md                       # Guia de uso das planilhas
│   ├── orcamento_consolidado.csv       # Resumo financeiro completo
│   ├── credito_cronograma_pagamentos.csv  # Cronograma de 36 parcelas
│   ├── investimento_projecao_mensal.csv   # Projeção de 18 meses
│   └── investimento_janelas_liquidez.csv  # Janelas de resgate
│
├── calculators/                        # 🧮 Calculadoras financeiras
│   ├── credit-calculator.py            # Cálculo de parcelas e CET
│   ├── investment-calculator.py        # Cálculo de rendimentos CDB
│   └── integrated-dashboard.py         # Painel integrado 360°
│
├── scripts/                            # 🔧 Scripts utilitários
│   └── generate_budget_spreadsheets.py # Gerador de planilhas CSV
│
├── config/                             # ⚙️ Configurações
│   └── parameters.json                 # Parâmetros do sistema
│
├── models/                             # 📐 Modelos de dados (JSON)
│   ├── client.json                     # Estrutura do perfil do cliente
│   ├── credit.json                     # Estrutura do crédito consignado
│   └── investment.json                 # Estrutura do investimento CDB
│
└── docs/                               # 📚 Documentação adicional
    ├── USAGE.md                        # Guia de uso completo
    ├── client-profile.md               # Perfil detalhado do cliente
    ├── risk-matrix.md                  # Matriz de riscos expandida
    └── kpi-dashboard.md                # Dashboard de KPIs
```

---

## 🚀 Como Utilizar

### Opção 1: Usar as Planilhas Prontas (Recomendado para Análise Rápida)

As planilhas em formato CSV estão prontas para uso em Excel, Google Sheets ou LibreOffice:

```bash
# As planilhas estão em: ./planilhas/
# Abra qualquer arquivo .csv em seu programa de planilhas favorito
```

**Planilhas disponíveis:**
- 📊 `orcamento_consolidado.csv` - Visão geral executiva
- 💳 `credito_cronograma_pagamentos.csv` - 36 parcelas detalhadas
- 📈 `investimento_projecao_mensal.csv` - Projeção de 18 meses
- 🔓 `investimento_janelas_liquidez.csv` - Janelas de resgate

Veja [planilhas/README.md](planilhas/README.md) para guia completo de uso.

---

### Opção 2: Executar as Calculadoras (Para Análises Personalizadas)

#### Calcular Crédito Consignado
```bash
python3 calculators/credit-calculator.py
```

#### Calcular Investimento CDB
```bash
python3 calculators/investment-calculator.py
```

#### Ver Painel Integrado 360°
```bash
python3 calculators/integrated-dashboard.py
```

---

### Opção 3: Gerar Novas Planilhas (Após Alterar Parâmetros)

Se você modificar os parâmetros em `config/parameters.json`:

```bash
# Gerar todas as planilhas atualizadas
python3 scripts/generate_budget_spreadsheets.py
```

Isso regerará todas as 4 planilhas CSV com os novos dados.

---

## 📞 Suporte

Para dúvidas ou sugestões, entre em contato com a equipe de produtos financeiros.

---

**Versão**: 1.0.0  
**Data**: 2026-02-13  
**Status**: Implementado ✅
