#!/usr/bin/env python3
"""
Main script to analyze planner cards and generate report
"""

import sys
from sample_data import create_sample_data
from report_generator import ReportGenerator


def main():
    """Main function to run the planner cards analysis"""
    print("=" * 80)
    print("Sistema de Análise de Cards do Planner")
    print("=" * 80)
    print()
    
    # Load sample data
    print("Carregando dados dos cards...")
    card_manager = create_sample_data()
    print(f"✓ {len(card_manager.get_all_cards())} cards carregados")
    print()
    
    # Create report generator
    print("Gerando relatório...")
    report_gen = ReportGenerator(card_manager)
    
    # Generate and display report
    report_text = report_gen.generate_text_report()
    print(report_text)
    
    # Save report to file
    filename = "relatorio_planner.txt"
    report_gen.save_report(filename)
    print()
    print(f"✓ Relatório salvo em: {filename}")
    print()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
