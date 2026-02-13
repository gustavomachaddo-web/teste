# 📊 Dashboard de KPIs e KRIs – Caso 6

## 🎯 Visão Geral

Monitoramento de indicadores de performance (KPIs) e risco (KRIs) para a solução integrada PF, com avaliação trimestral (90 dias).

---

## 📈 KPIs (Key Performance Indicators)

### KPI 1: Taxa de Adesão à Solução Integrada

**Definição**: Percentual de clientes elegíveis que contratam a solução completa (crédito + investimento).

```
Fórmula: (Contratos Integrados / Base Elegível) × 100
```

| Métrica | Meta | Atual | Status |
|---------|------|-------|--------|
| Conversão sobre base elegível | > 20% | - | 🔵 A medir |
| Conversão crédito isolado | < 30% | - | 🔵 A medir |
| Conversão investimento isolado | < 10% | - | 🔵 A medir |

**Ações se abaixo da meta:**
- Revisar comunicação da proposta de valor
- Aumentar incentivos para solução completa
- Analisar pontos de abandono no funil

---

### KPI 2: Spread Líquido Médio do Crédito

**Definição**: Margem financeira ajustada ao risco (PD/LGD) obtida nas operações de crédito.

```
Fórmula: Taxa Cobrada - (Custo de Funding + PD × LGD + Custos Operacionais)
Meta: 4,2 p.p./ano
```

| Métrica | Meta | Atual | Status |
|---------|------|-------|--------|
| Spread líquido médio | 4,2% a.a. | - | 🔵 A medir |
| Taxa média cobrada | ~15% a.a. | - | 🔵 A medir |
| Custo de funding | ~10% a.a. | - | 🔵 A medir |

**Componentes do Spread:**
- **PD × LGD**: 2,5% × 55% = 1,375%
- **Custos operacionais**: ~0,5%
- **Funding**: ~10%
- **Taxa ao cliente**: ~16%
- **Spread líquido**: ~4,2%

**Ações se abaixo da meta:**
- Revisar política de precificação
- Otimizar custos operacionais
- Melhorar seleção de clientes (reduzir PD)

---

### KPI 3: Retenção de Aplicações > 90 dias

**Definição**: Percentual de clientes que mantêm o investimento por mais de 90 dias.

```
Fórmula: (Investimentos Ativos >90d / Total de Investimentos) × 100
Meta: ≥ 98%
```

| Métrica | Meta | Atual | Status |
|---------|------|-------|--------|
| Retenção 90+ dias | ≥ 98% | - | 🔵 A medir |
| Retenção 180+ dias | ≥ 95% | - | 🔵 A medir |
| Valor médio mantido | R$ 85.000 | - | 🔵 A medir |

**Ações se abaixo da meta:**
- Investigar motivos de resgate antecipado
- Melhorar comunicação de rentabilidade
- Oferecer incentivos para manutenção

---

## ⚠️ KRIs (Key Risk Indicators)

### KRI 1: Reclamações sobre Cobrança/Rentabilidade

**Definição**: Volume de reclamações relacionadas a falta de clareza ou divergências em cobrança e rentabilidade.

```
Threshold Crítico: +20% vs. baseline
Meta: < 5 reclamações por 100 contratos
```

| Métrica | Threshold | Atual | Status |
|---------|-----------|-------|--------|
| Reclamações/100 contratos | < 5 | - | 🔵 A medir |
| Variação vs. baseline | +20% máx | - | 🔵 A medir |
| Taxa de resolução | > 90% | - | 🔵 A medir |

**Tipos de Reclamação Monitorados:**
- Não compreensão do CET
- Taxas não explicadas
- Rentabilidade diferente do prometido
- Dificuldade de resgate

**Ações se threshold ultrapassado:**
- 🟡 **Atenção (+10%)**: Revisar scripts de atendimento
- 🟠 **Alerta (+15%)**: Auditoria de processos
- 🔴 **Crítico (+20%)**: Suspensão temporária de novas vendas

---

### KRI 2: Inadimplência do Crédito > Meta

**Definição**: Taxa de inadimplência acima do PD esperado (2,5%).

```
PD Esperado: 2,5%
Threshold de Alerta: 3,0%
Threshold Crítico: 4,0%
```

