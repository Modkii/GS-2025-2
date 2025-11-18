
## 📋 Descrição do Projeto

Este projeto implementa uma solução completa para o **Problema da Mochila 0/1** aplicado à otimização de portfólio de projetos. Uma empresa de consultoria precisa selecionar projetos maximizando o valor estratégico dentro de um limite de horas-especialista disponíveis.

O sistema demonstra **quatro abordagens algorítmicas** distintas, comparando suas eficiências, complexidades e resultados:

1. **Estratégia Gulosa** - Rápida mas não garante solução ótima
2. **Recursão Pura** - Explora todas as combinações (exponencial)
3. **Programação Dinâmica Top-Down** - Solução ótima com memoização
4. **Programação Dinâmica Bottom-Up** - Solução ótima iterativa (mais eficiente)

---

## 👥 Integrantes

| Nome Completo | RM 
|--------------|---------|-------|-------|
| Gabriel Matias Simões    | RM 556171 
| Leonardo Rocha Scarpitta | RM 555460
| Murilo Justi Rodrigues   | RM 554512
```
╔══════════════════════════════════════════════════════════╗
║  Nome Completo | RM                                      ║
║                                                          ║
║  Gabriel Matias Simões    | RM 556171                    ║
║  Leonardo Rocha Scarpitta | RM 555460                    ║
║  Murilo Justi Rodrigues   | RM 554512                    ║
╚══════════════════════════════════════════════════════════╝
```

---

## 🎓 Informações Acadêmicas

```
╔══════════════════════════════════════════════════════════╗
║  Instituição:  FIAP - Faculdade de Informática e         ║
║                Administração Paulista                    ║
║  Curso:        Engenharia de Software                    ║
║  Disciplina:   Programação Dinâmica                      ║
║  Professor:    Marcelo Amorim                            ║
║  Semestre:     4º Semestre                               ║
║  Tema:         O Futuro do Trabalho                      ║
╚══════════════════════════════════════════════════════════╝
```

---

## 🎯 Descrição do Problema

### Problema da Mochila 0/1 Aplicado a Projetos

Uma empresa de consultoria possui **N projetos** disponíveis, cada um com:
- **Valor estratégico** (importância/lucro do projeto)
- **Horas-especialista** necessárias para execução

A empresa tem uma **capacidade limitada** de horas-especialista disponíveis.

**Objetivo:** Selecionar um subconjunto de projetos que **maximize o valor total**, respeitando o limite de capacidade.

**Restrição:** Cada projeto pode ser selecionado **0 ou 1 vez** (não pode ser parcialmente executado).

### Exemplo Ilustrativo

```
Capacidade: 10 horas-especialista

Projetos Disponíveis:
┌─────────┬───────┬───────┬────────────┐
│ Projeto │ Valor │ Horas │ Eficiência │
├─────────┼───────┼───────┼────────────┤
│    A    │  12   │   4   │    3.00    │
│    B    │  10   │   3   │    3.33    │
│    C    │   7   │   2   │    3.50    │
│    D    │   4   │   3   │    1.33    │
└─────────┴───────┴───────┴────────────┘

Solução Ótima: Projetos A + B + C = 29 (9 horas usadas)
```

---

## 🔹 As 4 Fases do Algoritmo

### Fase 1: Estratégia Gulosa 🟡

```
Complexidade: O(n log n)
Status: NÃO garante solução ótima
```

**Como funciona:** Ordena projetos por eficiência (valor/hora) e seleciona gulossamente até esgotar capacidade.

**Vantagem:** Muito rápida
**Desvantagem:** Pode falhar - demonstrado no Caso de Teste 2

---

### Fase 2: Solução Recursiva Pura 🔴

```
Complexidade: O(2^n)
Status: Ótima mas IMPRATICÁVEL para n > 25
```

**Como funciona:** Explora recursivamente todas as 2^n combinações possíveis de projetos.

