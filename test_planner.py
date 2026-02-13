#!/usr/bin/env python3
"""
Simple tests for the planner cards system
"""

from datetime import datetime, timedelta
from planner_cards import PlannerCard, PlannerCardManager, CardStatus, CardPriority
from card_analyzer import CardAnalyzer
from report_generator import ReportGenerator


def test_card_creation():
    """Test creating a planner card"""
    card = PlannerCard(
        id=1,
        title="Test Card",
        description="Test Description",
        status=CardStatus.IN_PROGRESS,
        priority=CardPriority.HIGH,
        assignee="Test User",
        tags=["test", "example"]
    )
    
    assert card.id == 1
    assert card.title == "Test Card"
    assert card.status == CardStatus.IN_PROGRESS
    assert card.priority == CardPriority.HIGH
    assert card.assignee == "Test User"
    assert "test" in card.tags
    print("✓ test_card_creation passed")


def test_overdue_detection():
    """Test overdue card detection"""
    # Create overdue card
    overdue_card = PlannerCard(
        id=1,
        title="Overdue Card",
        description="This card is overdue",
        status=CardStatus.IN_PROGRESS,
        priority=CardPriority.HIGH,
        due_date=datetime.now() - timedelta(days=5)
    )
    
    assert overdue_card.is_overdue() == True
    
    # Create not overdue card
    not_overdue_card = PlannerCard(
        id=2,
        title="Not Overdue Card",
        description="This card is not overdue",
        status=CardStatus.IN_PROGRESS,
        priority=CardPriority.HIGH,
        due_date=datetime.now() + timedelta(days=5)
    )
    
    assert not_overdue_card.is_overdue() == False
    
    # Completed cards are never overdue
    completed_card = PlannerCard(
        id=3,
        title="Completed Card",
        description="This card is completed",
        status=CardStatus.COMPLETED,
        priority=CardPriority.HIGH,
        due_date=datetime.now() - timedelta(days=10)
    )
    
    assert completed_card.is_overdue() == False
    print("✓ test_overdue_detection passed")


def test_card_manager():
    """Test card manager functionality"""
    manager = PlannerCardManager()
    
    card1 = PlannerCard(
        id=1,
        title="Card 1",
        description="Description 1",
        status=CardStatus.IN_PROGRESS,
        priority=CardPriority.HIGH
    )
    
    card2 = PlannerCard(
        id=2,
        title="Card 2",
        description="Description 2",
        status=CardStatus.COMPLETED,
        priority=CardPriority.MEDIUM
    )
    
    manager.add_card(card1)
    manager.add_card(card2)
    
    assert len(manager.get_all_cards()) == 2
    assert len(manager.get_cards_by_status(CardStatus.IN_PROGRESS)) == 1
    assert len(manager.get_cards_by_status(CardStatus.COMPLETED)) == 1
    assert len(manager.get_cards_by_priority(CardPriority.HIGH)) == 1
    print("✓ test_card_manager passed")


def test_analyzer():
    """Test card analyzer"""
    manager = PlannerCardManager()
    
    # Add cards with different statuses and priorities
    for i in range(5):
        manager.add_card(PlannerCard(
            id=i,
            title=f"Card {i}",
            description=f"Description {i}",
            status=CardStatus.COMPLETED if i < 2 else CardStatus.IN_PROGRESS,
            priority=CardPriority.HIGH if i < 3 else CardPriority.LOW,
            assignee="User A" if i < 3 else "User B"
        ))
    
    analyzer = CardAnalyzer(manager)
    
    stats = analyzer.get_summary_statistics()
    assert stats['total_cards'] == 5
    assert stats['completion_rate'] == 40.0  # 2 out of 5 completed
    assert len(stats['status_distribution']) > 0
    assert len(stats['priority_distribution']) > 0
    assert len(stats['assignee_workload']) == 2
    print("✓ test_analyzer passed")


def test_report_generation():
    """Test report generation"""
    manager = PlannerCardManager()
    
    manager.add_card(PlannerCard(
        id=1,
        title="Test Card",
        description="Test Description",
        status=CardStatus.IN_PROGRESS,
        priority=CardPriority.HIGH
    ))
    
    report_gen = ReportGenerator(manager)
    report = report_gen.generate_text_report()
    
    assert "RELATÓRIO DE CARDS DO PLANNER" in report
    assert "RESUMO GERAL" in report
    assert "Test Card" in report
    assert "Total de Cards: 1" in report
    print("✓ test_report_generation passed")


def run_all_tests():
    """Run all tests"""
    print("=" * 80)
    print("Running Tests for Planner Cards System")
    print("=" * 80)
    print()
    
    test_card_creation()
    test_overdue_detection()
    test_card_manager()
    test_analyzer()
    test_report_generation()
    
    print()
    print("=" * 80)
    print("All tests passed! ✓")
    print("=" * 80)


if __name__ == "__main__":
    run_all_tests()
