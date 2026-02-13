#!/usr/bin/env python3
"""
Calculadora de Investimento CDB - Caso 6
Calcula rendimentos, projeções e janelas de liquidez
"""

import json
from datetime import datetime, timedelta
from decimal import Decimal, ROUND_HALF_UP


class InvestmentCalculator:
    """Calculadora de CDB escalonado com liquidez semestral"""
    
    def __init__(self, principal: float, term: int, annual_rate: float):
        """
        Inicializa a calculadora
        
        Args:
            principal: Valor inicial investido em R$
            term: Prazo em meses
            annual_rate: Taxa de rentabilidade anual em %
        """
        self.principal = Decimal(str(principal))
        self.term = term
        self.annual_rate = Decimal(str(annual_rate))
        self.daily_rate = self._calculate_daily_rate()
        
    def _calculate_daily_rate(self) -> Decimal:
        """Calcula taxa diária a partir da taxa anual"""
        # Fórmula: (1 + i_anual)^(1/252) - 1 (252 dias úteis)
        annual_factor = (Decimal('1') + self.annual_rate / Decimal('100'))
        daily_factor = annual_factor ** (Decimal('1') / Decimal('252'))
        return (daily_factor - Decimal('1')) * Decimal('100')
    
    def calculate_future_value(self, days: int) -> Decimal:
        """
        Calcula valor futuro após determinado período
        
        Args:
            days: Número de dias corridos
        
        Returns:
            Valor futuro em R$
        """
        # Aproximação: 252 dias úteis por ano, 21 dias úteis por mês
        business_days = Decimal(str(days)) * Decimal('21') / Decimal('30')
        
        factor = (Decimal('1') + self.daily_rate / Decimal('100')) ** business_days
        future_value = self.principal * factor
        
        return future_value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    
    def calculate_ir_tax(self, days: int, gross_return: Decimal) -> dict:
        """
        Calcula imposto de renda regressivo
        
        Args:
            days: Número de dias de aplicação
            gross_return: Rendimento bruto em R$
        
        Returns:
            Dicionário com alíquota e valor do IR
        """
        # Tabela regressiva de IR
        if days <= 180:
            rate = Decimal('22.5')
        elif days <= 360:
            rate = Decimal('20.0')
        elif days <= 720:
            rate = Decimal('17.5')
        else:
            rate = Decimal('15.0')
        
        tax_amount = (gross_return * rate / Decimal('100')).quantize(
            Decimal('0.01'), rounding=ROUND_HALF_UP
        )
        
        return {
            'rate': float(rate),
            'amount': float(tax_amount),
            'netReturn': float(gross_return - tax_amount)
        }
    
    def generate_liquidity_windows(self, start_date: datetime = None) -> list:
        """
        Gera as janelas de liquidez semestral
        
        Args:
            start_date: Data de aplicação
        
        Returns:
            Lista de janelas de liquidez
        """
        if start_date is None:
            start_date = datetime.now()
        
        windows = []
        months_per_window = 6
        num_windows = (self.term + months_per_window - 1) // months_per_window
        
        for i in range(1, num_windows + 1):
            months = min(i * months_per_window, self.term)
            days = months * 30
            window_date = start_date + timedelta(days=days)
            
            # Calcula valor acumulado até essa janela
            future_value = self.calculate_future_value(days)
            gross_return = future_value - self.principal
            
            # Calcula IR
            tax_info = self.calculate_ir_tax(days, gross_return)
            
            windows.append({
                'windowNumber': i,
                'availableDate': window_date.strftime('%Y-%m-%d'),
                'months': months,
                'days': days,
                'projectedBalance': float(future_value),
                'grossReturn': float(gross_return),
                'irRate': tax_info['rate'],
                'irAmount': tax_info['amount'],
                'netReturn': tax_info['netReturn'],
                'netBalance': float(self.principal) + tax_info['netReturn'],
                'minRedemptionAmount': 5000.00 if i < num_windows else 0,
                'penaltyRate': 0
            })
        
        return windows
    
    def generate_monthly_projection(self, start_date: datetime = None) -> list:
        """
        Gera projeção mensal de rentabilidade
        
        Args:
            start_date: Data de aplicação
        
        Returns:
            Lista com projeção mês a mês
        """
        if start_date is None:
            start_date = datetime.now()
        
        projection = []
        
        for month in range(1, self.term + 1):
            days = month * 30
            projection_date = start_date + timedelta(days=days)
            
            # Calcula valor acumulado
            future_value = self.calculate_future_value(days)
            gross_return = future_value - self.principal
            
            # Calcula IR
            tax_info = self.calculate_ir_tax(days, gross_return)
            
            # Taxa de retorno acumulada
            return_rate = ((future_value / self.principal) - Decimal('1')) * Decimal('100')
            
            projection.append({
                'month': month,
                'date': projection_date.strftime('%Y-%m-%d'),
                'balance': float(future_value),
                'grossReturn': float(gross_return),
                'returnRate': float(return_rate),
                'irRate': tax_info['rate'],
                'netReturn': tax_info['netReturn'],
                'netBalance': float(self.principal) + tax_info['netReturn']
            })
        
        return projection
    
    def generate_summary(self, start_date: datetime = None) -> dict:
        """
        Gera resumo completo do investimento
        
        Returns:
            Dicionário com todos os detalhes calculados
        """
        if start_date is None:
            start_date = datetime.now()
        
        # Calcula valores finais
        total_days = self.term * 30
        final_value = self.calculate_future_value(total_days)
        gross_return = final_value - self.principal
        tax_info = self.calculate_ir_tax(total_days, gross_return)
        
        # Gera janelas de liquidez
        liquidity_windows = self.generate_liquidity_windows(start_date)
        
        # Gera projeção mensal
        monthly_projection = self.generate_monthly_projection(start_date)
        
        maturity_date = start_date + timedelta(days=total_days)
        
        return {
            'productDetails': {
                'productType': 'CDB',
                'productName': f'CDB Escalonado {self.term} Meses',
                'principalAmount': float(self.principal),
                'term': self.term,
                'annualRate': float(self.annual_rate),
                'dailyRate': float(self.daily_rate)
            },
            'performance': {
                'projectedFinalBalance': float(final_value),
                'projectedGrossReturn': float(gross_return),
                'projectedReturnRate': float(((final_value / self.principal) - Decimal('1')) * Decimal('100')),
                'estimatedIRTax': tax_info['amount'],
                'irRate': tax_info['rate'],
                'projectedNetReturn': tax_info['netReturn'],
                'projectedNetBalance': float(self.principal) + tax_info['netReturn']
            },
            'dates': {
                'applicationDate': start_date.strftime('%Y-%m-%d'),
                'maturityDate': maturity_date.strftime('%Y-%m-%d'),
                'daysToMaturity': total_days
            },
            'liquidityWindows': liquidity_windows,
            'monthlyProjection': monthly_projection,
            'protection': {
                'fgcProtected': True,
                'fgcLimit': 250000.00
            }
        }


