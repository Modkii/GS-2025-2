#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Otimização de Portfólio - Programação Dinâmica
===============================================

Este programa demonstra quatro abordagens para resolver o Problema da Mochila 0/1:
1. Estratégia Gulosa (não-ótima)
2. Solução Recursiva Pura (tempo exponencial)
3. PD Top-Down com Memoização (ótima, recursiva)
4. PD Bottom-Up (ótima, iterativa - mais eficiente)

Uso:
    python main.py
"""

import sys
import io

# Force UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from src.formatter import print_welcome, print_footer
from src.test_runner import run_all_tests
from src.test_cases import ALL_TEST_CASES


def main():
    """
    Função principal de execução.
    
    Fluxo:
        1. Exibe mensagem de boas-vindas
        2. Executa todos os casos de teste
        3. Exibe rodapé
    """
    # Display welcome header
    print_welcome()
    
    # Execute all test cases and collect results
    results = run_all_tests(ALL_TEST_CASES)
    
    # Display footer
    print_footer()


if __name__ == "__main__":
    main()
