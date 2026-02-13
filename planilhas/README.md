# 📊 Planilhas de Orçamento Financeiro

Este diretório contém as planilhas de orçamento organizadas em formato CSV para fácil importação em Excel, Google Sheets ou outras ferramentas de planilha.

## 📁 Arquivos Disponíveis

### 1. `orcamento_consolidado.csv`
**Resumo completo do orçamento financeiro integrado**

Contém:
- Perfil do cliente (renda, margem consignável, perfil de investidor)
- Detalhes do crédito consignado (valor, prazo, taxas, parcelas)
- Detalhes do investimento CDB (valor, rendimento, liquidez)
- Visão consolidada (benefício líquido, impacto mensal)
- Métricas de risco (PD, LGD, perda esperada)
- Metas de performance (KPIs)

**Uso recomendado:** Visão geral executiva do orçamento para apresentações e tomada de decisão.

---

### 2. `credito_cronograma_pagamentos.csv`
**Cronograma detalhado de pagamentos do crédito consignado**

Contém:
- Informações do contrato (valor, prazo, taxas)
- Cronograma completo das 36 parcelas
- Para cada parcela:
  - Número da parcela
  - Data de vencimento
  - Valor da amortização (principal)
  - Valor dos juros
  - Valor total da parcela
  - Saldo devedor remanescente
  - Status do pagamento

**Uso recomendado:** Controle mensal de pagamentos e acompanhamento do saldo devedor.

---

### 3. `investimento_projecao_mensal.csv`
**Projeção mês a mês do rendimento do investimento CDB**

Contém:
- Informações do investimento (valor, prazo, taxa)
- Projeção dos 18 meses:
  - Mês e data
  - Saldo bruto
  - Rendimento bruto acumulado
  - Taxa de retorno acumulada
  - Alíquota de IR aplicável
  - Rendimento líquido (após IR)
  - Saldo líquido

**Uso recomendado:** Acompanhamento da evolução do investimento e planejamento de resgates.

---

### 4. `investimento_janelas_liquidez.csv`
**Janelas de liquidez semestral do CDB**

Contém:
- Informações das 3 janelas de liquidez (6, 12 e 18 meses)
- Para cada janela:
  - Data disponível para resgate
  - Saldo projetado (bruto e líquido)
  - Rendimento (bruto e líquido)
  - Alíquota de IR
  - Valor mínimo para resgate
  - Penalidade (se houver)

**Uso recomendado:** Planejamento de resgates parciais conforme necessidade de liquidez.

---

## 🔄 Como Atualizar as Planilhas

As planilhas são geradas automaticamente a partir dos dados em `config/parameters.json`. Para gerar novas versões com dados atualizados:

```bash
# Na raiz do projeto
python3 scripts/generate_budget_spreadsheets.py
```

Isso regerará todas as 4 planilhas com os dados mais recentes.

---

## 📥 Como Usar

### No Excel ou LibreOffice Calc
1. Abra o Excel/Calc
2. Vá em Arquivo > Abrir
3. Selecione o arquivo CSV desejado
4. Configure a importação:
   - Delimitador: vírgula (,)
   - Codificação: UTF-8
   - Formato de número: conforme sua localidade

### No Google Sheets
1. Acesse Google Sheets
2. Arquivo > Importar
3. Faça upload do arquivo CSV
4. Configure:
   - Tipo de separador: Vírgula
   - Converter texto em números e datas: Sim

---

## 💡 Dicas de Uso

### Análise do Crédito
- Use o `credito_cronograma_pagamentos.csv` para:
  - Visualizar graficamente a evolução do saldo devedor
  - Calcular o total de juros já pagos
  - Planejar pagamentos antecipados
  - Identificar a progressão da amortização vs. juros

### Análise do Investimento
- Use o `investimento_projecao_mensal.csv` para:
  - Criar gráficos de evolução do patrimônio
  - Comparar cenários de resgate em diferentes momentos
  - Calcular o retorno efetivo considerando IR
  - Projetar o valor disponível em datas específicas

### Análise Consolidada
- Use o `orcamento_consolidado.csv` para:
  - Apresentar o caso completo para aprovação
  - Demonstrar o benefício líquido da solução integrada
  - Validar a capacidade de pagamento do cliente
  - Documentar os parâmetros de risco

---

## 📊 Visualizações Sugeridas

### Gráficos Recomendados

#### 1. Evolução do Saldo Devedor
- **Dados:** credito_cronograma_pagamentos.csv
- **Tipo:** Gráfico de linha
- **Eixo X:** Parcela ou Data
- **Eixo Y:** Saldo Devedor

#### 2. Composição da Parcela
- **Dados:** credito_cronograma_pagamentos.csv
- **Tipo:** Gráfico de área empilhada
- **Eixo X:** Parcela
- **Eixo Y:** Principal e Juros

#### 3. Evolução do Investimento
- **Dados:** investimento_projecao_mensal.csv
- **Tipo:** Gráfico de linha dupla
- **Eixo X:** Mês
- **Eixo Y:** Saldo Bruto e Saldo Líquido

#### 4. Impacto Financeiro Mensal
- **Dados:** Calcular manualmente ou usar dashboard integrado
- **Tipo:** Gráfico de barras
- **Valores:** Pagamento Mensal vs. Rendimento Mensal vs. Impacto Líquido

---

## 🔒 Segurança e Privacidade

⚠️ **IMPORTANTE:** Estas planilhas contêm informações financeiras sensíveis.

- **NÃO** compartilhe publicamente
- **NÃO** armazene em locais não seguros
- **NÃO** envie por email sem criptografia
- **SIM** mantenha backups seguros
- **SIM** use controle de acesso apropriado

---

## 📞 Suporte

Para dúvidas sobre:
- **Dados e cálculos:** Consulte a documentação em `/docs`
- **Geração de planilhas:** Veja `/scripts/generate_budget_spreadsheets.py`
- **Parâmetros:** Edite `/config/parameters.json`

---

**Última atualização:** 2026-02-13  
**Versão:** 1.0.0
