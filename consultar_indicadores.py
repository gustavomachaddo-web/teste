"""
Consultar Indicadores e Medições
Script para visualizar os indicadores (KPIs) configurados e suas medições
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime
from agent import DataMeasurementAgent


def carregar_configuracao(caminho: str = 'config.json') -> Dict[str, Any]:
    """
    Carrega a configuração de KPIs do arquivo
    
    Args:
        caminho: Caminho para o arquivo de configuração
        
    Returns:
        Dicionário com a configuração
    """
    if not os.path.exists(caminho):
        return {'kpis': {}}
    
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)


def exibir_indicadores(config: Dict[str, Any]):
    """
    Exibe todos os indicadores configurados
    
    Args:
        config: Configuração de KPIs
    """
    print("\n" + "="*80)
    print("INDICADORES (KPIs) CONFIGURADOS")
    print("="*80)
    
    if not config.get('kpis'):
        print("\nNenhum indicador configurado.")
        return
    
    print(f"\nTotal de Indicadores: {len(config['kpis'])}")
    print("\n" + "-"*80)
    
    for i, (nome, detalhes) in enumerate(config['kpis'].items(), 1):
        tipo = "INVERSO (menor é melhor)" if detalhes.get('inverso', False) else "NORMAL (maior é melhor)"
        
        print(f"\n{i}. {nome.upper()}")
        print(f"   Descrição: {detalhes.get('descricao', 'N/A')}")
        print(f"   Meta: {detalhes.get('meta', 0):,.2f}")
        print(f"   Tipo: {tipo}")
    
    print("\n" + "="*80)


def exibir_medicoes_exemplo(config: Dict[str, Any]):
    """
    Exibe um exemplo de medições para demonstrar o uso
    
    Args:
        config: Configuração de KPIs
    """
    print("\n" + "="*80)
    print("EXEMPLO DE MEDIÇÕES")
    print("="*80)
    
    # Criar agente
    agente = DataMeasurementAgent(config)
    
    # Dados de exemplo (valores fictícios para demonstração)
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
    
    print("\nMedindo KPIs com dados de exemplo...")
    
    # Mensurar apenas os KPIs que existem na configuração
    dados_validos = {k: v for k, v in dados_exemplo.items() if k in config.get('kpis', {})}
    
    if not dados_validos:
        print("\nNenhum dado válido para medir.")
        return
    
    agente.mensurar_dados(dados_validos)
    
    # Exibir resultados
    print("\n" + "-"*80)
    print("RESULTADOS DAS MEDIÇÕES")
    print("-"*80)
    
    for resultado in agente.resultados_kpis:
        status_emoji = {
            'excelente': '✓ EXCELENTE',
            'bom': '○ BOM',
            'atenção': '⚠ ATENÇÃO',
            'crítico': '✗ CRÍTICO'
        }.get(resultado.status.value, '?')
        
        print(f"\n{resultado.nome.upper()}")
        print(f"  Valor Medido: {resultado.valor:,.2f}")
        print(f"  Meta: {resultado.meta:,.2f}")
        print(f"  Atingimento: {resultado.percentual_atingido:.1f}%")
        print(f"  Status: {status_emoji}")
    
    print("\n" + "-"*80)
    print("RESUMO")
    print("-"*80)
    
    relatorio = agente.gerar_relatorio()
    resumo = relatorio['resumo']
    
    print(f"\nMédia de Atingimento: {resumo['media_atingimento']:.1f}%")
    print(f"KPIs Excelente: {resumo['kpis_excelente']}")
    print(f"KPIs Bom: {resumo['kpis_bom']}")
    print(f"KPIs Atenção: {resumo['kpis_atencao']}")
    print(f"KPIs Crítico: {resumo['kpis_criticos']}")
    
    print("\n" + "="*80)


def exibir_estrutura_dados():
    """Exibe a estrutura de dados esperada para medições"""
    print("\n" + "="*80)
    print("COMO ADICIONAR MEDIÇÕES")
    print("="*80)
    
    print("""
Para adicionar medições, use o agente de mensuração:

1. Importar o agente:
   from agent import DataMeasurementAgent

2. Criar instância:
   config = carregar_configuracao('config.json')
   agente = DataMeasurementAgent(config)

3. Adicionar medições:
   dados = {
       'vendas_mensais': 95000,
       'satisfacao_cliente': 88,
       'taxa_conversao': 12,
       # ... outros indicadores
   }
   agente.mensurar_dados(dados)

4. Gerar relatório:
   agente.imprimir_relatorio()
   # ou
   agente.exportar_json('relatorio.json')

Exemplo prático:
   python agent.py          # Executa exemplo básico
   python exemplos.py       # Exemplos avançados
   python processar_coordenadores.py  # Análise em lote
""")
    
    print("="*80)


def menu_principal():
    """Menu principal interativo"""
    while True:
        print("\n" + "="*80)
        print("CONSULTA DE INDICADORES E MEDIÇÕES")
        print("="*80)
        print("\n1. Ver todos os indicadores configurados")
        print("2. Ver exemplo de medições")
        print("3. Ver como adicionar medições")
        print("4. Ver tudo")
        print("0. Sair")
        
        try:
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == '0':
                print("\nSaindo...")
                break
            elif opcao == '1':
                config = carregar_configuracao()
                exibir_indicadores(config)
            elif opcao == '2':
                config = carregar_configuracao()
                exibir_medicoes_exemplo(config)
            elif opcao == '3':
                exibir_estrutura_dados()
            elif opcao == '4':
                config = carregar_configuracao()
                exibir_indicadores(config)
                exibir_medicoes_exemplo(config)
                exibir_estrutura_dados()
            else:
                print("\nOpção inválida. Tente novamente.")
        except KeyboardInterrupt:
            print("\n\nSaindo...")
            break
        except Exception as e:
            print(f"\nErro: {e}")


def modo_automatico():
    """Modo automático - exibe tudo sem interação"""
    print("\n" + "="*80)
    print("CONSULTA DE INDICADORES E MEDIÇÕES")
    print(f"Data/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80)
    
    config = carregar_configuracao()
    exibir_indicadores(config)
    exibir_medicoes_exemplo(config)
    exibir_estrutura_dados()


if __name__ == '__main__':
    import sys
    
    # Se passar --auto, executa modo automático
    if '--auto' in sys.argv or '-a' in sys.argv:
        modo_automatico()
    else:
        menu_principal()
