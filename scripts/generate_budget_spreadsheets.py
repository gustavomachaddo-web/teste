#!/usr/bin/env python3
"""
Script to generate organized budget spreadsheets in CSV format
Generates comprehensive budget reports from the financial calculators
"""

import json
import csv
import sys
from datetime import datetime
from pathlib import Path

# Add calculators to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'calculators'))

import importlib.util

def load_module_from_file(module_name, file_path):
    """Load a module from a file path"""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Load calculators
calc_dir = Path(__file__).parent.parent / 'calculators'
credit_module = load_module_from_file('credit_calculator', calc_dir / 'credit-calculator.py')
investment_module = load_module_from_file('investment_calculator', calc_dir / 'investment-calculator.py')

CreditCalculator = credit_module.CreditCalculator
InvestmentCalculator = investment_module.InvestmentCalculator


def generate_credit_schedule_csv(output_dir: Path):
    """Generate credit payment schedule CSV"""
    # Load parameters
    config_path = Path(__file__).parent.parent / 'config' / 'parameters.json'
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    credit_params = config['creditProduct']
    calculator = CreditCalculator(
        principal=credit_params['principalAmount'],
        term=credit_params['term'],
        annual_rate=credit_params['annualRate']
    )
    
    summary = calculator.generate_summary()
    schedule = summary['schedule']
    
    # Write to CSV
    output_file = output_dir / 'credito_cronograma_pagamentos.csv'
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Header
        writer.writerow(['CRONOGRAMA DE PAGAMENTOS - CRÉDITO CONSIGNADO'])
        writer.writerow([])
        writer.writerow(['Valor do Crédito:', f"R$ {credit_params['principalAmount']:,.2f}"])
        writer.writerow(['Prazo:', f"{credit_params['term']} meses"])
        writer.writerow(['Taxa Anual:', f"{credit_params['annualRate']:.2f}%"])
        writer.writerow(['CET:', f"{summary['contractDetails']['cet']:.2f}% a.a."])
        writer.writerow(['Parcela Mensal:', f"R$ {summary['contractDetails']['monthlyPayment']:,.2f}"])
        writer.writerow([])
        
        # Schedule table
        writer.writerow(['Parcela', 'Vencimento', 'Principal (R$)', 'Juros (R$)', 'Total (R$)', 'Saldo Devedor (R$)', 'Status'])
        
        for installment in schedule:
            writer.writerow([
                installment['installmentNumber'],
                installment['dueDate'],
                f"{installment['principalAmount']:.2f}",
                f"{installment['interestAmount']:.2f}",
                f"{installment['totalAmount']:.2f}",
                f"{installment['remainingBalance']:.2f}",
                installment['status']
            ])
        
        # Totals
        writer.writerow([])
        writer.writerow(['TOTAIS', '', 
                        f"{credit_params['principalAmount']:.2f}",
                        f"{summary['contractDetails']['totalInterest']:.2f}",
                        f"{summary['contractDetails']['totalAmount']:.2f}",
                        '', ''])
    
    print(f"✓ Cronograma de crédito gerado: {output_file}")
    return output_file


def generate_investment_projection_csv(output_dir: Path):
    """Generate investment projection CSV"""
    # Load parameters
    config_path = Path(__file__).parent.parent / 'config' / 'parameters.json'
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    investment_params = config['investmentProduct']
    calculator = InvestmentCalculator(
        principal=investment_params['principalAmount'],
        term=investment_params['term'],
        annual_rate=investment_params['annualRate']
    )
    
    summary = calculator.generate_summary()
    projection = summary['monthlyProjection']
    
    # Write to CSV
    output_file = output_dir / 'investimento_projecao_mensal.csv'
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Header
        writer.writerow(['PROJEÇÃO MENSAL - INVESTIMENTO CDB'])
        writer.writerow([])
        writer.writerow(['Valor Investido:', f"R$ {investment_params['principalAmount']:,.2f}"])
        writer.writerow(['Prazo:', f"{investment_params['term']} meses"])
        writer.writerow(['Taxa Anual:', f"{investment_params['annualRate']:.2f}%"])
        writer.writerow(['Rendimento Líquido Total:', f"R$ {summary['performance']['projectedNetReturn']:,.2f}"])
        writer.writerow([])
        
        # Projection table
        writer.writerow(['Mês', 'Data', 'Saldo Bruto (R$)', 'Rendimento Bruto (R$)', 'Taxa Retorno (%)', 'Alíquota IR (%)', 'Rendimento Líquido (R$)', 'Saldo Líquido (R$)'])
        
        for month in projection:
            writer.writerow([
                month['month'],
                month['date'],
                f"{month['balance']:.2f}",
                f"{month['grossReturn']:.2f}",
                f"{month['returnRate']:.2f}",
                f"{month['irRate']:.1f}",
                f"{month['netReturn']:.2f}",
                f"{month['netBalance']:.2f}"
            ])
    
    print(f"✓ Projeção de investimento gerada: {output_file}")
    return output_file


