// Estado da aplicação
let tasks = [];
let editingTaskId = null;

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
    renderTasks();
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
    renderTasks();
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
        renderTasks();
        showNotification('Atividade atualizada com sucesso!', 'success');
    }
}

// Deletar tarefa
function deleteTask(taskId) {
    if (confirm('Tem certeza que deseja excluir esta atividade?')) {
        tasks = tasks.filter(t => t.id !== taskId);
        saveTasks();
        renderTasks();
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
