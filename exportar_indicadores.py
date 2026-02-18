"""
Exportar Indicadores - Gera relatório JSON com todos os indicadores e medições
"""

import json
import os
from datetime import datetime
from consultar_indicadores import carregar_configuracao
from agent import DataMeasurementAgent


def exportar_indicadores_json(caminho_saida: str = 'indicadores_e_medicoes.json'):
    """
    Exporta indicadores e medições de exemplo para JSON
    
    Args:
        caminho_saida: Caminho do arquivo de saída
    """
    # Carregar configuração
    config = carregar_configuracao()
    
    # Preparar estrutura de saída
    saida = {
        'timestamp': datetime.now().isoformat(),
        'indicadores': {},
        'medicoes_exemplo': {},
        'resumo': {}
    }
    
    # Adicionar indicadores configurados
    for nome, detalhes in config.get('kpis', {}).items():
        saida['indicadores'][nome] = {
            'descricao': detalhes.get('descricao', ''),
            'meta': detalhes.get('meta', 0),
            'tipo': 'inverso' if detalhes.get('inverso', False) else 'normal',
            'tipo_descricao': 'menor é melhor' if detalhes.get('inverso', False) else 'maior é melhor'
        }
    
    # Criar agente e adicionar medições de exemplo
    agente = DataMeasurementAgent(config)
    
    dados_exemplo = {
        'vendas_mensais': 95000,
        'satisfacao_cliente': 88,
        'taxa_conversao': 12,
        'tempo_resposta': 20,
        'retencao_clientes': 82,
        'nps': 75,
        'ticket_medio': 520,
        'churn_rate': 4.2
    }
    
    # Mensurar apenas os KPIs que existem na configuração
    dados_validos = {k: v for k, v in dados_exemplo.items() if k in config.get('kpis', {})}
    
    if dados_validos:
        agente.mensurar_dados(dados_validos)
        relatorio = agente.gerar_relatorio()
        
        # Adicionar medições
        for kpi in relatorio['kpis']:
            saida['medicoes_exemplo'][kpi['nome']] = {
                'valor_medido': kpi['valor'],
                'meta': kpi['meta'],
                'percentual_atingido': kpi['percentual_atingido'],
                'status': kpi['status']
            }
        
        # Adicionar resumo
        saida['resumo'] = relatorio['resumo']
    
    # Salvar arquivo
    with open(caminho_saida, 'w', encoding='utf-8') as f:
        json.dump(saida, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Indicadores exportados para: {caminho_saida}")
    print(f"  Total de indicadores: {len(saida['indicadores'])}")
    print(f"  Medições de exemplo: {len(saida['medicoes_exemplo'])}")
    
    return saida


if __name__ == '__main__':
    import sys
    
    # Permitir especificar arquivo de saída
    arquivo = sys.argv[1] if len(sys.argv) > 1 else 'indicadores_e_medicoes.json'
    
    print("\n" + "="*80)
    print("EXPORTAÇÃO DE INDICADORES E MEDIÇÕES")
    print("="*80)
    
    resultado = exportar_indicadores_json(arquivo)
    
    print("\n" + "-"*80)
    print("PREVIEW DO ARQUIVO:")
    print("-"*80)
    print(json.dumps(resultado, indent=2, ensure_ascii=False)[:500] + "...")
    print("\n" + "="*80)
