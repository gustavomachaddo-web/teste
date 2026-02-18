"""
Processador de Dados de Coordenadores
Analisa dados tabulares de performance e gera relatórios com plano de ação
"""

import csv
import json
from agent import DataMeasurementAgent
from typing import List, Dict, Any


def parse_percentage(value: str) -> float:
    """Converte string de percentual para float"""
    if not value or value.strip() == '':
        return 0.0
    # Remove % e converte vírgula para ponto
    value = value.replace('%', '').replace(',', '.').strip()
    try:
        return float(value)
    except ValueError:
        return 0.0


def parse_number(value: str) -> float:
    """Converte string numérica para float"""
    if not value or value.strip() == '':
        return 0.0
    # Remove pontos de milhar e converte vírgula decimal para ponto
    value = value.replace('.', '').replace(',', '.').strip()
    try:
        return float(value)
    except ValueError:
        return 0.0


def processar_dados_coordenadores(dados_csv: str) -> List[Dict[str, Any]]:
    """
    Processa dados de coordenadores e gera análise de KPIs
    
    Args:
        dados_csv: Caminho para arquivo CSV ou string com dados
        
    Returns:
        Lista de relatórios por coordenador
    """
    # Definir metas baseadas nos dados totais fornecidos
    config = {
        'kpis': {
            'atendimento': {
                'meta': 100.0,
                'descricao': '% de Atendimento',
                'inverso': False
            },
            'consultas_motor': {
                'meta': 67.0,
                'descricao': '% de Consultas ao Motor',
                'inverso': False
            },
            'conversao': {
                'meta': 2.09,
                'descricao': '% de Conversão de Contratos',
                'inverso': False
            },
            'tkm': {
                'meta': 5043,
                'descricao': 'TKM (Tonelada por Quilômetro)',
                'inverso': False
            }
        }
    }
    
    relatorios = []
    
    # Processar cada linha de dados
    lines = dados_csv.strip().split('\n')
    
    for line in lines[1:]:  # Pular cabeçalho
        # Parse da linha (tab-separated)
        campos = line.split('\t')
        
        if len(campos) < 13:
            continue
            
        coordenador = campos[0].strip()
        
        # Ignorar linhas totais ou vazias
        if not coordenador or coordenador.lower() in ['total', 'coordenador']:
            continue
        
        # Ignorar coordenadores sem dados significativos
        if 'VAGO' in coordenador.upper() or 'INTERINO' in coordenador.upper() or 'PROJETO' in coordenador.upper():
            continue
        
        # Extrair KPIs
        perc_atendimento = parse_percentage(campos[3])
        perc_consultas = parse_percentage(campos[5])
        perc_conversao = parse_percentage(campos[11])
        tkm = parse_number(campos[12])
        vendas = parse_number(campos[8])
        contratos = parse_number(campos[9])
        producao = parse_number(campos[10])
        
        # Se não há dados significativos, pular
        if perc_atendimento == 0 and perc_consultas == 0:
            continue
        
        # Criar agente para este coordenador
        agente = DataMeasurementAgent(config)
        
        # Mensurar KPIs disponíveis
        dados_kpis = {}
        
        if perc_atendimento > 0:
            dados_kpis['atendimento'] = perc_atendimento
        
        if perc_consultas > 0:
            dados_kpis['consultas_motor'] = perc_consultas
        
        if perc_conversao > 0:
            dados_kpis['conversao'] = perc_conversao
        
        if tkm > 0:
            dados_kpis['tkm'] = tkm
        
        # Processar KPIs
        if dados_kpis:
            agente.mensurar_dados(dados_kpis)
            relatorio = agente.gerar_relatorio()
            
            # Adicionar informações extras
            relatorio['coordenador'] = coordenador
            relatorio['vendas'] = vendas
            relatorio['contratos'] = contratos
            relatorio['producao'] = producao
            
            relatorios.append(relatorio)
    
    return relatorios


