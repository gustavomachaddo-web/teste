# 📋 Agenda de Atividades - Planner

Uma aplicação web moderna e intuitiva para gerenciamento de atividades e tarefas, inspirada no Microsoft Planner.

## 🌟 Funcionalidades

### Visualizações
- 📊 **Visualização em Quadro**: Quadro Kanban com tarefas organizadas por status
- 📈 **Análise e Dashboard**: Estatísticas detalhadas e gráficos de produtividade
- 📅 **Linha do Tempo**: Visualização cronológica de tarefas por período

### Gerenciamento de Tarefas
- ✅ **Criação de Atividades**: Adicione novas tarefas com título, descrição, data de vencimento, prioridade e categoria
- 📊 **Organização por Status**: Visualize tarefas organizadas em colunas (Pendente, Em Progresso, Concluída)
- 🎯 **Níveis de Prioridade**: Defina prioridades (Alta, Média, Baixa) para suas atividades
- 🏷️ **Categorização**: Organize tarefas por categorias personalizadas (Trabalho, Pessoal, Estudos, etc.)
- 📅 **Datas de Vencimento**: Acompanhe prazos e visualize tarefas atrasadas
- 🔍 **Filtros Avançados**: Filtre tarefas por prioridade e status
- ✏️ **Edição e Exclusão**: Edite ou remova atividades facilmente

### Análise e Produtividade
- 📊 **Dashboard de Estatísticas**: Visualize métricas como total de tarefas, concluídas, pendentes e atrasadas
- 📈 **Gráficos de Distribuição**: Gráficos de barras para status e prioridades
- 💯 **Taxa de Conclusão**: Acompanhe sua produtividade em tempo real
- ⚠️ **Alertas de Tarefas Atrasadas**: Identifique rapidamente tarefas que passaram do prazo

### Recursos Técnicos
- 💾 **Persistência Local**: Seus dados são salvos automaticamente no navegador
- 📱 **Design Responsivo**: Interface adaptável para desktop, tablet e mobile
- 🎨 **Interface Moderna**: Design limpo e profissional com animações suaves

## 🚀 Como Usar

### Instalação

Não é necessária instalação! Basta abrir o arquivo `index.html` em seu navegador.

### Navegação

A aplicação possui três visualizações principais acessíveis através dos botões no topo:

1. **📊 Quadro** - Visualização Kanban tradicional
2. **📈 Análise** - Dashboard com estatísticas e gráficos
3. **📅 Linha do Tempo** - Visualização cronológica

### Utilização

#### Adicionar uma Atividade
1. Clique no botão "+ Nova Atividade"
2. Preencha os campos obrigatórios (título, prioridade, status)
3. Adicione informações opcionais (descrição, data, categoria)
4. Clique em "Salvar"

#### Visualização em Quadro
- As atividades são organizadas em três colunas por status
- Cada card mostra título, descrição, prioridade e data de vencimento
- Contadores no topo de cada coluna mostram o número de tarefas
- Use os filtros para visualizar tarefas específicas por prioridade ou status

#### Visualização de Análise
- Acesse estatísticas gerais: total de tarefas, concluídas, em progresso, pendentes e atrasadas
- Visualize a taxa de conclusão para acompanhar sua produtividade
- Analise gráficos de distribuição por status e prioridade
- Identifique rapidamente áreas que precisam de atenção

#### Visualização de Linha do Tempo
- Tarefas organizadas cronologicamente por período:
  - ⚠️ **Atrasadas**: Tarefas que passaram do prazo
  - 📅 **Hoje**: Tarefas com vencimento hoje
  - 📆 **Esta Semana**: Tarefas dos próximos 7 dias
  - 🗓️ **Próxima Semana**: Tarefas da semana seguinte
  - 📋 **Mais Tarde**: Tarefas futuras
  - 📭 **Sem Data Definida**: Tarefas sem prazo

#### Editar uma Atividade
- Clique no ícone de lápis (✏️) no card da tarefa
- Modifique os campos desejados
- Clique em "Salvar"

#### Excluir uma Atividade
- Clique no ícone de lixeira (🗑️) no card da tarefa
- Confirme a exclusão

#### Filtrar Atividades (na visualização Quadro)
- Use os filtros na barra superior para visualizar:
  - Todas as prioridades ou uma específica (Alta, Média, Baixa)
  - Todos os status ou um específico (Pendente, Em Progresso, Concluída)

## 📂 Estrutura do Projeto

```
project-root/
├── index.html      # Estrutura HTML da aplicação
├── styles.css      # Estilos e design visual
├── script.js       # Lógica e funcionalidades JavaScript
└── README.md       # Documentação do projeto
```

## 🎨 Tecnologias Utilizadas

- **HTML5**: Estrutura semântica da aplicação
- **CSS3**: Estilização moderna com variáveis CSS e animações
- **JavaScript (ES6+)**: Lógica de negócio e manipulação do DOM
- **LocalStorage API**: Persistência de dados no navegador

## 💡 Características Técnicas

### Gerenciamento de Estado
- Estado centralizado com array de tarefas
- Sincronização automática com LocalStorage
- Identificadores únicos para cada tarefa

### Interface do Usuário
- Design inspirado no Fluent Design System (Microsoft)
- Responsivo com Grid CSS e Flexbox
- Animações suaves para melhor experiência
- Feedback visual com notificações

### Funcionalidades Avançadas
- Validação de formulários
- Detecção de tarefas atrasadas
- Escape de HTML para segurança
- Modal reutilizável para adicionar/editar
- Filtros em tempo real

## 🔒 Segurança

- Escape de HTML para prevenir XSS
- Validação de campos obrigatórios
- Confirmação antes de exclusões

## 🌐 Compatibilidade

Compatível com navegadores modernos:
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Opera 76+

## 📱 Responsividade

A aplicação é totalmente responsiva e se adapta a diferentes tamanhos de tela:
- **Desktop**: Layout em 3 colunas
- **Tablet**: Layout adaptável
- **Mobile**: Layout em coluna única

## 🎯 Casos de Uso

- **Gerenciamento de Projetos**: Organize tarefas de projetos pessoais ou profissionais
- **Planejamento Diário**: Planeje suas atividades diárias
- **Acompanhamento de Estudos**: Gerencie tarefas acadêmicas
- **Organização Pessoal**: Mantenha sua vida organizada

## 🔄 Próximas Melhorias (Roadmap)

- [ ] Integração com Microsoft Planner API
- [ ] Drag and drop para mover tarefas entre colunas
- [ ] Modo escuro
- [ ] Exportar/importar dados
- [ ] Notificações de prazo
- [ ] Filtros por data
- [ ] Busca de atividades
- [ ] Subtarefas
- [ ] Anexos de arquivos
- [ ] Compartilhamento de tarefas

## 📝 Licença

Este projeto é de código aberto e está disponível para uso livre.

## 👨‍💻 Desenvolvimento

Para contribuir com o projeto:

1. Clone o repositório
2. Faça suas modificações
3. Teste localmente abrindo `index.html` no navegador
4. Envie suas melhorias

## 📞 Suporte

Para dúvidas ou sugestões, abra uma issue no repositório do projeto.

---

Desenvolvido com ❤️ para facilitar o gerenciamento de atividades
