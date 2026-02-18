// Estado da aplicação
let tasks = [];
let editingTaskId = null;
let currentView = 'board'; // board, analytics, timeline

// Constantes
const TIME_MIDNIGHT = 'T00:00:00';

// Elementos do DOM
const modal = document.getElementById('taskModal');
const addTaskBtn = document.getElementById('addTaskBtn');
const closeModal = document.querySelector('.close');
const cancelBtn = document.getElementById('cancelBtn');
const taskForm = document.getElementById('taskForm');
const modalTitle = document.getElementById('modalTitle');
const filterPriority = document.getElementById('filterPriority');
const filterStatus = document.getElementById('filterStatus');

// Inicialização
document.addEventListener('DOMContentLoaded', () => {
    loadTasks();
    renderCurrentView();
    setupEventListeners();
    setMinDate();
});

// Configurar listeners de eventos
function setupEventListeners() {
    addTaskBtn.addEventListener('click', openAddTaskModal);
    closeModal.addEventListener('click', closeTaskModal);
    cancelBtn.addEventListener('click', closeTaskModal);
    taskForm.addEventListener('submit', handleTaskSubmit);
    filterPriority.addEventListener('change', renderTasks);
    filterStatus.addEventListener('change', renderTasks);

    // Navegação entre visualizações
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const view = e.target.getAttribute('data-view');
            switchView(view);
        });
    });

    // Fechar modal ao clicar fora
    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeTaskModal();
        }
    });
}

// Definir data mínima como hoje
function setMinDate() {
    const today = new Date().toISOString().split('T')[0];
    document.getElementById('taskDueDate').setAttribute('min', today);
}

// Abrir modal para adicionar tarefa
function openAddTaskModal() {
    editingTaskId = null;
    modalTitle.textContent = 'Nova Atividade';
    taskForm.reset();
    modal.style.display = 'block';
}

// Abrir modal para editar tarefa
function openEditTaskModal(taskId) {
    editingTaskId = taskId;
    modalTitle.textContent = 'Editar Atividade';
    
    const task = tasks.find(t => t.id === taskId);
    if (task) {
        document.getElementById('taskTitle').value = task.title;
        document.getElementById('taskDescription').value = task.description || '';
        document.getElementById('taskDueDate').value = task.dueDate || '';
        document.getElementById('taskPriority').value = task.priority;
        document.getElementById('taskStatus').value = task.status;
        document.getElementById('taskCategory').value = task.category || '';
    }
    
    modal.style.display = 'block';
}

// Fechar modal
function closeTaskModal() {
    modal.style.display = 'none';
    taskForm.reset();
    editingTaskId = null;
}

// Manipular envio do formulário
function handleTaskSubmit(e) {
    e.preventDefault();
    
    const taskData = {
        title: document.getElementById('taskTitle').value.trim(),
        description: document.getElementById('taskDescription').value.trim(),
        dueDate: document.getElementById('taskDueDate').value,
        priority: document.getElementById('taskPriority').value,
        status: document.getElementById('taskStatus').value,
        category: document.getElementById('taskCategory').value.trim()
    };

    if (editingTaskId) {
        updateTask(editingTaskId, taskData);
    } else {
        addTask(taskData);
    }

    closeTaskModal();
}

// Adicionar nova tarefa
function addTask(taskData) {
    const task = {
        id: generateId(),
        ...taskData,
        createdAt: new Date().toISOString()
    };
    
    tasks.push(task);
    saveTasks();
    renderCurrentView();
    showNotification('Atividade adicionada com sucesso!', 'success');
}

// Atualizar tarefa existente
function updateTask(taskId, taskData) {
    const taskIndex = tasks.findIndex(t => t.id === taskId);
    if (taskIndex !== -1) {
        tasks[taskIndex] = {
            ...tasks[taskIndex],
            ...taskData,
            updatedAt: new Date().toISOString()
        };
        saveTasks();
        renderCurrentView();
        showNotification('Atividade atualizada com sucesso!', 'success');
    }
}

// Deletar tarefa
function deleteTask(taskId) {
    if (confirm('Tem certeza que deseja excluir esta atividade?')) {
        tasks = tasks.filter(t => t.id !== taskId);
        saveTasks();
        renderCurrentView();
        showNotification('Atividade excluída com sucesso!', 'success');
    }
}

