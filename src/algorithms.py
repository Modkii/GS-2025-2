"""
Algoritmos de Otimização de Portfólio
======================================
Implementa quatro abordagens para resolver o Problema da Mochila 0/1:
1. Estratégia Gulosa (não-ótima)
2. Solução Recursiva Pura (tempo exponencial)
3. PD Top-Down com Memoização (ótima, recursiva)
4. PD Bottom-Up (ótima, iterativa - mais eficiente)
"""

from typing import List, Dict, Tuple
from src.models import Project


# ===== FASE 1: ESTRATÉGIA GULOSA =====

def greedy_portfolio(projects: List[Project], capacity: int) -> Tuple[int, List[str]]:
    """
    Abordagem gulosa: Seleciona projetos pela maior razão valor/horas.
    
    IMPORTANTE: Esta abordagem NÃO garante solução ótima.
    Serve para demonstrar que heurísticas gulosas podem falhar para Mochila 0/1.
    
    Algoritmo:
        1. Ordena projetos por eficiência (valor/horas) em ordem decrescente
        2. Seleciona projetos gulossamente de forma sequencial até esgotar capacidade
        3. Retorna valor total e projetos selecionados
    
    Args:
        projects: Lista de projetos disponíveis
        capacity: Máximo de horas de especialista disponíveis
        
    Retorna:
        Tupla de (valor_total, nomes_projetos_selecionados)
        
    Complexidade de Tempo: O(n log n) devido à ordenação
    Complexidade de Espaço: O(n) para armazenar lista ordenada
    """
    # Ordena projetos por eficiência (razão valor/horas) em ordem decrescente
    sorted_projects = sorted(projects, key=lambda p: p.efficiency(), reverse=True)
    
    total_value = 0
    selected_projects = []
    remaining_capacity = capacity
    
    # Seleciona projetos gulossamente até esgotar capacidade
    for project in sorted_projects:
        if project.hours <= remaining_capacity:
            # Inclui este projeto
            selected_projects.append(project.name)
            total_value += project.value
            remaining_capacity -= project.hours
    
    return total_value, selected_projects


# ===== FASE 2: SOLUÇÃO RECURSIVA PURA =====

def recursive_portfolio(projects: List[Project], capacity: int, index: int = 0) -> int:
    """
    Solução recursiva pura explorando todas as combinações.
    
    Esta implementação deliberadamente evita memoização para demonstrar
    complexidade de tempo exponencial. Recalcula subproblemas múltiplas vezes.
    
    Relação de Recorrência:
        ValorMax(i, c) = max(
            ValorMax(i-1, c),                              # Não inclui projeto i
            projects[i].value + ValorMax(i-1, c-hours[i])  # Inclui projeto i
        )
    
    Casos Base:
        - Se index >= len(projects): sem mais projetos a considerar, retorna 0
        - Se capacity == 0: sem capacidade restante, retorna 0
        - Se hours[index] > capacity: projeto não cabe, pula ele
    
    Args:
        projects: Lista de projetos disponíveis
        capacity: Capacidade restante de horas de especialista
        index: Índice do projeto atual sendo considerado
        
    Retorna:
        Valor máximo alcançável
        
    Complexidade de Tempo: O(2^n) - exponencial (explora todas as 2^n combinações)
    Complexidade de Espaço: O(n) - profundidade da pilha de recursão
    """
    # Caso base: sem mais projetos a considerar
    if index >= len(projects):
        return 0
    
    # Caso base: sem capacidade restante
    if capacity == 0:
        return 0
    
    current_project = projects[index]
    
    # Se projeto atual não cabe, pula ele
    if current_project.hours > capacity:
        return recursive_portfolio(projects, capacity, index + 1)
    
    # Caso 1: Não inclui projeto atual
    exclude_value = recursive_portfolio(projects, capacity, index + 1)
    
    # Caso 2: Inclui projeto atual
    include_value = current_project.value + recursive_portfolio(
        projects, 
        capacity - current_project.hours, 
        index + 1
    )
    
    # Retorna máximo de ambos os casos
    return max(exclude_value, include_value)


# ===== FASE 3: PROGRAMAÇÃO DINÂMICA TOP-DOWN (MEMOIZAÇÃO) =====