def generate_liquidity_windows_csv(output_dir: Path):
    """Generate liquidity windows CSV"""
    # Load parameters
    config_path = Path(__file__).parent.parent / 'config' / 'parameters.json'
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    investment_params = config['investmentProduct']
    calculator = InvestmentCalculator(
        principal=investment_params['principalAmount'],
        term=investment_params['term'],
        annual_rate=investment_params['annualRate']
    )
    
    summary = calculator.generate_summary()
    windows = summary['liquidityWindows']
    
    # Write to CSV
    output_file = output_dir / 'investimento_janelas_liquidez.csv'
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Header
        writer.writerow(['JANELAS DE LIQUIDEZ SEMESTRAL - CDB'])
        writer.writerow([])
        writer.writerow(['Janela', 'Data Disponível', 'Meses', 'Dias', 'Saldo Projetado (R$)', 'Rendimento Bruto (R$)', 'Alíquota IR (%)', 'IR (R$)', 'Rendimento Líquido (R$)', 'Saldo Líquido (R$)', 'Resgate Mínimo (R$)', 'Penalidade (%)'])
        
        for window in windows:
            writer.writerow([
                window['windowNumber'],
                window['availableDate'],
                window['months'],
                window['days'],
                f"{window['projectedBalance']:.2f}",
                f"{window['grossReturn']:.2f}",
                f"{window['irRate']:.1f}",
                f"{window['irAmount']:.2f}",
                f"{window['netReturn']:.2f}",
                f"{window['netBalance']:.2f}",
                f"{window['minRedemptionAmount']:.2f}",
                f"{window['penaltyRate']:.2f}"
            ])
    
    print(f"✓ Janelas de liquidez geradas: {output_file}")
    return output_file


