"""
Funções Utilitárias para Otimização de Portfólio
=================================================
Funções auxiliares usadas em toda a aplicação.
"""

from typing import List
from src.models import Project


def calculate_hours_used(projects: List[Project], selected_names: List[str]) -> int:
    """
    Calcula o total de horas usadas pelos projetos selecionados.
    
    Args:
        projects: Lista de todos os projetos disponíveis
        selected_names: Lista de nomes dos projetos selecionados
        
    Retorna:
        Total de horas usadas pelos projetos selecionados
    """
    total = 0
    for proj in projects:
        if proj.name in selected_names:
            total += proj.hours
    return total


def reconstruct_selected_projects(projects: List[Project], selected_indices: List[int]) -> List[str]:
    """
    Converte índices de projetos em nomes de projetos.
    
    Args:
        projects: Lista de todos os projetos disponíveis
        selected_indices: Lista de índices dos projetos selecionados
        
    Retorna:
        Lista de nomes dos projetos selecionados
    """
    return [projects[i].name for i in selected_indices if i < len(projects)]
