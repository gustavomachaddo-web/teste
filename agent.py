"""
Agente de Mensuração de Dados e KPIs com Indicação de Plano de Ação

Este agente analisa dados, calcula KPIs (Indicadores-Chave de Performance)
e fornece recomendações de plano de ação baseadas nos resultados.
"""

import json
import os
import tempfile
from typing import Dict, List, Any, Optional
from datetime import datetime
from dataclasses import dataclass, asdict
from enum import Enum


# Constantes
PERFECT_INVERSE_KPI_SCORE = 200.0  # Score para KPIs inversos com valor zero (desempenho perfeito)


class KPIStatus(Enum):
    """Status do KPI baseado no desempenho"""
    EXCELENTE = "excelente"
    BOM = "bom"
    ATENCAO = "atenção"
    CRITICO = "crítico"


@dataclass
class KPIResult:
    """Resultado da medição de um KPI"""
    nome: str
    valor: float
    meta: float
    status: KPIStatus
    percentual_atingido: float
    timestamp: str
    
    def to_dict(self):
        result = asdict(self)
        result['status'] = self.status.value
        return result


@dataclass
class ActionPlan:
    """Plano de ação recomendado"""
    prioridade: str
    kpi: str
    acao: str
    prazo: str
    responsavel: Optional[str] = None
    
    def to_dict(self):
        return asdict(self)


