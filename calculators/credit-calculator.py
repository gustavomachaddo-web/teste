#!/usr/bin/env python3
"""
Calculadora de Crédito Consignado - Caso 6
Calcula parcelas, CET e gera cronograma de pagamentos
"""

import json
from datetime import datetime, timedelta
from decimal import Decimal, ROUND_HALF_UP


class CreditCalculator:
    """Calculadora de crédito consignado com taxa fixa"""
    
    def __init__(self, principal: float, term: int, annual_rate: float):
        """
        Inicializa a calculadora
        
        Args:
            principal: Valor principal solicitado em R$
            term: Prazo em meses
            annual_rate: Taxa de juros anual em %
        """
        self.principal = Decimal(str(principal))
        self.term = term
        self.annual_rate = Decimal(str(annual_rate))
        self.monthly_rate = self._calculate_monthly_rate()
        
    def _calculate_monthly_rate(self) -> Decimal:
        """Calcula taxa mensal a partir da taxa anual"""
        # Fórmula: (1 + i_anual)^(1/12) - 1
        annual_factor = (Decimal('1') + self.annual_rate / Decimal('100'))
        monthly_factor = annual_factor ** (Decimal('1') / Decimal('12'))
        return (monthly_factor - Decimal('1')) * Decimal('100')
    
    def calculate_monthly_payment(self) -> Decimal:
        """
        Calcula o valor da parcela mensal usando Sistema Price (SAC)
        
        Fórmula: PMT = PV × [i × (1+i)^n] / [(1+i)^n - 1]
        """
        i = self.monthly_rate / Decimal('100')
        n = Decimal(str(self.term))
        
        if i == 0:
            return self.principal / n
        
        factor = (Decimal('1') + i) ** n
        payment = self.principal * (i * factor) / (factor - Decimal('1'))
        
        return payment.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    
    def calculate_cet(self, additional_fees: float = 0) -> Decimal:
        """
        Calcula o CET (Custo Efetivo Total)
        
        Args:
            additional_fees: Taxas adicionais em R$
        
        Returns:
            CET em percentual anual
        """
        # Para simplificação, CET = taxa anual + impacto de taxas
        monthly_payment = self.calculate_monthly_payment()
        total_paid = monthly_payment * Decimal(str(self.term))
        
        if additional_fees > 0:
            total_with_fees = total_paid + Decimal(str(additional_fees))
            effective_rate = ((total_with_fees / self.principal) ** (Decimal('1') / (Decimal(str(self.term)) / Decimal('12')))) - Decimal('1')
            return (effective_rate * Decimal('100')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        
        return self.annual_rate
    
    def generate_schedule(self, start_date: datetime = None) -> list:
        """
        Gera o cronograma completo de pagamentos
        
        Args:
            start_date: Data do primeiro pagamento
        
        Returns:
            Lista de dicionários com detalhes de cada parcela
        """
        if start_date is None:
            start_date = datetime.now() + timedelta(days=30)
        
        monthly_payment = self.calculate_monthly_payment()
        remaining_balance = self.principal
        schedule = []
        
        for installment in range(1, self.term + 1):
            # Calcula juros da parcela
            interest = (remaining_balance * self.monthly_rate / Decimal('100')).quantize(
                Decimal('0.01'), rounding=ROUND_HALF_UP
            )
            
            # Calcula amortização
            principal_payment = monthly_payment - interest
            
            # Atualiza saldo devedor
            remaining_balance -= principal_payment
            
            # Ajusta última parcela para zerar saldo
            if installment == self.term:
                principal_payment += remaining_balance
                remaining_balance = Decimal('0')
            
            # Data de vencimento
            due_date = start_date + timedelta(days=30 * (installment - 1))
            
            schedule.append({
                'installmentNumber': installment,
                'dueDate': due_date.strftime('%Y-%m-%d'),
                'principalAmount': float(principal_payment),
                'interestAmount': float(interest),
                'totalAmount': float(monthly_payment),
                'remainingBalance': float(remaining_balance),
                'status': 'pendente'
            })
        
        return schedule
    
    def generate_summary(self, start_date: datetime = None) -> dict:
        """
        Gera um resumo completo do crédito
        
        Returns:
            Dicionário com todos os detalhes calculados
        """
        monthly_payment = self.calculate_monthly_payment()
        total_amount = monthly_payment * Decimal(str(self.term))
        total_interest = total_amount - self.principal
        cet = self.calculate_cet()
        
        schedule = self.generate_schedule(start_date)
        
        if start_date is None:
            start_date = datetime.now() + timedelta(days=30)
        
        last_date = start_date + timedelta(days=30 * self.term)
        
        return {
            'contractDetails': {
                'principalAmount': float(self.principal),
                'term': self.term,
                'monthlyRate': float(self.monthly_rate),
                'annualRate': float(self.annual_rate),
                'cet': float(cet),
                'monthlyPayment': float(monthly_payment),
                'totalAmount': float(total_amount),
                'totalInterest': float(total_interest)
            },
            'paymentDetails': {
                'firstDueDate': start_date.strftime('%Y-%m-%d'),
                'lastDueDate': last_date.strftime('%Y-%m-%d'),
                'paymentMethod': 'consignado'
            },
            'schedule': schedule
        }


def main():
    """Exemplo de uso da calculadora"""
    print("=" * 80)
    print("CALCULADORA DE CRÉDITO CONSIGNADO - CASO 6")
    print("=" * 80)
    print()
    
    # Parâmetros do Caso 6
    principal = 28000.00  # R$ 28.000
    term = 36  # 36 meses
    annual_rate = 16.08  # 16,08% a.a. (equivalente a ~1,25% a.m.)
    
    print(f"Valor solicitado: R$ {principal:,.2f}")
    print(f"Prazo: {term} meses")
    print(f"Taxa anual: {annual_rate:.2f}%")
    print()
    
    # Cria calculadora
    calculator = CreditCalculator(principal, term, annual_rate)
    
    # Gera resumo
    summary = calculator.generate_summary()
    
    print("-" * 80)
    print("RESUMO DO CRÉDITO")
    print("-" * 80)
    print(f"Taxa mensal: {summary['contractDetails']['monthlyRate']:.4f}%")
    print(f"Parcela mensal: R$ {summary['contractDetails']['monthlyPayment']:,.2f}")
    print(f"Total a pagar: R$ {summary['contractDetails']['totalAmount']:,.2f}")
    print(f"Total de juros: R$ {summary['contractDetails']['totalInterest']:,.2f}")
    print(f"CET: {summary['contractDetails']['cet']:.2f}% a.a.")
    print()
    
    print("-" * 80)
    print("CRONOGRAMA (Primeiras 5 parcelas)")
    print("-" * 80)
    print(f"{'Nº':<5} {'Vencimento':<12} {'Principal':>12} {'Juros':>12} {'Total':>12} {'Saldo':>12}")
    print("-" * 80)
    
    for i, installment in enumerate(summary['schedule'][:5]):
        print(
            f"{installment['installmentNumber']:<5} "
            f"{installment['dueDate']:<12} "
            f"R$ {installment['principalAmount']:>9,.2f} "
            f"R$ {installment['interestAmount']:>9,.2f} "
            f"R$ {installment['totalAmount']:>9,.2f} "
            f"R$ {installment['remainingBalance']:>9,.2f}"
        )
    
    print(f"{'...':<5} {'...':<12} {'...':<12} {'...':<12} {'...':<12} {'...':<12}")
    
    # Última parcela
    last = summary['schedule'][-1]
    print(
        f"{last['installmentNumber']:<5} "
        f"{last['dueDate']:<12} "
        f"R$ {last['principalAmount']:>9,.2f} "
        f"R$ {last['interestAmount']:>9,.2f} "
        f"R$ {last['totalAmount']:>9,.2f} "
        f"R$ {last['remainingBalance']:>9,.2f}"
    )
    print()
    
    # Salva em arquivo JSON
    output_file = '/tmp/credit_summary.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Resumo completo salvo em: {output_file}")
    print()
    
    # Mensagens de transparência
    print("-" * 80)
    print("💬 MENSAGENS DE TRANSPARÊNCIA")
    print("-" * 80)
    print("✓ Você vê tudo antes de contratar — simples e sem surpresas.")
    print("✓ Parcela fixa de R$ {:.2f} por {} meses.".format(
        summary['contractDetails']['monthlyPayment'], 
        term
    ))
    print("✓ CET de {:.2f}% a.a. - Custo total transparente!".format(
        summary['contractDetails']['cet']
    ))
    print("=" * 80)


if __name__ == '__main__':
    main()