// Renderizar tarefas
function renderTasks() {
    const pendingContainer = document.getElementById('pending-tasks');
    const inProgressContainer = document.getElementById('in-progress-tasks');
    const completedContainer = document.getElementById('completed-tasks');

    // Limpar containers
    pendingContainer.innerHTML = '';
    inProgressContainer.innerHTML = '';
    completedContainer.innerHTML = '';

    // Filtrar tarefas
    const filteredTasks = getFilteredTasks();

    // Separar tarefas por status
    const pendingTasks = filteredTasks.filter(t => t.status === 'pending');
    const inProgressTasks = filteredTasks.filter(t => t.status === 'in-progress');
    const completedTasks = filteredTasks.filter(t => t.status === 'completed');

    // Renderizar cada coluna
    renderTasksInColumn(pendingTasks, pendingContainer);
    renderTasksInColumn(inProgressTasks, inProgressContainer);
    renderTasksInColumn(completedTasks, completedContainer);

    // Atualizar contadores
    updateTaskCounts(pendingTasks.length, inProgressTasks.length, completedTasks.length);
}

// Renderizar tarefas em uma coluna
function renderTasksInColumn(tasks, container) {
    if (tasks.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <div class="empty-state-icon">📭</div>
                <div class="empty-state-text">Nenhuma atividade</div>
            </div>
        `;
        return;
    }

    tasks.forEach(task => {
        const taskCard = createTaskCard(task);
        container.appendChild(taskCard);
    });
}

// Criar card de tarefa
function createTaskCard(task) {
    const card = document.createElement('div');
    card.className = `task-card priority-${task.priority}`;
    
    const dueDateHtml = task.dueDate ? `
        <span class="due-date ${isOverdue(task.dueDate) ? 'overdue' : ''}">
            📅 ${formatDate(task.dueDate)}
            ${isOverdue(task.dueDate) ? ' (Atrasada)' : ''}
        </span>
    ` : '';

    const categoryHtml = task.category ? `
        <span class="task-badge category-badge">${task.category}</span>
    ` : '';

    card.innerHTML = `
        <div class="task-header">
            <div>
                <div class="task-title">${escapeHtml(task.title)}</div>
            </div>
            <div class="task-actions">
                <button class="task-btn" onclick="openEditTaskModal('${task.id}')" title="Editar">✏️</button>
                <button class="task-btn" onclick="deleteTask('${task.id}')" title="Excluir">🗑️</button>
            </div>
        </div>
        ${task.description ? `<div class="task-description">${escapeHtml(task.description)}</div>` : ''}
        <div class="task-meta">
            <span class="task-badge priority-badge ${task.priority}">
                ${getPriorityLabel(task.priority)}
            </span>
            ${categoryHtml}
            ${dueDateHtml}
        </div>
    `;

    return card;
}

// Obter tarefas filtradas
function getFilteredTasks() {
    let filtered = [...tasks];

    const priorityFilter = filterPriority.value;
    if (priorityFilter !== 'all') {
        filtered = filtered.filter(t => t.priority === priorityFilter);
    }

    const statusFilter = filterStatus.value;
    if (statusFilter !== 'all') {
        filtered = filtered.filter(t => t.status === statusFilter);
    }

    return filtered;
}

// Atualizar contadores de tarefas
function updateTaskCounts(pending, inProgress, completed) {
    document.getElementById('pending-count').textContent = pending;
    document.getElementById('in-progress-count').textContent = inProgress;
    document.getElementById('completed-count').textContent = completed;
}

// Utilitários
function generateId() {
    return 'task-' + Date.now() + '-' + Math.random().toString(36).substring(2, 11);
}

function formatDate(dateString) {
    const date = new Date(dateString + TIME_MIDNIGHT);
    return date.toLocaleDateString('pt-BR');
}

function isOverdue(dueDate) {
    if (!dueDate) return false;
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    const due = new Date(dueDate + TIME_MIDNIGHT);
    due.setHours(0, 0, 0, 0);
    return due < today;
}

function getPriorityLabel(priority) {
    const labels = {
        high: 'Alta',
        medium: 'Média',
        low: 'Baixa'
    };
    return labels[priority] || priority;
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function showNotification(message, type = 'info') {
    // Criar notificação
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${type === 'success' ? '#107c10' : '#0078d4'};
        color: white;
        padding: 15px 20px;
        border-radius: 4px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        z-index: 2000;
        animation: slideInRight 0.3s ease;
    `;
    notification.textContent = message;
    document.body.appendChild(notification);

    // Remover após 3 segundos
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Adicionar animações CSS dinamicamente
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Local Storage
function saveTasks() {
    localStorage.setItem('plannerTasks', JSON.stringify(tasks));
}

function loadTasks() {
    const saved = localStorage.getItem('plannerTasks');
    if (saved) {
        try {
            tasks = JSON.parse(saved);
        } catch (e) {
            console.error('Erro ao carregar tarefas:', e);
            tasks = [];
        }
    }
}

// Dados de exemplo (opcional - comentado para começar vazio)
/*
function loadSampleData() {
    if (tasks.length === 0) {
        tasks = [
            {
                id: generateId(),
                title: 'Reunião com a equipe',
                description: 'Discutir o progresso do projeto',
                dueDate: new Date().toISOString().split('T')[0],
                priority: 'high',
                status: 'pending',
                category: 'Trabalho',
                createdAt: new Date().toISOString()
            },
            {
                id: generateId(),
                title: 'Revisar documentação',
                description: 'Atualizar a documentação técnica',
                dueDate: '',
                priority: 'medium',
                status: 'in-progress',
                category: 'Trabalho',
                createdAt: new Date().toISOString()
            },
            {
                id: generateId(),
                title: 'Implementar nova funcionalidade',
                description: 'Desenvolver o sistema de agenda',
                dueDate: '',
                priority: 'high',
                status: 'completed',
                category: 'Desenvolvimento',
                createdAt: new Date().toISOString()
            }
        ];
        saveTasks();
    }
}
*/

// Navegação entre visualizações
function switchView(view) {
    currentView = view;

    // Atualizar botões de navegação
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.getAttribute('data-view') === view) {
            btn.classList.add('active');
        }
    });

    // Mostrar/ocultar seções
    const board = document.querySelector('.board');
    const controls = document.querySelector('.controls');
    const analyticsView = document.getElementById('analyticsView');
    const timelineView = document.getElementById('timelineView');

    board.style.display = 'none';
    controls.style.display = 'none';
    analyticsView.style.display = 'none';
    timelineView.style.display = 'none';

    if (view === 'board') {
        board.style.display = 'grid';
        controls.style.display = 'flex';
    } else if (view === 'analytics') {
        analyticsView.style.display = 'block';
        renderAnalytics();
    } else if (view === 'timeline') {
        timelineView.style.display = 'block';
        renderTimeline();
    }
}

