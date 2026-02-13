"""
Report Generator Module
Generates formatted reports from planner card analysis.
"""

from typing import Dict, List
from datetime import datetime
from planner_cards import PlannerCard, PlannerCardManager
from card_analyzer import CardAnalyzer


class ReportGenerator:
    """Generates formatted reports from card analysis"""
    
    def __init__(self, card_manager: PlannerCardManager):
        self.card_manager = card_manager
        self.analyzer = CardAnalyzer(card_manager)
    
    def generate_text_report(self) -> str:
        """Generate a text-based report"""
        report = []
        report.append("=" * 80)
        report.append("RELATÓRIO DE CARDS DO PLANNER")
        report.append("=" * 80)
        report.append(f"Data de Geração: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        report.append("")
        
        # Summary statistics
        stats = self.analyzer.get_summary_statistics()
        
        report.append("RESUMO GERAL")
        report.append("-" * 80)
        report.append(f"Total de Cards: {stats['total_cards']}")
        report.append(f"Taxa de Conclusão: {stats['completion_rate']:.2f}%")
        report.append(f"Cards Atrasados: {stats['overdue_count']}")
        report.append("")
        
        # Status distribution
        report.append("DISTRIBUIÇÃO POR STATUS")
        report.append("-" * 80)
        for status, count in stats['status_distribution'].items():
            percentage = (count / stats['total_cards'] * 100) if stats['total_cards'] > 0 else 0
            report.append(f"  {status}: {count} ({percentage:.1f}%)")
        report.append("")
        
        # Priority distribution
        report.append("DISTRIBUIÇÃO POR PRIORIDADE")
        report.append("-" * 80)
        for priority, count in stats['priority_distribution'].items():
            percentage = (count / stats['total_cards'] * 100) if stats['total_cards'] > 0 else 0
            report.append(f"  {priority}: {count} ({percentage:.1f}%)")
        report.append("")
        
        # Assignee workload
        if stats['assignee_workload']:
            report.append("CARGA DE TRABALHO POR RESPONSÁVEL")
            report.append("-" * 80)
            for assignee, count in sorted(
                stats['assignee_workload'].items(),
                key=lambda x: x[1],
                reverse=True
            ):
                report.append(f"  {assignee}: {count} cards")
            report.append("")
        
        # Tag distribution
        if stats['tag_distribution']:
            report.append("DISTRIBUIÇÃO POR TAGS")
            report.append("-" * 80)
            for tag, count in sorted(
                stats['tag_distribution'].items(),
                key=lambda x: x[1],
                reverse=True
            ):
                report.append(f"  {tag}: {count} cards")
            report.append("")
        
        # Overdue cards
        overdue_cards = self.card_manager.get_overdue_cards()
        if overdue_cards:
            report.append("CARDS ATRASADOS")
            report.append("-" * 80)
            for card in overdue_cards:
                report.append(f"  ID {card.id}: {card.title}")
                report.append(f"    Responsável: {card.assignee or 'Não atribuído'}")
                report.append(f"    Prazo: {card.due_date.strftime('%d/%m/%Y') if card.due_date else 'N/A'}")
                report.append(f"    Status: {card.status.value}")
                report.append("")
        
        # All cards detail
        report.append("DETALHAMENTO DE TODOS OS CARDS")
        report.append("-" * 80)
        for card in self.card_manager.get_all_cards():
            report.append(f"\nID: {card.id}")
            report.append(f"Título: {card.title}")
            report.append(f"Descrição: {card.description}")
            report.append(f"Status: {card.status.value}")
            report.append(f"Prioridade: {card.priority.value}")
            report.append(f"Responsável: {card.assignee or 'Não atribuído'}")
            if card.due_date:
                report.append(f"Prazo: {card.due_date.strftime('%d/%m/%Y')}")
            if card.tags:
                report.append(f"Tags: {', '.join(card.tags)}")
            report.append("-" * 40)
        
        report.append("")
        report.append("=" * 80)
        report.append("FIM DO RELATÓRIO")
        report.append("=" * 80)
        
        return "\n".join(report)
    
    def save_report(self, filename: str = "relatorio_planner.txt"):
        """Save report to a file"""
        report_text = self.generate_text_report()
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report_text)
        return filename