def gerar_relatorio_consolidado(relatorios: List[Dict[str, Any]]):
    """Gera relatório consolidado de todos os coordenadores"""
    
    print("\n" + "="*100)
    print("RELATÓRIO CONSOLIDADO DE PERFORMANCE - COORDENADORES")
    print("="*100)
    
    # Classificar por média de atingimento
    relatorios_ordenados = sorted(
        relatorios, 
        key=lambda x: x['resumo']['media_atingimento'],
        reverse=True
    )
    
    # Estatísticas gerais
    total_coordenadores = len(relatorios)
    coordenadores_criticos = sum(1 for r in relatorios if r['resumo']['kpis_criticos'] > 0)
    coordenadores_excelente = sum(1 for r in relatorios if r['resumo']['media_atingimento'] >= 100)
    
    print(f"\nTotal de Coordenadores Analisados: {total_coordenadores}")
    print(f"  - Performance Excelente (≥100%): {coordenadores_excelente}")
    print(f"  - Com KPIs Críticos: {coordenadores_criticos}")
    
    print("\n" + "-"*100)
    print("TOP 10 COORDENADORES - MELHOR PERFORMANCE")
    print("-"*100)
    print(f"{'#':<4} {'Coordenador':<40} {'Média':<10} {'KPIs OK':<10} {'Atenção':<10}")
    print("-"*100)
    
    for i, relatorio in enumerate(relatorios_ordenados[:10], 1):
        nome = relatorio['coordenador'][:38]
        media = f"{relatorio['resumo']['media_atingimento']:.1f}%"
        kpis_ok = relatorio['resumo']['kpis_excelente'] + relatorio['resumo']['kpis_bom']
        kpis_atencao = relatorio['resumo']['kpis_atencao'] + relatorio['resumo']['kpis_criticos']
        
        print(f"{i:<4} {nome:<40} {media:<10} {kpis_ok:<10} {kpis_atencao:<10}")
    
    print("\n" + "-"*100)
    print("COORDENADORES QUE REQUEREM ATENÇÃO")
    print("-"*100)
    
    # Coordenadores com KPIs críticos ou média baixa
    coordenadores_atencao = [
        r for r in relatorios 
        if r['resumo']['kpis_criticos'] > 0 or r['resumo']['media_atingimento'] < 80
    ]
    
    if coordenadores_atencao:
        print(f"{'Coordenador':<40} {'Média':<10} {'KPIs Críticos':<15} {'Principais Ações':<30}")
        print("-"*100)
        
        for relatorio in sorted(coordenadores_atencao, key=lambda x: x['resumo']['media_atingimento'])[:15]:
            nome = relatorio['coordenador'][:38]
            media = f"{relatorio['resumo']['media_atingimento']:.1f}%"
            criticos = relatorio['resumo']['kpis_criticos']
            
            # Pegar ação prioritária
            acoes_alta = [a for a in relatorio['plano_acao'] if a['prioridade'] == 'ALTA']
            acao = acoes_alta[0]['kpi'] if acoes_alta else 'N/A'
            
            print(f"{nome:<40} {media:<10} {criticos:<15} {acao:<30}")
    else:
        print("✓ Todos os coordenadores estão com performance adequada!")
    
    print("\n" + "="*100)


def gerar_relatorio_individual(relatorio: Dict[str, Any]):
    """Gera relatório detalhado de um coordenador"""
    
    print("\n" + "="*100)
    print(f"RELATÓRIO INDIVIDUAL - {relatorio['coordenador']}")
    print("="*100)
    
    resumo = relatorio['resumo']
    print(f"\nMédia de Atingimento: {resumo['media_atingimento']:.2f}%")
    print(f"Total de KPIs: {resumo['total_kpis']}")
    print(f"  - Excelente: {resumo['kpis_excelente']}")
    print(f"  - Bom: {resumo['kpis_bom']}")
    print(f"  - Atenção: {resumo['kpis_atencao']}")
    print(f"  - Crítico: {resumo['kpis_criticos']}")
    
    print(f"\nDados de Produção:")
    print(f"  - Vendas: {relatorio.get('vendas', 0):.0f}")
    print(f"  - Contratos: {relatorio.get('contratos', 0):.0f}")
    print(f"  - Produção: {relatorio.get('producao', 0):.0f}")
    
    print("\n" + "-"*100)
    print("DETALHAMENTO DOS KPIs")
    print("-"*100)
    
    for kpi in relatorio['kpis']:
        status_emoji = {
            'excelente': '✓',
            'bom': '○',
            'atenção': '⚠',
            'crítico': '✗'
        }.get(kpi['status'], '?')
        
        print(f"\n{status_emoji} {kpi['nome'].upper()}")
        print(f"   Valor: {kpi['valor']:.2f} | Meta: {kpi['meta']:.2f}")
        print(f"   Atingimento: {kpi['percentual_atingido']:.1f}% - Status: {kpi['status'].upper()}")
    
    if relatorio['plano_acao']:
        print("\n" + "-"*100)
        print("PLANO DE AÇÃO RECOMENDADO")
        print("-"*100)
        
        for i, acao in enumerate(relatorio['plano_acao'], 1):
            print(f"\n{i}. [{acao['prioridade']}] {acao['kpi'].upper()}")
            print(f"   {acao['acao']}")
            print(f"   Prazo: {acao['prazo']}")
    
    print("\n" + "="*100)


