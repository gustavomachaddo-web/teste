# 📚 Guia de Uso - Caso 6: Solução Integrada PF

## Índice
1. [Visão Geral](#visão-geral)
2. [Instalação e Requisitos](#instalação-e-requisitos)
3. [Estrutura do Projeto](#estrutura-do-projeto)
4. [Uso das Calculadoras](#uso-das-calculadoras)
5. [Painel Integrado](#painel-integrado)
6. [Modelos de Dados](#modelos-de-dados)
7. [Exemplos Práticos](#exemplos-práticos)
8. [FAQs](#faqs)

---

## Visão Geral

Este projeto implementa uma solução integrada de crédito consignado e investimento CDB para clientes pessoa física (PF) com perfil moderado. A solução foi projetada para oferecer:

- ✅ **Transparência total**: CET visível, sem taxas ocultas
- ✅ **Previsibilidade**: Parcelas fixas e rendimentos projetados
- ✅ **Flexibilidade**: Liquidez semestral no investimento
- ✅ **Autonomia**: Gestão digital completa

---

## Instalação e Requisitos

### Pré-requisitos
```bash
Python 3.8 ou superior
```

### Dependências
Todas as dependências são da biblioteca padrão do Python:
- `json` - Manipulação de dados JSON
- `datetime` - Cálculos de datas
- `decimal` - Precisão financeira

### Instalação
```bash
# Clone o repositório
git clone https://github.com/gustavomachaddo-web/teste.git
cd teste

# Torne os scripts executáveis
chmod +x calculators/*.py
```

---

## Estrutura do Projeto

```
teste/
├── README.md                          # Documentação principal
├── .gitignore                         # Arquivos ignorados pelo Git
│
├── docs/                              # Documentação detalhada
│   ├── client-profile.md              # Perfil do cliente
│   ├── risk-matrix.md                 # Matriz de riscos
│   ├── kpi-dashboard.md               # KPIs e KRIs
│   └── USAGE.md                       # Este arquivo
│
├── models/                            # Modelos de dados (JSON Schema)
│   ├── client.json                    # Estrutura do perfil do cliente
│   ├── credit.json                    # Estrutura do crédito consignado
│   └── investment.json                # Estrutura do investimento CDB
│
├── calculators/                       # Calculadoras e ferramentas
│   ├── credit-calculator.py           # Calculadora de crédito
│   ├── investment-calculator.py       # Calculadora de investimento
│   └── integrated-dashboard.py        # Painel integrado 360°
│
└── config/                            # Configurações
    └── parameters.json                # Parâmetros do sistema
```

---

## Uso das Calculadoras

### 1. Calculadora de Crédito Consignado

Calcula parcelas, CET e gera cronograma de pagamentos.

#### Execução Básica
```bash
python3 calculators/credit-calculator.py
```

#### Uso Programático
```python
from decimal import Decimal

# Importar a classe (ajuste o caminho conforme necessário)
from credit_calculator import CreditCalculator

# Criar calculadora
calculator = CreditCalculator(
    principal=28000.00,    # R$ 28.000
    term=36,               # 36 meses
    annual_rate=16.08      # 16,08% a.a.
)

# Calcular parcela mensal
monthly_payment = calculator.calculate_monthly_payment()
print(f"Parcela mensal: R$ {monthly_payment}")

# Calcular CET
cet = calculator.calculate_cet()
print(f"CET: {cet}% a.a.")

# Gerar cronograma completo
schedule = calculator.generate_schedule()

# Gerar resumo completo
summary = calculator.generate_summary()
```

#### Saída Esperada
```
================================================================================
CALCULADORA DE CRÉDITO CONSIGNADO - CASO 6
================================================================================

Valor solicitado: R$ 28,000.00
Prazo: 36 meses
Taxa anual: 16.08%

--------------------------------------------------------------------------------
RESUMO DO CRÉDITO
--------------------------------------------------------------------------------
Taxa mensal: 1.2503%
Parcela mensal: R$ 970.68
Total a pagar: R$ 34,944.48
Total de juros: R$ 6,944.48
CET: 16.08% a.a.
```

---

### 2. Calculadora de Investimento CDB

Calcula rendimentos, projeções e janelas de liquidez.

#### Execução Básica
```bash
python3 calculators/investment-calculator.py
```

#### Uso Programático
```python
from investment_calculator import InvestmentCalculator

# Criar calculadora
calculator = InvestmentCalculator(
    principal=85000.00,    # R$ 85.000
    term=18,               # 18 meses
    annual_rate=12.00      # 12% a.a.
)

# Calcular valor futuro
future_value = calculator.calculate_future_value(days=540)  # 18 meses
print(f"Valor futuro: R$ {future_value}")

# Gerar janelas de liquidez
windows = calculator.generate_liquidity_windows()

# Gerar projeção mensal
projection = calculator.generate_monthly_projection()

# Gerar resumo completo
summary = calculator.generate_summary()
```

#### Saída Esperada
```
================================================================================
CALCULADORA DE INVESTIMENTO CDB - CASO 6
================================================================================

Valor investido: R$ 85,000.00
Prazo: 18 meses
Taxa anual: 12.00%

--------------------------------------------------------------------------------
RESUMO DO INVESTIMENTO
--------------------------------------------------------------------------------
Saldo final projetado (bruto): R$ 100,750.21
Rendimento bruto: R$ 15,750.21
Taxa de retorno: 18.53%
Imposto de Renda (17.5%): R$ 2,756.29
Rendimento líquido: R$ 12,993.92
Saldo final líquido: R$ 97,993.92
```

---

## Painel Integrado

O **Painel Financeiro Integrado 360°** combina crédito e investimento em uma única visão.

### Execução
```bash
python3 calculators/integrated-dashboard.py
```

### Funcionalidades

#### 1. Visão Consolidada
- Impacto líquido mensal (pagamento - rendimento)
- Uso da margem consignável
- Benefício financeiro líquido

#### 2. Análise de Risco
- Probabilidade de inadimplência (PD)
- Perda dado default (LGD)
- Perda esperada

#### 3. Metas e Indicadores
- Taxa de conversão esperada
- Retenção de clientes
- Net Promoter Score (NPS)

### Saída do Painel
```
====================================================================================================
                             PAINEL FINANCEIRO INTEGRADO 360° - CASO 6                              
====================================================================================================

👤 PERFIL DO CLIENTE
Renda Líquida Mensal: R$ 9,500.00
Margem Consignável: 22% (R$ 2,090.00/mês)

💳 CRÉDITO CONSIGNADO
Parcela Mensal: R$ 970.68 (fixo)
CET: 16.08% a.a.

📈 INVESTIMENTO CDB ESCALONADO
Rendimento Líquido Projetado: R$ 12,993.92
Taxa Anual: 12.00% a.a.

📊 VISÃO CONSOLIDADA
Impacto Líquido Mensal: R$ 248.80
Uso da Margem Consignável: 46.4%
Benefício Financeiro Líquido: ✓ R$ 6,049.44
```

---

## Modelos de Dados

### Client Model (`models/client.json`)
Define a estrutura do perfil do cliente:
```json
{
  "id": "uuid",
  "personalInfo": {
    "cpf": "string",
    "fullName": "string",
    "email": "string"
  },
  "financialProfile": {
    "monthlyNetIncome": "number",
    "consignableMargin": "number",
    "investmentCapacity": "number"
  },
  "riskProfile": {
    "investorProfile": "conservador|moderado|agressivo",
    "probabilityOfDefault": "number",
    "lossGivenDefault": "number"
  }
}
```

### Credit Model (`models/credit.json`)
Define a estrutura do contrato de crédito:
```json
{
  "contractId": "uuid",
  "clientId": "uuid",
  "contractDetails": {
    "principalAmount": "number",
    "term": "integer",
    "monthlyRate": "number",
    "cet": "number",
    "monthlyPayment": "number"
  },
  "schedule": [
    {
      "installmentNumber": "integer",
      "dueDate": "date",
      "principalAmount": "number",
      "interestAmount": "number",
      "remainingBalance": "number"
    }
  ]
}
```

### Investment Model (`models/investment.json`)
Define a estrutura do investimento:
```json
{
  "investmentId": "uuid",
  "clientId": "uuid",
  "productDetails": {
    "productType": "CDB|LCI|LCA",
    "principalAmount": "number",
    "term": "integer",
    "annualRate": "number"
  },
  "liquidityWindows": [
    {
      "windowNumber": "integer",
      "availableDate": "date",
      "minRedemptionAmount": "number"
    }
  ]
}
```

---

## Exemplos Práticos

### Exemplo 1: Simular Crédito com Parâmetros Personalizados

```python
#!/usr/bin/env python3
from credit_calculator import CreditCalculator

# Cliente quer R$ 50.000 em 48 meses
calculator = CreditCalculator(
    principal=50000.00,
    term=48,
    annual_rate=18.00
)

# Gerar resumo
summary = calculator.generate_summary()

print(f"Parcela: R$ {summary['contractDetails']['monthlyPayment']:,.2f}")
print(f"Total: R$ {summary['contractDetails']['totalAmount']:,.2f}")
print(f"CET: {summary['contractDetails']['cet']:.2f}%")
```

### Exemplo 2: Comparar Diferentes Cenários de Investimento

```python
#!/usr/bin/env python3
from investment_calculator import InvestmentCalculator

# Cenário 1: 12 meses
calc_12m = InvestmentCalculator(100000, 12, 12.0)
summary_12m = calc_12m.generate_summary()

# Cenário 2: 24 meses
calc_24m = InvestmentCalculator(100000, 24, 12.0)
summary_24m = calc_24m.generate_summary()

print("Comparação de Cenários:")
print(f"12 meses: R$ {summary_12m['performance']['projectedNetReturn']:,.2f}")
print(f"24 meses: R$ {summary_24m['performance']['projectedNetReturn']:,.2f}")
```

### Exemplo 3: Exportar Dados para Análise

```python
#!/usr/bin/env python3
import json
from integrated_dashboard import IntegratedDashboard

# Carregar configuração
with open('config/parameters.json') as f:
    config = json.load(f)

# Criar dashboard
dashboard = IntegratedDashboard(config)

# Exportar para JSON
output = dashboard.export_to_json('/tmp/analise_cliente.json')

print(f"Dados exportados para: {output}")
```

---

## FAQs

### Q1: Como alterar os parâmetros do cliente?
**R:** Edite o arquivo `config/parameters.json` com os novos valores.

### Q2: As calculadoras consideram dias úteis ou corridos?
**R:** Os cálculos de crédito usam meses (30 dias). Os cálculos de investimento aproximam dias úteis (21 dias úteis/mês).

### Q3: Como adicionar novas janelas de liquidez?
**R:** As janelas são geradas automaticamente a cada 6 meses. Para alterar, modifique `months_per_window` em `InvestmentCalculator.generate_liquidity_windows()`.

### Q4: O IR está sendo calculado corretamente?
**R:** Sim. Usamos a tabela regressiva:
- Até 180 dias: 22,5%
- 181-360 dias: 20%
- 361-720 dias: 17,5%
- Acima de 720 dias: 15%

### Q5: Como integrar com um banco de dados?
**R:** Os modelos JSON podem ser usados como schemas. Exemplo com SQLAlchemy:
```python
from sqlalchemy import Column, String, Float, Integer
from models import client

# Definir tabela baseada no modelo
class Client(Base):
    __tablename__ = 'clients'
    id = Column(String, primary_key=True)
    monthly_income = Column(Float)
    # ... outros campos
```

### Q6: Posso usar este código em produção?
**R:** Este é um protótipo educacional. Para produção:
- Adicione testes unitários
- Implemente validações robustas
- Integre com sistemas reais (core bancário, bureaus de crédito)
- Adicione auditoria e logs
- Implemente segurança (criptografia, autenticação)

### Q7: Como reportar bugs ou sugerir melhorias?
**R:** Abra uma issue no repositório do GitHub com detalhes do problema ou sugestão.

---

## Suporte e Contato

Para dúvidas, sugestões ou contribuições:
- 📧 Email: [suporte@exemplo.com]
- 🐛 Issues: https://github.com/gustavomachaddo-web/teste/issues
- 📖 Wiki: https://github.com/gustavomachaddo-web/teste/wiki

---

**Versão**: 1.0.0  
**Última atualização**: 2026-02-13  
**Autores**: Equipe de Produtos Financeiros
