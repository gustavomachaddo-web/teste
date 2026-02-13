# Matriz de Riscos – Caso 6: Solução Integrada PF

## 📋 Visão Geral

Esta matriz identifica, avalia e propõe controles para os principais riscos associados à solução integrada de crédito e investimento para clientes PF.

---

## 🔴 Riscos Críticos (Top 3)

### 1. Risco de Conduta / Reputação

**Categoria**: Compliance e Reputação  
**Probabilidade**: Média (30%)  
**Impacto**: Alto  
**Severidade**: 🔴 Crítico

#### Descrição
Cliente pode não compreender completamente o CET (Custo Efetivo Total) ou as regras de liquidez do investimento, levando a:
- Reclamações públicas
- Processos judiciais
- Danos à reputação da instituição
- Multas regulatórias

#### Controles Implementados

| # | Controle | Tipo | Efetividade |
|---|----------|------|-------------|
| 1.1 | Comunicação obrigatória com resumo "em 10 segundos" | Preventivo | Alta |
| 1.2 | Exibição simultânea de CET e rentabilidade na mesma tela | Preventivo | Alta |
| 1.3 | Quiz de compreensão antes da contratação | Preventivo | Média |
| 1.4 | Gravação de aceite com confirmação verbal/escrita | Detectivo | Alta |
| 1.5 | Canal de SAC dedicado para esclarecimentos | Corretivo | Média |

#### Indicadores de Monitoramento
- Reclamações sobre "não entendimento" < 5% dos contratos
- Taxa de desistência pós-simulação < 15%
- NPS do processo de contratação > 70

---

### 2. Risco de Crédito

**Categoria**: Risco Financeiro  
**Probabilidade**: Baixa (2,5% - PD)  
**Impacto**: Alto  
**Severidade**: 🟡 Alto

#### Descrição
Risco de inadimplência caso a avaliação de margem consignável seja falha ou o cliente tenha redução de renda:
- Perda financeira para a instituição
- Necessidade de provisionamento
- Impacto no spread líquido
- Acionamento de garantias

#### Controles Implementados

| # | Controle | Tipo | Efetividade |
|---|----------|------|-------------|
| 2.1 | Confirmação automática de margem consignável via convênio | Preventivo | Alta |
| 2.2 | Checagem de dados bancários e holerite no onboarding | Preventivo | Alta |
| 2.3 | Validação de CPF e consulta a bureaus de crédito | Preventivo | Alta |
| 2.4 | Análise de comportamento de crédito pregresso | Preventivo | Média |
| 2.5 | Desconto em folha automático (consignado) | Preventivo | Muito Alta |
| 2.6 | Sistema de early warning para mudanças de emprego | Detectivo | Média |

#### Indicadores de Monitoramento
- Inadimplência < 2,5% (dentro do PD esperado)
- Taxa de aprovação ajustada a risco > 85%
- Loss Given Default (LGD) < 55%

---

### 3. Risco Operacional / Experiência

**Categoria**: Operações e Processos  
**Probabilidade**: Média (40%)  
**Impacto**: Médio  
**Severidade**: 🟡 Alto

#### Descrição
Atendimento inconsistente ou falta de padronização pode levar a:
- Informações divergentes entre canais
- Frustração do cliente
- Aumento de reclamações
- Perda de eficiência operacional
- Redução do NPS

#### Controles Implementados

| # | Controle | Tipo | Efetividade |
|---|----------|------|-------------|
| 3.1 | Scripts únicos para crédito e investimento | Preventivo | Alta |
| 3.2 | Trilha de treinamento dedicada para equipe | Preventivo | Alta |
| 3.3 | Base de conhecimento unificada | Preventivo | Média |
| 3.4 | Monitoramento contínuo de NPS | Detectivo | Alta |
| 3.5 | Quality assurance em 10% das interações | Detectivo | Média |
| 3.6 | SLA de resposta em até 24h | Preventivo | Alta |

#### Indicadores de Monitoramento
- NPS > 75
- Taxa de resolução no primeiro contato > 80%
- Consistência de informações entre canais > 95%

---

## 🟠 Riscos Secundários

### 4. Risco de Liquidez (Investimento)

**Severidade**: 🟢 Médio

#### Descrição
Cliente pode precisar resgatar o investimento antes do prazo semestral.

#### Controles
- Comunicação clara sobre janelas de liquidez
- Opção de resgate parcial sem penalidades nas datas programadas
- Reserva de emergência sugerida separadamente

---

### 5. Risco de Mercado (Taxa de Juros)

**Severidade**: 🟢 Médio

#### Descrição
Variação nas taxas de juros pode afetar a atratividade do CDB.

#### Controles
- Taxa pós-fixada atrelada ao CDI
- Comunicação periódica de rentabilidade
- Opção de portabilidade para produtos mais competitivos

---

### 6. Risco Tecnológico

**Severidade**: 🟢 Médio

#### Descrição
Falhas no sistema digital podem impedir operações ou causar frustração.

#### Controles
- Arquitetura redundante
- Backup em tempo real
- Canal alternativo (telefone) sempre disponível
- SLA de uptime > 99,5%

---

## 📊 Matriz de Risco Consolidada

| Risco | Probabilidade | Impacto | Severidade | Controles |
|-------|---------------|---------|------------|-----------|
| 1. Conduta/Reputação | Média | Alto | 🔴 Crítico | 5 controles |
| 2. Crédito | Baixa | Alto | 🟡 Alto | 6 controles |
| 3. Operacional | Média | Médio | 🟡 Alto | 6 controles |
| 4. Liquidez | Baixa | Médio | 🟢 Médio | 3 controles |
| 5. Mercado | Baixa | Médio | 🟢 Médio | 3 controles |
| 6. Tecnológico | Baixa | Médio | 🟢 Médio | 4 controles |

---

## 🎯 Plano de Ação

### Curto Prazo (30 dias)
- [ ] Implementar quiz de compreensão
- [ ] Treinar equipe com scripts padronizados
- [ ] Configurar alertas de KRIs

### Médio Prazo (90 dias)
- [ ] Revisar efetividade dos controles
- [ ] Ajustar thresholds de KRIs
- [ ] Realizar auditoria de processos

### Longo Prazo (180 dias)
- [ ] Benchmark com mercado
- [ ] Implementar melhorias contínuas
- [ ] Certificação de qualidade

---

**Revisão**: Trimestral  
**Responsável**: Gestão de Riscos  
**Última atualização**: 2026-02-13