def memoization_portfolio(projects: List[Project], capacity: int) -> Tuple[int, Dict]:
    """
    PD Top-down com memoização: Mesma lógica recursiva com cache.
    
    Otimiza a solução recursiva armazenando resultados de subproblemas computados.
    Quando um subproblema (índice, capacidade) é encontrado novamente, retornamos o
    resultado em cache ao invés de recalcular.
    
    Estrutura do Memo: memo[(índice, capacidade)] = valor_máximo
    
    Algoritmo:
        1. Verifica se (índice, capacidade) já foi computado no memo
        2. Se sim, retorna valor em cache
        3. Se não, computa recursivamente
        4. Armazena resultado no memo antes de retornar
    
    Args:
        projects: Lista de projetos disponíveis
        capacity: Máximo de horas de especialista disponíveis
        
    Retorna:
        Tupla de (valor_ótimo, dicionário_memo)
        
    Complexidade de Tempo: O(n * capacidade) - cada subproblema computado uma vez
    Complexidade de Espaço: O(n * capacidade) - armazenamento memo + O(n) pilha recursão
    """
    memo: Dict[Tuple[int, int], int] = {}
    
    def _memoized_helper(index: int, remaining_capacity: int) -> int:
        """Função auxiliar recursiva com memoização."""
        # Caso base: sem mais projetos
        if index >= len(projects):
            return 0
        
        # Caso base: sem capacidade
        if remaining_capacity == 0:
            return 0
        
        # Verifica memo antes de computar
        state = (index, remaining_capacity)
        if state in memo:
            return memo[state]
        
        current_project = projects[index]
        
        # Se projeto não cabe, pula ele
        if current_project.hours > remaining_capacity:
            result = _memoized_helper(index + 1, remaining_capacity)
        else:
            # Caso 1: Exclui projeto atual
            exclude_value = _memoized_helper(index + 1, remaining_capacity)
            
            # Caso 2: Inclui projeto atual
            include_value = current_project.value + _memoized_helper(
                index + 1, 
                remaining_capacity - current_project.hours
            )
            
            result = max(exclude_value, include_value)
        
        # Armazena no memo antes de retornar
        memo[state] = result
        return result
    
    optimal_value = _memoized_helper(0, capacity)
    return optimal_value, memo


# ===== FASE 4: PROGRAMAÇÃO DINÂMICA BOTTOM-UP (ITERATIVA) =====

def dynamic_programming_portfolio(projects: List[Project], capacity: int) -> Tuple[int, List[str]]:
    """
    PD Bottom-up: Constrói tabela de solução iterativamente a partir de subproblemas menores.
    
    Esta é a abordagem MAIS EFICIENTE para uso em produção.
    
    Estrutura da Tabela PD:
        T[i][c] = valor máximo alcançável usando primeiros i projetos com capacidade c
    
    Recorrência (preenchendo a tabela):
        T[i][c] = max(
            T[i-1][c],                                    # Não inclui projeto i
            projects[i-1].value + T[i-1][c-hours[i-1]]   # Inclui projeto i (se couber)
        )
    
    Inicialização:
        T[0][c] = 0 para todo c (sem projetos = valor zero)
        T[i][0] = 0 para todo i (sem capacidade = valor zero)
    
    Algoritmo de Retrocesso:
        Começando de T[n][capacidade], traça de volta para encontrar quais projetos foram incluídos:
        - Se T[i][c] != T[i-1][c]: projeto i foi incluído
        - Move para T[i-1][c - hours[i]] e repete
    
    Args:
        projects: Lista de projetos disponíveis
        capacity: Máximo de horas de especialista disponíveis
        
    Retorna:
        Tupla de (valor_ótimo, nomes_projetos_selecionados)
        
    Complexidade de Tempo: O(n * capacidade) - preenche n*capacidade células da tabela
    Complexidade de Espaço: O(n * capacidade) - armazenamento da tabela PD
    
    Vantagens sobre Memoização:
        - Sem overhead de recursão
        - Melhor localidade de cache (padrão de acesso iterativo)
        - Mais fácil otimizar espaço (pode usar array 1D)
        - Performance mais previsível
    """
    n = len(projects)
    
    # Cria tabela PD: T[i][c] representa valor máx com primeiros i projetos e capacidade c
    # Dimensões: (n+1) x (capacidade+1) para incluir casos base
    T = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Preenche a tabela PD iterativamente
    for i in range(1, n + 1):
        current_project = projects[i - 1]  # i-ésimo projeto (indexado em 0)
        
        for c in range(capacity + 1):
            # Caso 1: Não inclui projeto atual (herda linha anterior)
            exclude_value = T[i - 1][c]
            
            # Caso 2: Inclui projeto atual (se couber)
            if current_project.hours <= c:
                include_value = current_project.value + T[i - 1][c - current_project.hours]
                T[i][c] = max(exclude_value, include_value)
            else:
                # Project doesn't fit, must exclude
                T[i][c] = exclude_value
    
    # Valor ótimo está na célula inferior direita
    optimal_value = T[n][capacity]
    
    # Retroage para encontrar quais projetos foram selecionados
    selected_projects = []
    i = n
    c = capacity
    
    while i > 0 and c > 0:
        # Se valor veio de incluir projeto i, será diferente da linha acima
        if T[i][c] != T[i - 1][c]:
            # Projeto i foi incluído
            project = projects[i - 1]
            selected_projects.append(project.name)
            c -= project.hours  # Reduce capacity
        i -= 1
    
    selected_projects.reverse()  # Retroação dá ordem inversa
    
    return optimal_value, selected_projects
