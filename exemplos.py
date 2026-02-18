"""
Exemplo avançado de uso do Agente de Mensuração de Dados e KPIs

Este exemplo mostra como:
1. Carregar configuração de um arquivo JSON
2. Processar múltiplos períodos de dados
3. Comparar resultados ao longo do tempo
"""

import json
from agent import DataMeasurementAgent


def exemplo_com_config_json():
    """Exemplo carregando configuração de arquivo JSON"""
    print("\n=== EXEMPLO 1: Usando arquivo de configuração JSON ===\n")
    
    # Carregar configuração do arquivo
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    # Inicializar agente
    agente = DataMeasurementAgent(config)
    
    # Dados do mês atual
    dados_atual = {
        'vendas_mensais': 120000,
        'satisfacao_cliente': 88,
        'taxa_conversao': 16,
        'tempo_resposta': 18,
        'retencao_clientes': 90,
        'nps': 75,
        'ticket_medio': 520,
        'churn_rate': 4.5
    }
    
    # Processar medições
    agente.mensurar_dados(dados_atual)
    
    # Imprimir relatório
    agente.imprimir_relatorio()


def exemplo_adicionar_kpis_dinamicamente():
    """Exemplo adicionando KPIs dinamicamente"""
    print("\n=== EXEMPLO 2: Adicionando KPIs Dinamicamente ===\n")
    
    # Inicializar agente sem configuração
    agente = DataMeasurementAgent()
    
    # Adicionar KPIs dinamicamente
    agente.definir_kpi('usuarios_ativos', 10000, 'Número de usuários ativos mensais')
    agente.definir_kpi('taxa_engajamento', 45, 'Taxa de engajamento (%)')
    agente.definir_kpi('receita_recorrente', 50000, 'Receita recorrente mensal (MRR)')
    
    # Mensurar dados
    dados = {
        'usuarios_ativos': 8500,
        'taxa_engajamento': 52,
        'receita_recorrente': 48000
    }
    
    agente.mensurar_dados(dados)
    agente.imprimir_relatorio()


def exemplo_comparacao_periodos():
    """Exemplo comparando dados de diferentes períodos"""
    print("\n=== EXEMPLO 3: Comparação de Períodos ===\n")
    
    # Configuração básica
    config = {
        'kpis': {
            'vendas': {'meta': 100000, 'descricao': 'Vendas mensais'},
            'clientes_novos': {'meta': 50, 'descricao': 'Novos clientes'},
            'satisfacao': {'meta': 85, 'descricao': 'Satisfação (%)'}
        }
    }
    
    periodos = {
        'Janeiro': {'vendas': 85000, 'clientes_novos': 42, 'satisfacao': 82},
        'Fevereiro': {'vendas': 95000, 'clientes_novos': 48, 'satisfacao': 87},
        'Março': {'vendas': 105000, 'clientes_novos': 55, 'satisfacao': 89}
    }
    
    for periodo, dados in periodos.items():
        print(f"\n{'='*80}")
        print(f"PERÍODO: {periodo}")
        print('='*80)
        
        agente = DataMeasurementAgent(config)
        agente.mensurar_dados(dados)
        
        relatorio = agente.gerar_relatorio()
        print(f"\nMédia de Atingimento: {relatorio['resumo']['media_atingimento']:.2f}%")
        print(f"KPIs Excelente: {relatorio['resumo']['kpis_excelente']}")
        print(f"KPIs em Atenção/Crítico: {relatorio['resumo']['kpis_atencao'] + relatorio['resumo']['kpis_criticos']}")


def exemplo_exportacao_json():
    """Exemplo de exportação para JSON"""
    print("\n=== EXEMPLO 4: Exportação para JSON ===\n")
    
    config = {
        'kpis': {
            'producao': {'meta': 1000, 'descricao': 'Unidades produzidas'},
            'qualidade': {'meta': 95, 'descricao': 'Taxa de qualidade (%)'},
            'eficiencia': {'meta': 80, 'descricao': 'Eficiência operacional (%)'}
        }
    }
    
    agente = DataMeasurementAgent(config)
    
    dados = {
        'producao': 950,
        'qualidade': 97,
        'eficiencia': 75
    }
    
    agente.mensurar_dados(dados)
    
    # Exportar para JSON
    arquivo_saida = '/tmp/relatorio_producao.json'
    agente.exportar_json(arquivo_saida)
    
    print(f"\n✓ Relatório exportado com sucesso!")
    print(f"  Arquivo: {arquivo_saida}")
    
    # Ler e mostrar preview
    with open(arquivo_saida, 'r', encoding='utf-8') as f:
        dados_json = json.load(f)
    
    print(f"\n  Total de KPIs: {dados_json['resumo']['total_kpis']}")
    print(f"  Média de Atingimento: {dados_json['resumo']['media_atingimento']:.2f}%")
    print(f"  Planos de Ação: {len(dados_json['plano_acao'])}")


def exemplo_cenario_critico():
    """Exemplo com cenário crítico que gera ações urgentes"""
    print("\n=== EXEMPLO 5: Cenário Crítico - Ações Urgentes ===\n")
    
    config = {
        'kpis': {
            'disponibilidade_sistema': {'meta': 99.9, 'descricao': 'Uptime (%)'},
            'tempo_resposta_api': {'meta': 200, 'descricao': 'Tempo de resposta (ms)'},
            'erros_aplicacao': {'meta': 10, 'descricao': 'Erros por hora'}
        }
    }
    
    agente = DataMeasurementAgent(config)
    
    # Dados críticos
    dados_criticos = {
        'disponibilidade_sistema': 95.5,  # Muito abaixo da meta
        'tempo_resposta_api': 180,         # Bom
        'erros_aplicacao': 4               # Excelente (menos erros é melhor)
    }
    
    agente.mensurar_dados(dados_criticos)
    agente.imprimir_relatorio()


if __name__ == '__main__':
    # Executar todos os exemplos
    exemplo_com_config_json()
    input("\nPressione Enter para continuar...")
    
    exemplo_adicionar_kpis_dinamicamente()
    input("\nPressione Enter para continuar...")
    
    exemplo_comparacao_periodos()
    input("\nPressione Enter para continuar...")
    
    exemplo_exportacao_json()
    input("\nPressione Enter para continuar...")
    
    exemplo_cenario_critico()
    
    print("\n" + "="*80)
    print("EXEMPLOS CONCLUÍDOS!")
    print("="*80)
    print("\nConfira os arquivos JSON gerados em /tmp/")