**Vantagem:** Encontra solução ótima, fácil de entender
**Desvantagem:** Tempo exponencial - recalcula subproblemas múltiplas vezes

---

### Fase 3: Programação Dinâmica com Memoização (Top-Down) 🟢

```
Complexidade: O(n × capacidade)
Status: Ótima e EFICIENTE
```

**Como funciona:** Mesma lógica recursiva da Fase 2, mas armazena resultados de subproblemas em cache (memo).

**Vantagem:** Solução ótima em tempo polinomial
**Desvantagem:** Usa recursão (limites de pilha) e consome memória

---

### Fase 4: Programação Dinâmica Bottom-Up (Iterativa) ⭐

```
Complexidade: O(n × capacidade)
Status: Ótima e MAIS EFICIENTE
```

**Como funciona:** Constrói iterativamente uma tabela DP preenchendo de baixo para cima.

**Vantagem:** Solução ótima, sem recursão, melhor localidade de cache
**Desvantagem:** Nenhuma - esta é a abordagem recomendada para produção

---

## 📁 Estrutura do Projeto

```
GS/
│
├── main.py                      # Ponto de entrada da aplicação
│
├── src/                         # Código-fonte principal
│   ├── __init__.py             # Inicialização do pacote
│   ├── models.py               # Classe Project (dataclass)
│   ├── utils.py                # Funções auxiliares
│   ├── algorithms.py           # 4 implementações dos algoritmos
│   ├── formatter.py            # Funções de formatação PT-BR
│   ├── test_cases.py           # 5 casos de teste definidos
│   └── test_runner.py          # Orquestrador de testes
│
├── README.md                    # Este arquivo
├── DOCUMENTACAO.md             # Documentação técnica detalhada
└── ANALISE_COMPLEXIDADE.md     # Análise matemática de complexidade
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.7 ou superior
- Nenhuma dependência externa (usa apenas biblioteca padrão)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/portfolio-optimization.git
cd portfolio-optimization

# Não é necessário instalar dependências - projeto usa apenas stdlib
```

### Execução

```bash
# Execute o programa principal
python main.py
```

### Saída Esperada

O programa executará automaticamente 5 casos de teste e exibirá:

1. **Dados de Entrada** - Capacidade e projetos disponíveis
2. **Fase 1 - Estratégia Gulosa** - Resultado e complexidade
3. **Fase 2 - Recursão Pura** - Resultado e complexidade
4. **Fase 3 - Memoização** - Resultado, tamanho do memo, complexidade
5. **Fase 4 - DP Bottom-Up** - Resultado ótimo ⭐
6. **Comparação de Resultados** - Todos os algoritmos lado a lado
7. **Análise** - Detecta falha da gulosa quando aplicável
8. **Resumo Final** - Tabela comparativa e estatísticas

---

## 📊 Resumo dos Casos de Teste

| # | Nome do Teste | Descrição | Gulosa Falha? | Status |
|---|--------------|-----------|---------------|---------|
| 1 | Exemplo Padrão | 4 projetos, cap=10 | ❌ Não | ✓ Todos ótimos |
| 2 | Falha da Gulosa | Design especial para demonstrar falha | ✓ **Sim** | ⚠️ Gulosa=13, Ótimo=16 |
| 3 | Projeto Único | Caso limite com 1 projeto | ❌ Não | ✓ Todos ótimos |
| 4 | Todos Excedem | Nenhum projeto cabe | ❌ Não | ✓ Todos=0 |
| 5 | Escala Maior | 8 projetos, cap=15 | ❌ Não | ✓ Todos ótimos |

**Taxa de Sucesso DP:** 100% (sempre encontra solução ótima)
**Taxa de Falha Gulosa:** 20% (1 de 5 testes)

---

## 📝 Conceitos Abordados