function renderCurrentView() {
    if (currentView === 'board') {
        renderTasks();
    } else if (currentView === 'analytics') {
        renderAnalytics();
    } else if (currentView === 'timeline') {
        renderTimeline();
    }
}

// Análise e Estatísticas
function renderAnalytics() {
    const total = tasks.length;
    const completed = tasks.filter(t => t.status === 'completed').length;
    const inProgress = tasks.filter(t => t.status === 'in-progress').length;
    const pending = tasks.filter(t => t.status === 'pending').length;
    const overdue = tasks.filter(t => t.dueDate && isOverdue(t.dueDate) && t.status !== 'completed').length;
    
    const productivityRate = total > 0 ? Math.round((completed / total) * 100) : 0;

    // Atualizar cards de estatísticas
    document.getElementById('totalTasks').textContent = total;
    document.getElementById('completedTasks').textContent = completed;
    document.getElementById('inProgressTasks').textContent = inProgress;
    document.getElementById('pendingTasks').textContent = pending;
    document.getElementById('overdueTasks').textContent = overdue;
    document.getElementById('productivityRate').textContent = productivityRate + '%';

    // Gráfico de status
    updateBarChart('statusChart', {
        'Pendente': pending,
        'Em Progresso': inProgress,
        'Concluída': completed
    }, total);

    // Gráfico de prioridades
    const highPriority = tasks.filter(t => t.priority === 'high').length;
    const mediumPriority = tasks.filter(t => t.priority === 'medium').length;
    const lowPriority = tasks.filter(t => t.priority === 'low').length;

    updateBarChart('priorityChart', {
        'Alta': highPriority,
        'Média': mediumPriority,
        'Baixa': lowPriority
    }, total);
}

function updateBarChart(chartId, data, total) {
    const chart = document.getElementById(chartId);
    const bars = chart.querySelectorAll('.chart-bar');

    bars.forEach((bar, index) => {
        const label = bar.querySelector('.bar-label').textContent;
        const value = data[label] || 0;
        const percentage = total > 0 ? (value / total) * 100 : 0;

        const barFill = bar.querySelector('.bar-fill');
        const barValue = bar.querySelector('.bar-value');

        barFill.style.width = percentage + '%';
        barValue.textContent = value;
    });
}

