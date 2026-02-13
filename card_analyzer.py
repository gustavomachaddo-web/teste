"""
Card Analyzer Module
Analyzes planner cards and generates statistics and insights.
"""

from typing import Dict, List
from collections import Counter
from planner_cards import PlannerCard, PlannerCardManager, CardStatus, CardPriority


class CardAnalyzer:
    """Analyzes planner cards and generates insights"""
    
    def __init__(self, card_manager: PlannerCardManager):
        self.card_manager = card_manager
    
    def get_status_distribution(self) -> Dict[str, int]:
        """Get distribution of cards by status"""
        cards = self.card_manager.get_all_cards()
        status_counts = Counter(card.status.value for card in cards)
        return dict(status_counts)
    
    def get_priority_distribution(self) -> Dict[str, int]:
        """Get distribution of cards by priority"""
        cards = self.card_manager.get_all_cards()
        priority_counts = Counter(card.priority.value for card in cards)
        return dict(priority_counts)
    
    def get_assignee_workload(self) -> Dict[str, int]:
        """Get number of cards per assignee"""
        cards = self.card_manager.get_all_cards()
        assignee_counts = Counter(
            card.assignee for card in cards if card.assignee
        )
        return dict(assignee_counts)
    
    def get_completion_rate(self) -> float:
        """Calculate completion rate as percentage"""
        cards = self.card_manager.get_all_cards()
        if not cards:
            return 0.0
        
        completed = sum(
            1 for card in cards if card.status == CardStatus.COMPLETED
        )
        return (completed / len(cards)) * 100
    
    def get_overdue_count(self) -> int:
        """Get count of overdue cards"""
        return len(self.card_manager.get_overdue_cards())
    
    def get_tag_distribution(self) -> Dict[str, int]:
        """Get distribution of tags across cards"""
        cards = self.card_manager.get_all_cards()
        all_tags = []
        for card in cards:
            all_tags.extend(card.tags)
        
        tag_counts = Counter(all_tags)
        return dict(tag_counts)
    
    def get_summary_statistics(self) -> Dict:
        """Get comprehensive summary statistics"""
        cards = self.card_manager.get_all_cards()
        
        return {
            'total_cards': len(cards),
            'status_distribution': self.get_status_distribution(),
            'priority_distribution': self.get_priority_distribution(),
            'assignee_workload': self.get_assignee_workload(),
            'completion_rate': self.get_completion_rate(),
            'overdue_count': self.get_overdue_count(),
            'tag_distribution': self.get_tag_distribution()
        }