| Métrica | Threshold | Atual | Status |
|---------|-----------|-------|--------|
| Inadimplência 30+ dias | < 2,5% | - | 🔵 A medir |
| Inadimplência 60+ dias | < 1,5% | - | 🔵 A medir |
| Inadimplência 90+ dias | < 0,8% | - | 🔵 A medir |

**Fatores de Risco Monitorados:**
- Mudança de emprego do cliente
- Redução de margem consignável
- Acúmulo de outras dívidas
- Comportamento de pagamento degradando

**Ações se threshold ultrapassado:**
- 🟡 **Atenção (2,5-3,0%)**: Reforçar políticas de crédito
- 🟠 **Alerta (3,0-4,0%)**: Revisar critérios de aprovação
- 🔴 **Crítico (>4,0%)**: Suspender novas aprovações e revisar carteira

---

### KRI 3: Cancelamentos ou Resgates antes de 6 meses

**Definição**: Volume de clientes que cancelam crédito ou resgatam investimento antes do prazo mínimo recomendado.

```
Meta: < 10% dos contratos
Threshold de Alerta: 15%
```

| Métrica | Threshold | Atual | Status |
|---------|-----------|-------|--------|
| Cancelamento crédito <6m | < 5% | - | 🔵 A medir |
| Resgate investimento <6m | < 10% | - | 🔵 A medir |
| Churn total | < 10% | - | 🔵 A medir |

**Motivos de Cancelamento Monitorados:**
- Insatisfação com taxas
- Falta de clareza contratual
- Atendimento inadequado
- Mudança de situação financeira
- Oferta concorrente

**Ações se threshold ultrapassado:**
- Entrevista de saída com 100% dos canceladores
- Análise de causas raiz
- Implementação de melhorias no processo
- Programa de retenção proativo

---

## 📊 Dashboard Consolidado

### Semáforo de Indicadores (90 dias)

| Indicador | Meta | Threshold | Status Atual | Tendência |
|-----------|------|-----------|--------------|-----------|
| **KPI 1** - Taxa de Adesão | >20% | <15% | 🔵 A medir | - |
| **KPI 2** - Spread Líquido | 4,2% | <3,5% | 🔵 A medir | - |
| **KPI 3** - Retenção 90d | ≥98% | <95% | 🔵 A medir | - |
| **KRI 1** - Reclamações | <5/100 | +20% | 🔵 A medir | - |
| **KRI 2** - Inadimplência | <2,5% | >3,0% | 🔵 A medir | - |
| **KRI 3** - Cancelamentos | <10% | >15% | 🔵 A medir | - |

**Legenda:**
- 🟢 Verde: Dentro da meta
- 🟡 Amarelo: Atenção necessária
- 🟠 Laranja: Ação corretiva urgente
- 🔴 Vermelho: Situação crítica
- 🔵 Azul: Ainda não medido

---

## 🎯 Metas Consolidadas (90 dias)

### Sucesso da Solução
```
✅ Retenção: ≥ 98%
✅ NPS: > 75
✅ Conversão: > 20%
```

### Indicadores Financeiros
```
✅ Spread líquido: 4,2% a.a.
✅ Inadimplência: < 2,5%
✅ Custo de aquisição: < R$ 500/cliente
```

### Experiência do Cliente
```
✅ NPS > 75
✅ Tempo médio de contratação: < 15 min
✅ Resolução primeiro contato: > 80%
```

---

## 📅 Calendário de Revisão

| Frequência | Atividade | Responsável |
|------------|-----------|-------------|
| **Semanal** | Monitoramento de KRIs críticos | Gestão de Riscos |
| **Quinzenal** | Review de performance comercial | Gerência Comercial |
| **Mensal** | Dashboard executivo completo | Diretoria |
| **Trimestral** | Revisão de metas e thresholds | Comitê Executivo |

---

## 🚨 Plano de Contingência

### Cenário 1: Inadimplência acima de 4%
- Suspensão imediata de novas aprovações
- Revisão completa de política de crédito
- Auditoria de processos de onboarding

### Cenário 2: NPS abaixo de 60
- Task force de experiência do cliente
- Revisão de todos os pontos de contato
- Programa intensivo de treinamento

### Cenário 3: Conversão abaixo de 10%
- Revisão de proposta de valor
- Teste A/B de jornada de contratação
- Análise competitiva de mercado

---

**Atualização**: Semanal  
**Owner**: Head de Produtos PF  
**Última revisão**: 2026-02-13