def exemplo_uso_com_dados_reais():
    """Exemplo usando os dados reais fornecidos"""
    
    # Dados fornecidos pelo usuário
    dados_csv = """Coordenador	Transbordo	Atendimento	% Atendimento	Consulta Motor	% Consultas Motor	Encerramento até 10m	% Encerramento até 10m	Vendas	Contratos	Produção	% Conversão	TKM
ERNAUTON DENISAR ROLIM DE CASTRO SOBRINHO	230	230	100,00%	111	48,3%			0	0		0,00%	
EZEQUIEL THEISEN GUTJAHR	291	291	100,00%	143	49,1%			6	10	59.047	2,06%	9.841
CICERO ROMAO DE LIMA JUNIOR	446	446	100,00%	227	50,9%			9	14	13.439	2,02%	1.493
SUELLEN CAROLINE FERNANDES MACEDO	943	943	100,00%	525	55,7%			14	22	75.400	1,48%	5.386
ERIC DE BRITO REIS	745	745	100,00%	420	56,4%			13	18	31.358	1,74%	2.412
BRUNA PASSOS GONCALVES	889	889	100,00%	507	57,0%			9	11	11.667	1,01%	1.296
ANA ANGELICA QUIXABEIRA TAVARES	505	505	100,00%	289	57,2%			7	9	28.231	1,39%	4.033
JEFFERSON WILLIAM DE MORAIS RIBEIRO	462	462	100,00%	268	58,0%			12	17	44.557	2,60%	3.713
RAMON DE BRITO MACEDO	1.393	1.393	100,00%	818	58,7%			17	25	56.421	1,22%	3.319
MONIQUE PEREIRA DOS SANTOS	473	473	100,00%	282	59,6%			4	11	121.169	0,85%	30.292
JESSICA GOMES GENTILUOMO	531	531	100,00%	320	60,3%			4	11	20.203	0,75%	5.051
BRUNO CESAR DE SOUZA GUERRA	985	985	100,00%	594	60,3%			17	27	92.281	1,73%	5.428
ROJANE MARIA GANJAO	478	478	100,00%	289	60,5%			7	9	36.369	1,46%	5.196
ALEXANDRA CARRUPT DE AZEVEDO PACHECO	659	659	100,00%	401	60,8%			14	28	42.861	2,12%	3.062
DANIELE DA SILVA PENA	787	787	100,00%	484	61,5%			12	17	75.344	1,52%	6.279
BRUNA RODRIGUES DA SILVA LIMA	423	423	100,00%	261	61,7%			13	21	70.972	3,07%	5.459
NAYRA LORRANE OLIVEIRA ANDRADE	1.194	1.194	100,00%	739	61,9%			27	33	94.193	2,26%	3.489
LUCAS SILVEIRA ARAUJO	614	614	100,00%	383	62,4%			9	12	120.443	1,47%	13.383
MARCELA OLINDA MOREIRA PINHEIRO PONTELO	1.082	1.082	100,00%	688	63,6%			21	36	94.451	1,94%	4.498
MURILO AMARAL DE OLIVEIRA	705	705	100,00%	450	63,8%			4	9	29.260	0,57%	7.315
NATHAN GABRIEL IARROCHESKI	634	634	100,00%	411	64,8%			12	26	89.528	1,89%	7.461
CLEBER DE SALES TINI	1.196	1.196	100,00%	778	65,1%			22	27	119.711	1,84%	5.441
DANIELE DE BARROS CONCEICAO	885	885	100,00%	578	65,3%			17	25	101.147	1,92%	5.950
GABRIELA MARINHO CURTY	998	998	100,00%	652	65,3%			32	42	110.185	3,21%	3.443
RAQUEL COELHO RIGHETTI MELINO	2.038	2.038	100,00%	1.342	65,8%			42	68	217.755	2,06%	5.185
KARINA OLIVEIRA GOMES DA SILVA	1.073	1.073	100,00%	709	66,1%			19	20	47.778	1,77%	2.515
GLAUBER LARANJEIRA DO NASCIMENTO	888	888	100,00%	601	67,7%			27	49	188.010	3,04%	6.963
BARBARA GONZAGA DOS SANTOS	633	633	100,00%	431	68,1%			17	31	63.241	2,69%	3.720
TATIANE CARINA OLIVEIRA SOUZA	1.487	1.487	100,00%	1.018	68,5%			24	33	184.327	1,61%	7.680
INGRID GOMES MARCELINO	395	395	100,00%	271	68,6%			17	21	50.098	4,30%	2.947
ALEX SANDRO DA SILVA	670	670	100,00%	461	68,8%			11	26	131.727	1,64%	11.975
FERNANDA BASTOS MONTE	698	698	100,00%	483	69,2%			15	28	90.286	2,15%	6.019
JOHN CRYSTIAN FARIA	830	830	100,00%	577	69,5%			15	16	81.713	1,81%	5.448
NAYARA DA PENHA SILVA ALMEIDA	979	979	100,00%	685	70,0%			37	50	163.773	3,78%	4.426
THIAGO SANTOS DE MOURA	1.234	1.234	100,00%	868	70,3%			40	54	136.735	3,24%	3.418
IVAN FRANCISCO KARL COSTA	893	893	100,00%	635	71,1%			20	31	112.212	2,24%	5.611
CARINA DA SILVA SIMOES FARIAS	669	669	100,00%	481	71,9%			20	27	81.628	2,99%	4.081
BRUNA CAROLINE PEREIRA DE SIQUEIRA	1.018	1.018	100,00%	732	71,9%			20	35	155.712	1,96%	7.786
LEONARDO RANGEL DE AZEVEDO	981	981	100,00%	713	72,7%			22	35	131.644	2,24%	5.984
BEATRIZ DOS SANTOS NUNES	393	393	100,00%	291	74,0%			10	12	17.899	2,54%	1.790
EDUARDO ANDRE RUEBENICH KOLLING	539	539	100,00%	401	74,4%			10	12	53.424	1,86%	5.342
MARIANA KITAMURA PRUDENTE	1.039	1.039	100,00%	776	74,7%			32	40	83.040	3,08%	2.595
ANDRE VINICIUS BARCELLOS GUTERRES	382	382	100,00%	287	75,1%			4	5	47.164	1,05%	11.791
RIVONIA SIQUEIRA DA SILVA	1.288	1.288	100,00%	973	75,5%			30	41	150.437	2,33%	5.015
JAMILE SANTOS SOUZA	738	738	100,00%	561	76,0%			30	52	171.320	4,07%	5.711
CLEYTON MENDES COLIM	402	402	100,00%	307	76,4%			18	22	73.113	4,48%	4.062
MERCIA MEZALINA ALCANTARA CAMPOS DE SILVEIRA	389	389	100,00%	307	78,9%			4	6	5.397	1,03%	1.349
LUCAS LEANDRO DE SENA LOPES	451	451	100,00%	360	79,8%			8	12	55.365	1,77%	6.921
VANESSA ALVES DA SILVA	1.143	1.143	100,00%	915	80,1%			25	29	145.254	2,19%	5.810
LUIZ FLAVIO LADISLAU	708	708	100,00%	568	80,2%			20	24	95.472	2,82%	4.774
ANA LUCIA ROSA CAMPANER	1.043	1.043	100,00%	855	82,0%			17	30	102.952	1,63%	6.056
NICOLE LANAI BRAGA	506	506	100,00%	432	85,4%			12	23	56.142	2,37%	4.679"""
    
    # Processar dados
    print("\nProcessando dados dos coordenadores...")
    relatorios = processar_dados_coordenadores(dados_csv)
    print(f"✓ {len(relatorios)} coordenadores processados")
    
    # Gerar relatório consolidado
    gerar_relatorio_consolidado(relatorios)
    
    # Mostrar alguns relatórios individuais detalhados
    print("\n\n" + "="*100)
    print("RELATÓRIOS INDIVIDUAIS DETALHADOS - EXEMPLOS")
    print("="*100)
    
    # Top performer
    if relatorios:
        melhor = max(relatorios, key=lambda x: x['resumo']['media_atingimento'])
        gerar_relatorio_individual(melhor)
    
    # Alguém que precisa de atenção
    necessita_atencao = [r for r in relatorios if r['resumo']['media_atingimento'] < 80]
    if necessita_atencao:
        gerar_relatorio_individual(necessita_atencao[0])
    
    # Exportar todos para JSON
    output_file = '/tmp/relatorio_coordenadores_completo.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(relatorios, f, indent=2, ensure_ascii=False)
    
    print(f"\n\n✓ Relatório completo exportado para: {output_file}")
    print(f"✓ Total de {len(relatorios)} coordenadores analisados")


if __name__ == '__main__':
    exemplo_uso_com_dados_reais()