// Linha do Tempo
function renderTimeline() {
    const today = new Date();
    today.setHours(0, 0, 0, 0);

    const todayEnd = new Date(today);
    todayEnd.setDate(todayEnd.getDate() + 1);

    const weekEnd = new Date(today);
    weekEnd.setDate(weekEnd.getDate() + 7);

    const nextWeekEnd = new Date(today);
    nextWeekEnd.setDate(nextWeekEnd.getDate() + 14);

    // Categorizar tarefas
    const overdueTasks = [];
    const todayTasks = [];
    const weekTasks = [];
    const nextWeekTasks = [];
    const laterTasks = [];
    const noDateTasks = [];

    tasks.forEach(task => {
        if (!task.dueDate) {
            noDateTasks.push(task);
        } else {
            const dueDate = new Date(task.dueDate + TIME_MIDNIGHT);
            dueDate.setHours(0, 0, 0, 0);

            if (dueDate < today && task.status !== 'completed') {
                overdueTasks.push(task);
            } else if (dueDate.getTime() === today.getTime()) {
                todayTasks.push(task);
            } else if (dueDate > today && dueDate < weekEnd) {
                weekTasks.push(task);
            } else if (dueDate >= weekEnd && dueDate < nextWeekEnd) {
                nextWeekTasks.push(task);
            } else {
                laterTasks.push(task);
            }
        }
    });

    // Renderizar cada seção
    renderTimelineSection('overdue-timeline', overdueTasks, true);
    renderTimelineSection('today-timeline', todayTasks, false);
    renderTimelineSection('week-timeline', weekTasks, false);
    renderTimelineSection('next-week-timeline', nextWeekTasks, false);
    renderTimelineSection('later-timeline', laterTasks, false);
    renderTimelineSection('no-date-timeline', noDateTasks, false);

    // Ocultar seções vazias
    hideEmptyTimelineSections();
}

function renderTimelineSection(containerId, tasks, isOverdue) {
    const container = document.getElementById(containerId);
    container.innerHTML = '';

    if (tasks.length === 0) {
        container.innerHTML = '<div class="timeline-empty">Nenhuma tarefa</div>';
        return;
    }

    // Ordenar por data
    tasks.sort((a, b) => {
        if (!a.dueDate) return 1;
        if (!b.dueDate) return -1;
        return new Date(a.dueDate) - new Date(b.dueDate);
    });

    tasks.forEach(task => {
        const taskElement = createTimelineTask(task, isOverdue);
        container.appendChild(taskElement);
    });
}

function createTimelineTask(task, isOverdue) {
    const div = document.createElement('div');
    div.className = `timeline-task priority-${task.priority}`;
    if (isOverdue) {
        div.classList.add('overdue');
    }

    const dueDateHtml = task.dueDate ? `
        <span class="task-badge">📅 ${formatDate(task.dueDate)}</span>
    ` : '';

    const categoryHtml = task.category ? `
        <span class="task-badge category-badge">${escapeHtml(task.category)}</span>
    ` : '';

    const statusLabels = {
        'pending': '📝 Pendente',
        'in-progress': '🔄 Em Progresso',
        'completed': '✅ Concluída'
    };

    div.innerHTML = `
        <div class="timeline-task-content">
            <div class="timeline-task-title">${escapeHtml(task.title)}</div>
            ${task.description ? `<div class="task-description">${escapeHtml(task.description)}</div>` : ''}
            <div class="timeline-task-meta">
                <span class="task-badge priority-badge ${task.priority}">
                    ${getPriorityLabel(task.priority)}
                </span>
                <span class="task-badge">${statusLabels[task.status]}</span>
                ${categoryHtml}
                ${dueDateHtml}
                ${isOverdue ? '<span class="task-badge" style="background: var(--danger-color); color: white;">⚠️ Atrasada</span>' : ''}
            </div>
        </div>
        <div class="task-actions">
            <button class="task-btn" onclick="openEditTaskModal('${task.id}')" title="Editar">✏️</button>
            <button class="task-btn" onclick="deleteTask('${task.id}')" title="Excluir">🗑️</button>
        </div>
    `;

    return div;
}

function hideEmptyTimelineSections() {
    const sections = [
        'overdue-section',
        'today-section',
        'week-section',
        'next-week-section',
        'later-section',
        'no-date-section'
    ];

    sections.forEach(sectionId => {
        const section = document.getElementById(sectionId);
        const container = section.querySelector('.timeline-tasks');
        
        if (container.innerHTML.includes('Nenhuma tarefa')) {
            section.style.display = 'none';
        } else {
            section.style.display = 'block';
        }
    });
}

