"""
Sample data for testing the planner cards system
"""

from datetime import datetime, timedelta
from planner_cards import PlannerCard, PlannerCardManager, CardStatus, CardPriority


def create_sample_data() -> PlannerCardManager:
    """Create sample planner cards for testing"""
    manager = PlannerCardManager()
    
    # Create various sample cards
    cards_data = [
        {
            'id': 1,
            'title': 'Desenvolver funcionalidade de login',
            'description': 'Implementar sistema de autenticação com email e senha',
            'status': CardStatus.COMPLETED,
            'priority': CardPriority.HIGH,
            'assignee': 'João Silva',
            'created_date': datetime.now() - timedelta(days=30),
            'due_date': datetime.now() - timedelta(days=5),
            'tags': ['desenvolvimento', 'backend', 'segurança']
        },
        {
            'id': 2,
            'title': 'Criar dashboard de relatórios',
            'description': 'Desenvolver interface para visualização de métricas',
            'status': CardStatus.IN_PROGRESS,
            'priority': CardPriority.HIGH,
            'assignee': 'Maria Santos',
            'created_date': datetime.now() - timedelta(days=20),
            'due_date': datetime.now() + timedelta(days=5),
            'tags': ['desenvolvimento', 'frontend', 'UI/UX']
        },
        {
            'id': 3,
            'title': 'Otimizar consultas no banco de dados',
            'description': 'Melhorar performance das queries principais',
            'status': CardStatus.IN_PROGRESS,
            'priority': CardPriority.MEDIUM,
            'assignee': 'João Silva',
            'created_date': datetime.now() - timedelta(days=15),
            'due_date': datetime.now() + timedelta(days=10),
            'tags': ['backend', 'performance', 'database']
        },
        {
            'id': 4,
            'title': 'Implementar testes automatizados',
            'description': 'Criar suite de testes unitários e de integração',
            'status': CardStatus.NOT_STARTED,
            'priority': CardPriority.MEDIUM,
            'assignee': 'Pedro Oliveira',
            'created_date': datetime.now() - timedelta(days=10),
            'due_date': datetime.now() + timedelta(days=15),
            'tags': ['testes', 'qualidade']
        },
        {
            'id': 5,
            'title': 'Corrigir bug no checkout',
            'description': 'Resolver problema de cálculo de desconto no checkout',
            'status': CardStatus.BLOCKED,
            'priority': CardPriority.URGENT,
            'assignee': 'Maria Santos',
            'created_date': datetime.now() - timedelta(days=5),
            'due_date': datetime.now() - timedelta(days=2),
            'tags': ['bug', 'frontend', 'urgente']
        },
        {
            'id': 6,
            'title': 'Atualizar documentação da API',
            'description': 'Documentar novos endpoints e atualizar exemplos',
            'status': CardStatus.IN_PROGRESS,
            'priority': CardPriority.LOW,
            'assignee': 'Pedro Oliveira',
            'created_date': datetime.now() - timedelta(days=8),
            'due_date': datetime.now() + timedelta(days=20),
            'tags': ['documentação', 'API']
        },
        {
            'id': 7,
            'title': 'Configurar ambiente de staging',
            'description': 'Preparar ambiente de testes antes da produção',
            'status': CardStatus.COMPLETED,
            'priority': CardPriority.MEDIUM,
            'assignee': 'Ana Costa',
            'created_date': datetime.now() - timedelta(days=25),
            'due_date': datetime.now() - timedelta(days=10),
            'tags': ['devops', 'infraestrutura']
        },
        {
            'id': 8,
            'title': 'Implementar notificações por email',
            'description': 'Sistema de envio de emails transacionais',
            'status': CardStatus.NOT_STARTED,
            'priority': CardPriority.LOW,
            'assignee': 'João Silva',
            'created_date': datetime.now() - timedelta(days=7),
            'due_date': datetime.now() + timedelta(days=30),
            'tags': ['desenvolvimento', 'backend', 'notificações']
        },
        {
            'id': 9,
            'title': 'Revisar código do módulo de pagamentos',
            'description': 'Code review e refatoração do módulo de pagamentos',
            'status': CardStatus.IN_PROGRESS,
            'priority': CardPriority.HIGH,
            'assignee': 'Ana Costa',
            'created_date': datetime.now() - timedelta(days=3),
            'due_date': datetime.now() + timedelta(days=3),
            'tags': ['code-review', 'pagamentos', 'segurança']
        },
        {
            'id': 10,
            'title': 'Criar landing page promocional',
            'description': 'Desenvolver página para campanha de marketing',
            'status': CardStatus.NOT_STARTED,
            'priority': CardPriority.MEDIUM,
            'assignee': None,
            'created_date': datetime.now() - timedelta(days=2),
            'due_date': datetime.now() + timedelta(days=25),
            'tags': ['frontend', 'marketing', 'UI/UX']
        }
    ]
    
    # Add all cards to manager
    for card_data in cards_data:
        card = PlannerCard(**card_data)
        manager.add_card(card)
    
    return manager
