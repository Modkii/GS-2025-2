"""
Modelos de Dados para Otimização de Portfólio
==============================================
Define a estrutura de dados Project e modelos relacionados.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Project:
    """
    Representa um projeto no portfólio.
    
    Atributos:
        name: Identificador do projeto
        value: Valor estratégico ou lucro do projeto
        hours: Horas de especialista necessárias para completar o projeto
    """
    name: str
    value: int
    hours: int
    
    def efficiency(self) -> float:
        """
        Calcula a razão valor/horas para seleção gulosa.
        
        Retorna:
            Float representando eficiência (valor por hora)
        """
        return self.value / self.hours if self.hours > 0 else 0