### Algoritmos e Estruturas de Dados
- ✅ Problema da Mochila 0/1 (0/1 Knapsack Problem)
- ✅ Algoritmos Gulosos (Greedy Algorithms)
- ✅ Recursão e Árvores de Recursão
- ✅ Memoização (Caching de Subproblemas)
- ✅ Programação Dinâmica (Dynamic Programming)
- ✅ Backtracking (Reconstrução de Solução)

### Análise de Complexidade
- ✅ Notação Big-O
- ✅ Complexidade de Tempo
- ✅ Complexidade de Espaço
- ✅ Comparação de Algoritmos

### Boas Práticas de Engenharia
- ✅ Separação de Responsabilidades (SRP)
- ✅ Código Modular e Reutilizável
- ✅ Type Hints (Python 3.7+)
- ✅ Docstrings Completas
- ✅ Estrutura de Testes Organizada

---

## 📋 Critérios de Avaliação

| Critério | Peso | Descrição |
|----------|------|-----------|
| **Correção do Algoritmo** | 50% | Implementação correta das 4 abordagens, solução ótima encontrada |
| **Memoização/Tabela** | 20% | Uso adequado de memoização (Fase 3) e tabela DP (Fase 4) |
| **Demonstração de Falha** | 15% | Caso de teste que demonstra falha da estratégia gulosa |
| **Documentação** | 15% | Clareza e organização da documentação (README, código) |

---

## 📚 Referências Bibliográficas

1. **CORMEN, T. H. et al.** *Introduction to Algorithms*, 3rd Edition. MIT Press, 2009.
   - Capítulo 15: Dynamic Programming
   - Seção 15.2: Matrix-chain multiplication
   - Seção 16.2: Elements of the greedy strategy

2. **KLEINBERG, J.; TARDOS, É.** *Algorithm Design*. Pearson, 2005.
   - Capítulo 6: Dynamic Programming
   - Seção 6.4: Knapsack Problem

3. **SEDGEWICK, R.; WAYNE, K.** *Algorithms*, 4th Edition. Addison-Wesley, 2011.
   - Capítulo sobre Dynamic Programming

4. **Materiais do Curso**
   - Slides Prof. Marcelo Amorim - Programação Dinâmica
   - FIAP, 2º Semestre 2025

5. **Documentação Python**
   - Python 3.11 Documentation: https://docs.python.org/3/
   - PEP 8 - Style Guide for Python Code

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

```
MIT License

Copyright (c) 2025 FIAP - Equipe de Desenvolvimento

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 📌 Histórico de Versões

| Versão | Data | Descrição |
|--------|------|-----------|
| 1.0.0 | 14/11/2025 | Versão inicial completa com 4 fases implementadas |
| 1.1.0 | 14/11/2025 | Refatoração para estrutura modular (src/ e tests/) |
| 1.2.0 | 14/11/2025 | Consolidação em src/ único, tradução completa PT-BR |

---

## 🔧 Suporte e Contato

Para dúvidas ou sugestões sobre o projeto:

- **Issues:** Abra uma issue no repositório GitHub
- **Email:** Consulte a seção "Equipe de Desenvolvimento"
- **Professor:** Marcelo Amorim - [email do professor]

---

## ⚡ Quick Start

```bash
# Execução rápida
python main.py

# Verificar versão Python
python --version  # Deve ser >= 3.7

# Estrutura mínima
GS/
├── main.py
└── src/
    ├── models.py
    ├── algorithms.py
    ├── formatter.py
    ├── utils.py
    ├── test_cases.py
    └── test_runner.py
```

---

**Última atualização:** 14 de Novembro de 2025

**Desenvolvido com 💙 para FIAP - Programação Dinâmica**

---

## 🎯 Observações Importantes

1. ✅ **Todos os algoritmos estão implementados e funcionando**
2. ✅ **5 casos de teste abrangentes incluídos**
3. ✅ **Falha da estratégia gulosa demonstrada no Caso 2**
4. ✅ **Documentação completa em Português-BR**
5. ✅ **Código segue PEP 8 e boas práticas**
6. ✅ **Complexidades analisadas detalhadamente**

---