class DataMeasurementAgent:
    """
    Agente para mensurar dados, calcular KPIs e gerar planos de ação
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Inicializa o agente com configuração de KPIs
        
        Args:
            config: Dicionário com configuração de KPIs e metas
        """
        self.config = config or {}
        self.kpis_definidos = self.config.get('kpis', {})
        self.resultados_kpis: List[KPIResult] = []
        self.planos_acao: List[ActionPlan] = []
    
    def definir_kpi(self, nome: str, meta: float, descricao: str = "", inverso: bool = False):
        """
        Define um novo KPI
        
        Args:
            nome: Nome do KPI
            meta: Meta a ser atingida
            descricao: Descrição do KPI
            inverso: Se True, valores menores são melhores (ex: erros, tempo de resposta)
        """
        if meta <= 0:
            raise ValueError(f"Meta deve ser maior que zero. Recebido: {meta}")
        
        self.kpis_definidos[nome] = {
            'meta': meta,
            'descricao': descricao,
            'inverso': inverso
        }
    
    def mensurar_kpi(self, nome: str, valor: float) -> KPIResult:
        """
        Mensura um KPI específico
        
        Args:
            nome: Nome do KPI
            valor: Valor medido
            
        Returns:
            KPIResult com o resultado da mensuração
        """
        if nome not in self.kpis_definidos:
            raise ValueError(f"KPI '{nome}' não está definido")
        
        meta = self.kpis_definidos[nome]['meta']
        inverso = self.kpis_definidos[nome].get('inverso', False)
        
        # Para KPIs inversos, valores menores são melhores
        if inverso:
            # Quanto menor o valor em relação à meta, melhor o desempenho
            # Se valor é 0 (perfeito para KPIs como erros), consideramos desempenho excelente
            if valor == 0:
                percentual_atingido = PERFECT_INVERSE_KPI_SCORE
            else:
                percentual_atingido = (meta / valor * 100)
        else:
            # Quanto maior o valor em relação à meta, melhor o desempenho
            percentual_atingido = (valor / meta * 100)
        
        # Determina o status baseado no percentual atingido
        if percentual_atingido >= 100:
            status = KPIStatus.EXCELENTE
        elif percentual_atingido >= 80:
            status = KPIStatus.BOM
        elif percentual_atingido >= 60:
            status = KPIStatus.ATENCAO
        else:
            status = KPIStatus.CRITICO
        
        resultado = KPIResult(
            nome=nome,
            valor=valor,
            meta=meta,
            status=status,
            percentual_atingido=round(percentual_atingido, 2),
            timestamp=datetime.now().isoformat()
        )
        
        self.resultados_kpis.append(resultado)
        return resultado
    
    def mensurar_dados(self, dados: Dict[str, float]) -> List[KPIResult]:
        """
        Mensura múltiplos KPIs de uma vez
        
        Args:
            dados: Dicionário com nome do KPI e valor medido
            
        Returns:
            Lista de KPIResult
        """
        resultados = []
        for nome, valor in dados.items():
            resultado = self.mensurar_kpi(nome, valor)
            resultados.append(resultado)
        
        return resultados
    
    def gerar_plano_acao(self) -> List[ActionPlan]:
        """
        Gera plano de ação baseado nos KPIs mensurados
        
        Returns:
            Lista de ActionPlan com recomendações
        """
        self.planos_acao = []
        
        for resultado in self.resultados_kpis:
            if resultado.status == KPIStatus.CRITICO:
                self.planos_acao.append(ActionPlan(
                    prioridade="ALTA",
                    kpi=resultado.nome,
                    acao=f"Ação urgente necessária: {resultado.nome} está {resultado.percentual_atingido:.1f}% da meta. "
                         f"Revisar processos imediatamente e implementar ações corretivas.",
                    prazo="Imediato (24-48h)"
                ))
            
            elif resultado.status == KPIStatus.ATENCAO:
                self.planos_acao.append(ActionPlan(
                    prioridade="MÉDIA",
                    kpi=resultado.nome,
                    acao=f"Atenção necessária: {resultado.nome} está {resultado.percentual_atingido:.1f}% da meta. "
                         f"Analisar causas e desenvolver plano de melhoria.",
                    prazo="Curto prazo (1 semana)"
                ))
            
            elif resultado.status == KPIStatus.BOM:
                self.planos_acao.append(ActionPlan(
                    prioridade="BAIXA",
                    kpi=resultado.nome,
                    acao=f"Monitoramento: {resultado.nome} está {resultado.percentual_atingido:.1f}% da meta. "
                         f"Manter práticas atuais e buscar otimizações.",
                    prazo="Médio prazo (1 mês)"
                ))
        
        return self.planos_acao
    
    def gerar_relatorio(self) -> Dict[str, Any]:
        """
        Gera relatório completo com KPIs e plano de ação
        
        Returns:
            Dicionário com relatório completo
        """
        if not self.planos_acao:
            self.gerar_plano_acao()
        
        # Estatísticas gerais
        total_kpis = len(self.resultados_kpis)
        kpis_criticos = sum(1 for r in self.resultados_kpis if r.status == KPIStatus.CRITICO)
        kpis_atencao = sum(1 for r in self.resultados_kpis if r.status == KPIStatus.ATENCAO)
        kpis_bom = sum(1 for r in self.resultados_kpis if r.status == KPIStatus.BOM)
        kpis_excelente = sum(1 for r in self.resultados_kpis if r.status == KPIStatus.EXCELENTE)
        
        media_atingimento = sum(r.percentual_atingido for r in self.resultados_kpis) / total_kpis if total_kpis > 0 else 0
        
        relatorio = {
            'timestamp': datetime.now().isoformat(),
            'resumo': {
                'total_kpis': total_kpis,
                'media_atingimento': round(media_atingimento, 2),
                'kpis_excelente': kpis_excelente,
                'kpis_bom': kpis_bom,
                'kpis_atencao': kpis_atencao,
                'kpis_criticos': kpis_criticos
            },
            'kpis': [r.to_dict() for r in self.resultados_kpis],
            'plano_acao': [p.to_dict() for p in self.planos_acao]
        }
        
        return relatorio
    
    def imprimir_relatorio(self):
        """Imprime relatório formatado no console"""
        relatorio = self.gerar_relatorio()
        
        print("\n" + "="*80)
        print("RELATÓRIO DE MENSURAÇÃO DE DADOS E KPIs")
        print("="*80)
        print(f"\nData/Hora: {relatorio['timestamp']}")
        
        print("\n" + "-"*80)
        print("RESUMO GERAL")
        print("-"*80)
        resumo = relatorio['resumo']
        print(f"Total de KPIs Mensurados: {resumo['total_kpis']}")
        print(f"Média de Atingimento: {resumo['media_atingimento']:.2f}%")
        print(f"  - Excelente (≥100%): {resumo['kpis_excelente']}")
        print(f"  - Bom (80-99%): {resumo['kpis_bom']}")
        print(f"  - Atenção (60-79%): {resumo['kpis_atencao']}")
        print(f"  - Crítico (<60%): {resumo['kpis_criticos']}")
        
        print("\n" + "-"*80)
        print("DETALHAMENTO DOS KPIs")
        print("-"*80)
        for kpi in relatorio['kpis']:
            print(f"\n{kpi['nome']}:")
            print(f"  Valor: {kpi['valor']:.2f} | Meta: {kpi['meta']:.2f}")
            print(f"  Atingimento: {kpi['percentual_atingido']:.2f}%")
            print(f"  Status: {kpi['status'].upper()}")
        
        print("\n" + "-"*80)
        print("PLANO DE AÇÃO")
        print("-"*80)
        for i, acao in enumerate(relatorio['plano_acao'], 1):
            print(f"\n{i}. [{acao['prioridade']}] {acao['kpi']}")
            print(f"   Ação: {acao['acao']}")
            print(f"   Prazo: {acao['prazo']}")
        
        print("\n" + "="*80 + "\n")
    
    def exportar_json(self, caminho: str):
        """
        Exporta relatório para arquivo JSON
        
        Args:
            caminho: Caminho do arquivo de saída
        """
        relatorio = self.gerar_relatorio()
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(relatorio, f, indent=2, ensure_ascii=False)
        print(f"Relatório exportado para: {caminho}")
    
    def limpar_resultados(self):
        """Limpa todas as medições e planos de ação"""
        self.resultados_kpis = []
        self.planos_acao = []


def exemplo_uso():
    """Exemplo de uso do agente"""
    
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
            'taxa_conversao': {
                'meta': 15,
                'descricao': 'Taxa de conversão de leads (%)',
                'inverso': False
            },
            'tempo_resposta': {
                'meta': 24,
                'descricao': 'Tempo médio de resposta em horas',
                'inverso': True
            },
            'retencao_clientes': {
                'meta': 85,
                'descricao': 'Taxa de retenção de clientes (%)',
                'inverso': False
            }
        }
    }
    
    # Inicializar agente
    agente = DataMeasurementAgent(config)
    
    # Mensurar dados (valores reais do período)
    dados = {
        'vendas_mensais': 85000,
        'satisfacao_cliente': 92,
        'taxa_conversao': 9,
        'tempo_resposta': 20,
        'retencao_clientes': 65
    }
    
    # Processar medições
    agente.mensurar_dados(dados)
    
    # Gerar e imprimir relatório
    agente.imprimir_relatorio()
    
    # Exportar para JSON
    output_file = os.path.join(tempfile.gettempdir(), 'relatorio_kpis.json')
    agente.exportar_json(output_file)


if __name__ == '__main__':
    exemplo_uso()
