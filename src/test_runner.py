"""
Executor de Testes para Otimização de Portfólio
================================================
Orquestra a execução de testes e exibição de resultados.
"""

from typing import List, Dict, Any
from src.algorithms import (
    greedy_portfolio,
    recursive_portfolio,
    memoization_portfolio,
    dynamic_programming_portfolio
)
from src.utils import calculate_hours_used
from src.formatter import (
    print_test_case_header,
    print_input_section,
    print_phase_results,
    print_comparison_section,
    print_analysis_section,
    print_summary_table,
    print_execution_stats
)


def run_test_case(test_case: Dict[str, Any]) -> Dict[str, int]:
    """
    Executa um único caso de teste através dos quatro algoritmos.
    
    Args:
        test_case: Dicionário contendo dados do caso de teste:
            - name: Nome do caso de teste
            - capacity: Capacidade de horas de especialista
            - projects: Lista de objetos Project
            - expected_greedy_fails: Se espera-se que a gulosa falhe
            - case_num: Número do caso de teste
            
    Retorna:
        Dicionário com resultados de todos os algoritmos
    """
    name = test_case['name']
    capacity = test_case['capacity']
    projects = test_case['projects']
    expected_fail = test_case['expected_greedy_fails']
    case_num = test_case['case_num']
    
    # Display test case header and input
    print_test_case_header(case_num, name)
    print_input_section(capacity, projects)
    
    # Phase 1: Greedy
    greedy_value, greedy_projects = greedy_portfolio(projects, capacity)
    greedy_hours = calculate_hours_used(projects, greedy_projects)
    greedy_results = {
        'value': greedy_value,
        'projects': greedy_projects,
        'hours_used': f"{greedy_hours}/{capacity}",
        'complexity': "O(n log n)"
    }
    print_phase_results(1, "ESTRATÉGIA GULOSA", greedy_results)
    
    # Phase 2: Pure Recursive (skip if too many projects)
    if len(projects) <= 10:
        recursive_value = recursive_portfolio(projects, capacity)
        recursive_results = {
            'value': recursive_value,
            'complexity': "O(2^n) - Exponencial"
        }
        print_phase_results(2, "SOLUÇÃO RECURSIVA PURA", recursive_results)
    else:
        recursive_value = None
        recursive_results = {'skipped': True}
        print_phase_results(2, "SOLUÇÃO RECURSIVA PURA", recursive_results)
    
    # Phase 3: Memoization
    memo_value, memo_dict = memoization_portfolio(projects, capacity)
    memo_results = {
        'value': memo_value,
        'memo_size': len(memo_dict),
        'complexity': "O(n × capacidade)"
    }
    print_phase_results(3, "PROGRAMAÇÃO DINÂMICA (Top-Down com Memoização)", memo_results)
    
    # Phase 4: Bottom-Up DP
    dp_value, dp_projects = dynamic_programming_portfolio(projects, capacity)
    dp_hours = calculate_hours_used(projects, dp_projects)
    dp_results = {
        'value': dp_value,
        'projects': dp_projects,
        'hours_used': f"{dp_hours}/{capacity}",
        'complexity': "O(n × capacidade)",
        'optimal': True
    }
    print_phase_results(4, "PROGRAMAÇÃO DINÂMICA (Bottom-Up Iterativa)", dp_results)
    
    # Comparison section
    print_comparison_section(greedy_value, recursive_value, memo_value, dp_value)
    
    # Analysis section
    print_analysis_section(greedy_value, dp_value, expected_fail)
    
    return {
        'greedy': greedy_value,
        'recursive': recursive_value,
        'memoization': memo_value,
        'dp': dp_value
    }


def run_all_tests(test_cases: List[Dict[str, Any]]) -> List[Dict[str, int]]:
    """
    Executa todos os casos de teste e exibe resumo.
    
    Args:
        test_cases: Lista de dicionários de casos de teste
        
    Retorna:
        Lista de dicionários de resultados de todos os casos de teste
    """
    all_results = []
    
    # Run each test case
    for test_case in test_cases:
        results = run_test_case(test_case)
        all_results.append(results)
    
    # Display summary
    print_summary_table()
    
    # Calculate and display statistics
    total_tests = len(all_results)
    greedy_failures = sum(1 for r in all_results if r['greedy'] < r['dp'])
    print_execution_stats(total_tests, greedy_failures)
    
    return all_results
