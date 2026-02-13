#!/usr/bin/env python3
"""
Painel Financeiro Integrado 360° - Caso 6
Combina crédito consignado e investimento CDB em uma única visão
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

# Import the calculator classes directly by loading the modules
import importlib.util

def load_module_from_file(module_name, file_path):
    """Load a module from a file path"""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Load calculators
credit_calc_path = Path(__file__).parent / 'credit-calculator.py'
investment_calc_path = Path(__file__).parent / 'investment-calculator.py'

credit_module = load_module_from_file('credit_calculator', credit_calc_path)
investment_module = load_module_from_file('investment_calculator', investment_calc_path)

CreditCalculator = credit_module.CreditCalculator
InvestmentCalculator = investment_module.InvestmentCalculator


class IntegratedDashboard:
    """Painel integrado de Crédito + Investimento"""
    
    def __init__(self, client_data: dict):
        """
        Inicializa o painel com dados do cliente
        
        Args:
            client_data: Dicionário com dados do cliente e produtos
        """
        self.client_data = client_data
        
        # Inicializa calculadoras
        credit_params = client_data['creditProduct']
        self.credit_calculator = CreditCalculator(
            principal=credit_params['principalAmount'],
            term=credit_params['term'],
            annual_rate=credit_params['annualRate']
        )
        
        investment_params = client_data['investmentProduct']
        self.investment_calculator = InvestmentCalculator(
            principal=investment_params['principalAmount'],
            term=investment_params['term'],
            annual_rate=investment_params['annualRate']
        )
    
    def generate_integrated_view(self) -> dict:
        """
        Gera visão integrada do cliente
        
        Returns:
            Dicionário com todas as informações consolidadas
        """
        # Gera resumos individuais
        credit_summary = self.credit_calculator.generate_summary()
        investment_summary = self.investment_calculator.generate_summary()
        
        # Calcula métricas consolidadas
        monthly_payment = credit_summary['contractDetails']['monthlyPayment']
        monthly_return = investment_summary['performance']['projectedNetReturn'] / self.client_data['investmentProduct']['term']
        
        net_monthly_impact = monthly_payment - monthly_return
        
        # Análise de capacidade de pagamento
        available_margin = self.client_data['clientProfile']['availableMargin']
        margin_usage = (monthly_payment / available_margin) * 100
        
        return {
            'clientProfile': {
                'monthlyNetIncome': self.client_data['clientProfile']['monthlyNetIncome'],
                'consignableMargin': self.client_data['clientProfile']['consignableMarginPercentage'],
                'availableMargin': available_margin,
                'investorProfile': self.client_data['clientProfile']['investorProfile']
            },
            'credit': {
                'principalAmount': credit_summary['contractDetails']['principalAmount'],
                'monthlyPayment': monthly_payment,
                'totalInterest': credit_summary['contractDetails']['totalInterest'],
                'cet': credit_summary['contractDetails']['cet'],
                'remainingInstallments': credit_summary['contractDetails']['term'],
                'firstDueDate': credit_summary['paymentDetails']['firstDueDate'],
                'lastDueDate': credit_summary['paymentDetails']['lastDueDate']
            },
            'investment': {
                'principalAmount': investment_summary['productDetails']['principalAmount'],
                'projectedNetReturn': investment_summary['performance']['projectedNetReturn'],
                'averageMonthlyReturn': monthly_return,
                'annualRate': investment_summary['productDetails']['annualRate'],
                'maturityDate': investment_summary['dates']['maturityDate'],
                'liquidityWindows': len(investment_summary['liquidityWindows']),
                'fgcProtected': investment_summary['protection']['fgcProtected']
            },
            'consolidated': {
                'monthlyPayment': monthly_payment,
                'averageMonthlyReturn': monthly_return,
                'netMonthlyImpact': net_monthly_impact,
                'marginUsage': margin_usage,
                'totalCreditCost': credit_summary['contractDetails']['totalInterest'],
                'totalInvestmentReturn': investment_summary['performance']['projectedNetReturn'],
                'netFinancialBenefit': investment_summary['performance']['projectedNetReturn'] - credit_summary['contractDetails']['totalInterest']
            },
            'risk': {
                'probabilityOfDefault': self.client_data['riskParameters']['probabilityOfDefault'],
                'lossGivenDefault': self.client_data['riskParameters']['lossGivenDefault'],
                'expectedLoss': self.client_data['riskParameters']['expectedLoss']
            },
            'targets': {
                'conversionRate': self.client_data['kpis']['targets']['conversionRate'],
                'retention90Days': self.client_data['kpis']['targets']['retention90Days'],
                'nps': self.client_data['kpis']['targets']['nps']
            }
        }
    
    def display_dashboard(self):
        """Exibe o painel formatado no console"""
        view = self.generate_integrated_view()
        
        print("=" * 100)
        print("PAINEL FINANCEIRO INTEGRADO 360° - CASO 6".center(100))
        print("=" * 100)
        print()
        
        # Perfil do Cliente
        print("👤 PERFIL DO CLIENTE".center(100))
        print("-" * 100)
        print(f"Renda Líquida Mensal: R$ {view['clientProfile']['monthlyNetIncome']:,.2f}")
        print(f"Margem Consignável: {view['clientProfile']['consignableMargin']}% (R$ {view['clientProfile']['availableMargin']:,.2f}/mês)")
        print(f"Perfil de Investidor: {view['clientProfile']['investorProfile'].title()}")
        print()
        
        # Crédito Consignado
        print("💳 CRÉDITO CONSIGNADO".center(100))
        print("-" * 100)
        print(f"Valor do Crédito: R$ {view['credit']['principalAmount']:,.2f}")
        print(f"Parcela Mensal: R$ {view['credit']['monthlyPayment']:,.2f} (fixo)")
        print(f"Total de Juros: R$ {view['credit']['totalInterest']:,.2f}")
        print(f"CET: {view['credit']['cet']:.2f}% a.a.")
        print(f"Parcelas Restantes: {view['credit']['remainingInstallments']}")
        print(f"Período: {view['credit']['firstDueDate']} até {view['credit']['lastDueDate']}")
        print()
        
        # Investimento CDB
        print("📈 INVESTIMENTO CDB ESCALONADO".center(100))
        print("-" * 100)
        print(f"Valor Investido: R$ {view['investment']['principalAmount']:,.2f}")
        print(f"Rendimento Líquido Projetado: R$ {view['investment']['projectedNetReturn']:,.2f}")
        print(f"Rendimento Médio Mensal: R$ {view['investment']['averageMonthlyReturn']:,.2f}")
        print(f"Taxa Anual: {view['investment']['annualRate']:.2f}% a.a.")
        print(f"Vencimento: {view['investment']['maturityDate']}")
        print(f"Janelas de Liquidez: {view['investment']['liquidityWindows']} (semestrais)")
        print(f"Proteção FGC: {'✓ Sim' if view['investment']['fgcProtected'] else '✗ Não'}")
        print()
        
        # Visão Consolidada
        print("📊 VISÃO CONSOLIDADA".center(100))
        print("-" * 100)
        print(f"Pagamento Mensal (Crédito): R$ {view['consolidated']['monthlyPayment']:,.2f}")
        print(f"Rendimento Médio Mensal (Investimento): R$ {view['consolidated']['averageMonthlyReturn']:,.2f}")
        print(f"Impacto Líquido Mensal: R$ {view['consolidated']['netMonthlyImpact']:,.2f}")
        print(f"Uso da Margem Consignável: {view['consolidated']['marginUsage']:.1f}%")
        print()
        print(f"Custo Total do Crédito: R$ {view['consolidated']['totalCreditCost']:,.2f}")
        print(f"Retorno Total do Investimento: R$ {view['consolidated']['totalInvestmentReturn']:,.2f}")
        
        benefit_color = "✓" if view['consolidated']['netFinancialBenefit'] > 0 else "✗"
        print(f"Benefício Financeiro Líquido: {benefit_color} R$ {view['consolidated']['netFinancialBenefit']:,.2f}")
        print()
        
        # Análise de Risco
        print("⚠️  ANÁLISE DE RISCO".center(100))
        print("-" * 100)
        print(f"Probabilidade de Inadimplência (PD): {view['risk']['probabilityOfDefault']:.2f}%")
        print(f"Perda Dado Default (LGD): {view['risk']['lossGivenDefault']:.2f}%")
        print(f"Perda Esperada: {view['risk']['expectedLoss']:.2f}%")
        print()
        
        # Metas e KPIs
        print("🎯 METAS E INDICADORES".center(100))
        print("-" * 100)
        print(f"Meta de Conversão: {view['targets']['conversionRate']}% sobre base elegível")
        print(f"Meta de Retenção (90 dias): {view['targets']['retention90Days']}%")
        print(f"Meta de NPS: {view['targets']['nps']}")
        print()
        
        # Mensagens de Transparência
        print("💬 MENSAGENS DE TRANSPARÊNCIA".center(100))
        print("-" * 100)
        print("✓ Você vê tudo antes de contratar — simples e sem surpresas.")
        print("✓ Seu dinheiro rende enquanto você organiza suas parcelas.")
        print("✓ Cancelou? Resgatou? Sem custo escondido, tudo em um clique.")
        print()
        
        print("=" * 100)
    
    def export_to_json(self, filename: str = None):
        """
        Exporta a visão integrada para JSON
        
        Args:
            filename: Nome do arquivo de saída
        """
        if filename is None:
            filename = f'/tmp/integrated_dashboard_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
        
        view = self.generate_integrated_view()
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(view, f, ensure_ascii=False, indent=2)
        
        return filename


def main():
    """Exemplo de uso do painel integrado"""
    
    # Carrega parâmetros do sistema
    config_path = Path(__file__).parent.parent / 'config' / 'parameters.json'
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    # Cria painel integrado
    dashboard = IntegratedDashboard(config)
    
    # Exibe painel no console
    dashboard.display_dashboard()
    
    # Exporta para JSON
    output_file = dashboard.export_to_json()
    print(f"✅ Dashboard completo exportado para: {output_file}")
    print()


if __name__ == '__main__':
    main()