def generate_consolidated_budget_csv(output_dir: Path):
    """Generate consolidated budget summary CSV"""
    # Load parameters
    config_path = Path(__file__).parent.parent / 'config' / 'parameters.json'
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    # Initialize calculators
    credit_params = config['creditProduct']
    credit_calc = CreditCalculator(
        principal=credit_params['principalAmount'],
        term=credit_params['term'],
        annual_rate=credit_params['annualRate']
    )
    
    investment_params = config['investmentProduct']
    investment_calc = InvestmentCalculator(
        principal=investment_params['principalAmount'],
        term=investment_params['term'],
        annual_rate=investment_params['annualRate']
    )
    
    credit_summary = credit_calc.generate_summary()
    investment_summary = investment_calc.generate_summary()
    
    # Calculate consolidated metrics
    monthly_payment = credit_summary['contractDetails']['monthlyPayment']
    monthly_return = investment_summary['performance']['projectedNetReturn'] / investment_params['term']
    net_benefit = investment_summary['performance']['projectedNetReturn'] - credit_summary['contractDetails']['totalInterest']
    
    # Write to CSV
    output_file = output_dir / 'orcamento_consolidado.csv'
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Header
        writer.writerow(['ORÇAMENTO FINANCEIRO CONSOLIDADO'])
        writer.writerow(['Data de Geração:', datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
        writer.writerow([])
        
        # Client profile
        writer.writerow(['PERFIL DO CLIENTE'])
        writer.writerow(['Renda Líquida Mensal:', f"R$ {config['clientProfile']['monthlyNetIncome']:,.2f}"])
        writer.writerow(['Margem Consignável:', f"{config['clientProfile']['consignableMarginPercentage']}%"])
        writer.writerow(['Margem Disponível:', f"R$ {config['clientProfile']['availableMargin']:,.2f}"])
        writer.writerow(['Perfil de Investidor:', config['clientProfile']['investorProfile']])
        writer.writerow([])
        
        # Credit details
        writer.writerow(['CRÉDITO CONSIGNADO'])
        writer.writerow(['Valor do Crédito:', f"R$ {credit_params['principalAmount']:,.2f}"])
        writer.writerow(['Prazo:', f"{credit_params['term']} meses"])
        writer.writerow(['Taxa Anual:', f"{credit_params['annualRate']:.2f}%"])
        writer.writerow(['Parcela Mensal:', f"R$ {monthly_payment:,.2f}"])
        writer.writerow(['Total de Juros:', f"R$ {credit_summary['contractDetails']['totalInterest']:,.2f}"])
        writer.writerow(['CET:', f"{credit_summary['contractDetails']['cet']:.2f}% a.a."])
        writer.writerow(['Uso da Margem:', f"{(monthly_payment / config['clientProfile']['availableMargin'] * 100):.1f}%"])
        writer.writerow([])
        
        # Investment details
        writer.writerow(['INVESTIMENTO CDB'])
        writer.writerow(['Valor Investido:', f"R$ {investment_params['principalAmount']:,.2f}"])
        writer.writerow(['Prazo:', f"{investment_params['term']} meses"])
        writer.writerow(['Taxa Anual:', f"{investment_params['annualRate']:.2f}%"])
        writer.writerow(['Rendimento Líquido Total:', f"R$ {investment_summary['performance']['projectedNetReturn']:,.2f}"])
        writer.writerow(['Rendimento Médio Mensal:', f"R$ {monthly_return:,.2f}"])
        writer.writerow(['Proteção FGC:', 'Sim - até R$ 250.000,00'])
        writer.writerow([])
        
        # Consolidated view
        writer.writerow(['VISÃO CONSOLIDADA'])
        writer.writerow(['Custo Total do Crédito:', f"R$ {credit_summary['contractDetails']['totalInterest']:,.2f}"])
        writer.writerow(['Retorno Total do Investimento:', f"R$ {investment_summary['performance']['projectedNetReturn']:,.2f}"])
        writer.writerow(['Benefício Financeiro Líquido:', f"R$ {net_benefit:,.2f}"])
        writer.writerow(['Impacto Mensal Líquido:', f"R$ {monthly_payment - monthly_return:,.2f}"])
        writer.writerow([])
        
        # Risk metrics
        writer.writerow(['MÉTRICAS DE RISCO'])
        writer.writerow(['Probabilidade de Inadimplência (PD):', f"{config['riskParameters']['probabilityOfDefault']:.2f}%"])
        writer.writerow(['Perda Dado Default (LGD):', f"{config['riskParameters']['lossGivenDefault']:.2f}%"])
        writer.writerow(['Perda Esperada:', f"{config['riskParameters']['expectedLoss']:.2f}%"])
        writer.writerow(['Spread Líquido:', f"{config['riskParameters']['spreadLiquido']:.2f} p.p."])
        writer.writerow([])
        
        # Performance targets
        writer.writerow(['METAS DE PERFORMANCE'])
        writer.writerow(['Taxa de Conversão:', f"{config['kpis']['targets']['conversionRate']}%"])
        writer.writerow(['Retenção 90 Dias:', f"{config['kpis']['targets']['retention90Days']}%"])
        writer.writerow(['NPS:', f"{config['kpis']['targets']['nps']}"])
    
    print(f"✓ Orçamento consolidado gerado: {output_file}")
    return output_file


def main():
    """Main function to generate all budget spreadsheets"""
    print("=" * 80)
    print("GERADOR DE PLANILHAS DE ORÇAMENTO")
    print("=" * 80)
    print()
    
    # Create output directory
    output_dir = Path(__file__).parent.parent / 'planilhas'
    output_dir.mkdir(exist_ok=True)
    
    print(f"Diretório de saída: {output_dir}")
    print()
    
    # Generate all spreadsheets
    print("Gerando planilhas...")
    print()
    
    generate_consolidated_budget_csv(output_dir)
    generate_credit_schedule_csv(output_dir)
    generate_investment_projection_csv(output_dir)
    generate_liquidity_windows_csv(output_dir)
    
    print()
    print("=" * 80)
    print("✅ Todas as planilhas foram geradas com sucesso!")
    print(f"Localização: {output_dir.absolute()}")
    print("=" * 80)


if __name__ == '__main__':
    main()