def main():
    """Exemplo de uso da calculadora"""
    print("=" * 80)
    print("CALCULADORA DE INVESTIMENTO CDB - CASO 6")
    print("=" * 80)
    print()
    
    # Parâmetros do Caso 6
    principal = 85000.00  # R$ 85.000
    term = 18  # 18 meses
    annual_rate = 12.00  # 12% a.a.
    
    print(f"Valor investido: R$ {principal:,.2f}")
    print(f"Prazo: {term} meses")
    print(f"Taxa anual: {annual_rate:.2f}%")
    print()
    
    # Cria calculadora
    calculator = InvestmentCalculator(principal, term, annual_rate)
    
    # Gera resumo
    summary = calculator.generate_summary()
    
    print("-" * 80)
    print("RESUMO DO INVESTIMENTO")
    print("-" * 80)
    print(f"Saldo final projetado (bruto): R$ {summary['performance']['projectedFinalBalance']:,.2f}")
    print(f"Rendimento bruto: R$ {summary['performance']['projectedGrossReturn']:,.2f}")
    print(f"Taxa de retorno: {summary['performance']['projectedReturnRate']:.2f}%")
    print(f"Imposto de Renda ({summary['performance']['irRate']:.1f}%): R$ {summary['performance']['estimatedIRTax']:,.2f}")
    print(f"Rendimento líquido: R$ {summary['performance']['projectedNetReturn']:,.2f}")
    print(f"Saldo final líquido: R$ {summary['performance']['projectedNetBalance']:,.2f}")
    print()
    
    print("-" * 80)
    print("JANELAS DE LIQUIDEZ SEMESTRAL")
    print("-" * 80)
    print(f"{'Janela':<8} {'Data':<12} {'Meses':<7} {'Saldo Bruto':>14} {'Rend. Líquido':>14} {'Saldo Líquido':>14}")
    print("-" * 80)
    
    for window in summary['liquidityWindows']:
        print(
            f"{window['windowNumber']:<8} "
            f"{window['availableDate']:<12} "
            f"{window['months']:<7} "
            f"R$ {window['projectedBalance']:>11,.2f} "
            f"R$ {window['netReturn']:>11,.2f} "
            f"R$ {window['netBalance']:>11,.2f}"
        )
    
    print()
    
    print("-" * 80)
    print("PROJEÇÃO MENSAL (Primeiros 6 meses)")
    print("-" * 80)
    print(f"{'Mês':<5} {'Data':<12} {'Saldo':>14} {'Rendimento':>14} {'Taxa':>8}")
    print("-" * 80)
    
    for i, month in enumerate(summary['monthlyProjection'][:6]):
        print(
            f"{month['month']:<5} "
            f"{month['date']:<12} "
            f"R$ {month['balance']:>11,.2f} "
            f"R$ {month['grossReturn']:>11,.2f} "
            f"{month['returnRate']:>7.2f}%"
        )
    
    print()
    
    # Salva em arquivo JSON
    output_file = '/tmp/investment_summary.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Resumo completo salvo em: {output_file}")
    print()
    
    # Mensagens de transparência
    print("-" * 80)
    print("💬 MENSAGENS DE TRANSPARÊNCIA")
    print("-" * 80)
    print("✓ Seu dinheiro rende enquanto você organiza suas parcelas.")
    print("✓ Rentabilidade de {:.2f}% a.a. - Superior à poupança!".format(annual_rate))
    print("✓ Liquidez semestral sem perda de rendimento.")
    print("✓ Proteção do FGC até R$ 250.000,00.")
    print("=" * 80)


if __name__ == '__main__':
    main()
