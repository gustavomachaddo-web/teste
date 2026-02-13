# 🚀 Guia Rápido de Uso

Este guia mostra como começar a usar as planilhas e calculadoras de orçamento em 5 minutos.

## 📊 Uso Mais Simples: Abrir as Planilhas

### Passo 1: Localize as Planilhas
```bash
cd planilhas/
```

### Passo 2: Abra em Sua Ferramenta Favorita

#### Excel ou LibreOffice Calc
1. Clique duas vezes no arquivo `.csv`
2. Ou: Abrir com > Excel/Calc

#### Google Sheets
1. Acesse Google Sheets
2. Arquivo > Importar
3. Upload do arquivo CSV
4. Pronto!

### Passo 3: Explore os Dados

**Orçamento Consolidado** (`orcamento_consolidado.csv`)
- Visão geral de tudo
- Perfil do cliente
- Resumo de crédito e investimento
- Métricas de risco

**Cronograma de Crédito** (`credito_cronograma_pagamentos.csv`)
- 36 parcelas detalhadas
- Evolução do saldo devedor
- Separação entre principal e juros

**Projeção de Investimento** (`investimento_projecao_mensal.csv`)
- Evolução mês a mês
- Rendimento bruto e líquido
- Impacto do IR

**Janelas de Liquidez** (`investimento_janelas_liquidez.csv`)
- Datas de resgate disponíveis
- Valores projetados
- Regras de resgate

---

## 🧮 Executar as Calculadoras

### Pré-requisito
Python 3.8 ou superior instalado.

### Crédito Consignado
```bash
python3 calculators/credit-calculator.py
```

**Saída no terminal:**
- Resumo do crédito
- CET e taxas
- Primeiras e últimas parcelas
- Total de juros

**Arquivo gerado:** `/tmp/credit_summary.json`

---

### Investimento CDB
```bash
python3 calculators/investment-calculator.py
```

**Saída no terminal:**
- Resumo do investimento
- Rendimento bruto e líquido
- Janelas de liquidez
- Projeção mensal

**Arquivo gerado:** `/tmp/investment_summary.json`

---

### Painel Integrado 360°
```bash
python3 calculators/integrated-dashboard.py
```

**Saída no terminal:**
- Perfil do cliente
- Visão consolidada de crédito + investimento
- Benefício financeiro líquido
- Análise de risco
- Metas de performance

**Arquivo gerado:** `/tmp/integrated_dashboard_*.json`

---

## 🔄 Personalizar os Dados

### Passo 1: Edite os Parâmetros
```bash
# Abra o arquivo de configuração
vim config/parameters.json
# ou use seu editor preferido
```

### Passo 2: Modifique os Valores
Você pode alterar:
- Valor do crédito (`principalAmount`)
- Prazo em meses (`term`)
- Taxa de juros (`annualRate`)
- Perfil do cliente
- Metas de performance

### Passo 3: Regere as Planilhas
```bash
python3 scripts/generate_budget_spreadsheets.py
```

As planilhas em `planilhas/` serão atualizadas com os novos valores!

---

## 📈 Criar Gráficos

### No Excel/Google Sheets

#### Gráfico 1: Evolução do Saldo Devedor
1. Abra `credito_cronograma_pagamentos.csv`
2. Selecione as colunas "Parcela" e "Saldo Devedor"
3. Inserir > Gráfico > Linha
4. Pronto!

#### Gráfico 2: Evolução do Investimento
1. Abra `investimento_projecao_mensal.csv`
2. Selecione "Mês", "Saldo Bruto" e "Saldo Líquido"
3. Inserir > Gráfico > Linha com múltiplas séries
4. Veja a diferença entre bruto e líquido!

#### Gráfico 3: Composição da Parcela
1. Abra `credito_cronograma_pagamentos.csv`
2. Selecione "Parcela", "Principal" e "Juros"
3. Inserir > Gráfico > Colunas Empilhadas
4. Veja como a proporção muda!

---

## 🎯 Casos de Uso Comuns

### Caso 1: Apresentar Proposta para Cliente
1. Use `orcamento_consolidado.csv` para visão geral
2. Destaque o **benefício líquido** positivo
3. Mostre a **parcela fixa** e o **rendimento mensal**
4. Enfatize a **transparência total** (CET visível)

### Caso 2: Planejamento de Resgates
1. Abra `investimento_janelas_liquidez.csv`
2. Identifique as datas disponíveis (6, 12, 18 meses)
3. Veja o saldo líquido em cada janela
4. Planeje resgates conforme necessidade

### Caso 3: Análise de Sensibilidade
1. Copie `config/parameters.json` para backup
2. Altere um parâmetro (ex: taxa de juros)
3. Regere as planilhas
4. Compare os resultados
5. Repita para diferentes cenários

### Caso 4: Relatório Executivo
1. Execute `python3 calculators/integrated-dashboard.py`
2. A saída no terminal é perfeita para documentos
3. Ou use o JSON gerado para criar dashboard visual
4. Inclua gráficos das planilhas CSV

---

## 💡 Dicas Rápidas

### ✅ Faça
- Mantenha backup do `parameters.json` original
- Crie cenários diferentes em pastas separadas
- Use gráficos para visualizar melhor
- Compartilhe apenas o necessário

### ❌ Não Faça
- Não altere os arquivos CSV manualmente (regere com o script)
- Não compartilhe dados sensíveis publicamente
- Não modifique os calculadores sem entender o código
- Não esqueça de regenerar após alterar parâmetros

---

## 🆘 Ajuda Rápida

### Problema: "Python não encontrado"
**Solução:** Instale Python 3.8+ de python.org

### Problema: "Módulo não encontrado"
**Solução:** As bibliotecas usadas são padrão do Python. Verifique a instalação.

### Problema: "Erro ao abrir CSV"
**Solução:** Configure o delimitador como vírgula (,) e encoding UTF-8

### Problema: "Valores diferentes dos esperados"
**Solução:** Verifique se `config/parameters.json` tem os valores corretos

---

## 📚 Documentação Completa

Para informações detalhadas:
- **Planilhas:** Ver `planilhas/README.md`
- **Exemplos JSON:** Ver `examples/README.md`
- **Uso completo:** Ver `docs/USAGE.md`
- **Resumo executivo:** Ver `EXECUTIVE_SUMMARY.md`

---

## ⏱️ Resumo de 30 Segundos

```bash
# 1. Ver planilhas (método mais rápido)
cd planilhas/
open orcamento_consolidado.csv

# 2. Executar painel integrado
python3 calculators/integrated-dashboard.py

# 3. Personalizar e regenerar
vim config/parameters.json
python3 scripts/generate_budget_spreadsheets.py
```

**Pronto! Você já está usando o sistema de orçamento! 🎉**

---

**Tempo estimado para dominar:** 5-10 minutos  
**Tempo para análise completa:** 30-60 minutos  
**Última atualização:** 2026-02-13
