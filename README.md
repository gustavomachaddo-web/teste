# 📋 Agenda de Atividades - Planner

Uma aplicação web moderna e intuitiva para gerenciamento de atividades e tarefas, inspirada no Microsoft Planner.

## 🌟 Funcionalidades

- ✅ **Criação de Atividades**: Adicione novas tarefas com título, descrição, data de vencimento, prioridade e categoria
- 📊 **Organização por Status**: Visualize tarefas organizadas em colunas (Pendente, Em Progresso, Concluída)
- 🎯 **Níveis de Prioridade**: Defina prioridades (Alta, Média, Baixa) para suas atividades
- 🏷️ **Categorização**: Organize tarefas por categorias personalizadas (Trabalho, Pessoal, Estudos, etc.)
- 📅 **Datas de Vencimento**: Acompanhe prazos e visualize tarefas atrasadas
- 🔍 **Filtros Avançados**: Filtre tarefas por prioridade e status
- ✏️ **Edição e Exclusão**: Edite ou remova atividades facilmente
- 💾 **Persistência Local**: Seus dados são salvos automaticamente no navegador
- 📱 **Design Responsivo**: Interface adaptável para desktop, tablet e mobile
- 🎨 **Interface Moderna**: Design limpo e profissional com animações suaves

## 🚀 Como Usar

### Instalação

Não é necessária instalação! Basta abrir o arquivo `index.html` em seu navegador.

### Utilização

1. **Adicionar uma Atividade**
   - Clique no botão "+ Nova Atividade"
   - Preencha os campos obrigatórios (título, prioridade, status)
   - Adicione informações opcionais (descrição, data, categoria)
   - Clique em "Salvar"

2. **Visualizar Atividades**
   - As atividades são organizadas em três colunas por status
   - Cada card mostra título, descrição, prioridade e data de vencimento
   - Contadores no topo de cada coluna mostram o número de tarefas

3. **Editar uma Atividade**
   - Clique no ícone de lápis (✏️) no card da tarefa
   - Modifique os campos desejados
   - Clique em "Salvar"

4. **Excluir uma Atividade**
   - Clique no ícone de lixeira (🗑️) no card da tarefa
   - Confirme a exclusão

5. **Filtrar Atividades**
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
