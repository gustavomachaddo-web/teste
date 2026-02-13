"""
Planner Cards Data Management
This module handles the data structure and operations for planner cards.
"""

from typing import List, Dict, Optional
from datetime import datetime
from enum import Enum


class CardStatus(Enum):
    """Status of a planner card"""
    NOT_STARTED = "Não Iniciado"
    IN_PROGRESS = "Em Progresso"
    COMPLETED = "Concluído"
    BLOCKED = "Bloqueado"


class CardPriority(Enum):
    """Priority levels for planner cards"""
    LOW = "Baixa"
    MEDIUM = "Média"
    HIGH = "Alta"
    URGENT = "Urgente"


class PlannerCard:
    """Represents a single planner card"""
    
    def __init__(
        self,
        id: int,
        title: str,
        description: str,
        status: CardStatus,
        priority: CardPriority,
        assignee: Optional[str] = None,
        created_date: Optional[datetime] = None,
        due_date: Optional[datetime] = None,
        tags: Optional[List[str]] = None
    ):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.assignee = assignee
        self.created_date = created_date or datetime.now()
        self.due_date = due_date
        self.tags = tags or []
    
    def to_dict(self) -> Dict:
        """Convert card to dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status.value,
            'priority': self.priority.value,
            'assignee': self.assignee,
            'created_date': self.created_date.isoformat() if self.created_date else None,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'tags': self.tags
        }
    
    def is_overdue(self) -> bool:
        """Check if card is overdue"""
        if self.due_date and self.status != CardStatus.COMPLETED:
            return datetime.now() > self.due_date
        return False


class PlannerCardManager:
    """Manages a collection of planner cards"""
    
    def __init__(self):
        self.cards: List[PlannerCard] = []
    
    def add_card(self, card: PlannerCard):
        """Add a card to the manager"""
        self.cards.append(card)
    
    def get_all_cards(self) -> List[PlannerCard]:
        """Get all cards"""
        return self.cards
    
    def get_cards_by_status(self, status: CardStatus) -> List[PlannerCard]:
        """Get cards filtered by status"""
        return [card for card in self.cards if card.status == status]
    
    def get_cards_by_priority(self, priority: CardPriority) -> List[PlannerCard]:
        """Get cards filtered by priority"""
        return [card for card in self.cards if card.priority == priority]
    
    def get_overdue_cards(self) -> List[PlannerCard]:
        """Get all overdue cards"""
        return [card for card in self.cards if card.is_overdue()]
    
    def get_cards_by_assignee(self, assignee: str) -> List[PlannerCard]:
        """Get cards assigned to a specific person"""
        return [card for card in self.cards if card.assignee == assignee]
