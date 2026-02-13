# 📋 Exemplos de Saída

Este diretório contém exemplos de saídas geradas pelas calculadoras financeiras em formato JSON.

## Arquivos de Exemplo

### `credit_summary.json`
Resumo completo do cálculo de crédito consignado, incluindo:
- Detalhes do contrato (valor, prazo, taxas)
- Informações de pagamento (CET, parcela mensal, total de juros)
- Cronograma completo das 36 parcelas

**Gerado por:** `calculators/credit-calculator.py`

---

### `investment_summary.json`
Resumo completo do cálculo de investimento CDB, incluindo:
- Detalhes do produto (tipo, prazo, taxas)
- Performance projetada (rendimento bruto e líquido)
- Projeção mensal dos 18 meses
- Janelas de liquidez semestral
- Proteção FGC

**Gerado por:** `calculators/investment-calculator.py`

---

### `integrated_dashboard.json`
Visão consolidada integrando crédito e investimento:
- Perfil do cliente
- Resumo do crédito
- Resumo do investimento
- Métricas consolidadas (benefício líquido, impacto mensal)
- Análise de risco
- Metas de performance

**Gerado por:** `calculators/integrated-dashboard.py`

---

## Como Usar Estes Exemplos

### 1. Visualizar no Terminal
```bash
# Ver resumo do crédito
cat examples/credit_summary.json | python3 -m json.tool | less

# Ver resumo do investimento
cat examples/investment_summary.json | python3 -m json.tool | less

# Ver dashboard integrado
cat examples/integrated_dashboard.json | python3 -m json.tool | less
```

### 2. Processar com Python
```python
import json

# Carregar resumo do crédito
with open('examples/credit_summary.json', 'r') as f:
    credit = json.load(f)
    
print(f"Parcela mensal: R$ {credit['contractDetails']['monthlyPayment']:.2f}")
print(f"Total de juros: R$ {credit['contractDetails']['totalInterest']:.2f}")
```

### 3. Importar em Outras Ferramentas
Estes arquivos JSON podem ser importados em:
- **Power BI / Tableau:** Para dashboards visuais
- **Excel:** Via Power Query
- **Google Sheets:** Via importação de JSON
- **APIs:** Como resposta de exemplo

---

## Regenerar os Exemplos

Para gerar novos exemplos com dados atualizados:

```bash
# Crédito
python3 calculators/credit-calculator.py
# Saída em: /tmp/credit_summary.json

# Investimento
python3 calculators/investment-calculator.py
# Saída em: /tmp/investment_summary.json

# Dashboard integrado
python3 calculators/integrated-dashboard.py
# Saída em: /tmp/integrated_dashboard_YYYYMMDD_HHMMSS.json
```

---

## Estrutura dos Dados

### Credit Summary
```json
{
  "contractDetails": {
    "principalAmount": 28000.00,
    "term": 36,
    "monthlyRate": 1.2503,
    "annualRate": 16.08,
    "cet": 16.08,
    "monthlyPayment": 970.68,
    "totalAmount": 34944.48,
    "totalInterest": 6944.48
  },
  "paymentDetails": {
    "firstDueDate": "2026-03-15",
    "lastDueDate": "2029-02-27",
    "paymentMethod": "consignado"
  },
  "schedule": [...]
}
```

### Investment Summary
```json
{
  "productDetails": {
    "productType": "CDB",
    "productName": "CDB Escalonado 18 Meses",
    "principalAmount": 85000.00,
    "term": 18,
    "annualRate": 12.00
  },
  "performance": {
    "projectedFinalBalance": 100750.21,
    "projectedGrossReturn": 15750.21,
    "projectedNetReturn": 12993.92
  },
  "liquidityWindows": [...],
  "monthlyProjection": [...]
}
```

### Integrated Dashboard
```json
{
  "clientProfile": {...},
  "credit": {...},
  "investment": {...},
  "consolidated": {
    "netFinancialBenefit": 6049.44,
    "netMonthlyImpact": 248.80
  },
  "risk": {...},
  "targets": {...}
}
```

---

**Última atualização:** 2026-02-13  
**Versão:** 1.0.0
