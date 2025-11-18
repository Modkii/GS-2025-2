"""
Casos de Teste para Otimização de Portfólio
============================================
Define todos os casos de teste para o problema da Mochila 0/1.
"""

from src.models import Project


# ===== CASO DE TESTE 1: EXEMPLO PADRÃO =====
TEST_CASE_1_EXAMPLE = {
    'name': 'Exemplo Padrão',
    'capacity': 10,
    'projects': [
        Project(name='A', value=12, hours=4),
        Project(name='B', value=10, hours=3),
        Project(name='C', value=7, hours=2),
        Project(name='D', value=4, hours=3),
    ],
    'expected_greedy_fails': False,
    'case_num': 1,
}

# ===== CASO DE TESTE 2: CASO DE FALHA DA GREEDY =====
# Design: Projeto com alta eficiência mas valor médio vs
#         Projeto com menor eficiência mas alto valor que usa a capacidade restante perfeitamente
# Gulosa escolherá alta eficiência primeiro, deixando capacidade insuficiente para combinação ótima
TEST_CASE_2_GREEDY_FAILURE = {
    'name': 'Demonstração de Falha da Greedy',
    'capacity': 10,
    'projects': [
        Project(name='X', value=5, hours=2),   # Eficiência: 2.5 (gulosa escolhe este primeiro)
        Project(name='Y', value=8, hours=5),   # Eficiência: 1.6
        Project(name='Z', value=8, hours=5),   # Eficiência: 1.6
    ],
    'expected_greedy_fails': True,
    'case_num': 2,
}
# Gulosa: escolhe X (5 valor, 2 horas), depois Y (8 valor, 5 horas) = 13 total, 7 horas usadas, não cabe Z
# Ótimo: escolhe Y + Z (16 valor, 10 horas) - MELHOR!

# ===== CASO DE TESTE 3: CASO LIMITE - PROJETO ÚNICO =====
TEST_CASE_3_SINGLE_PROJECT = {
    'name': 'Projeto Único (Caso Limite)',
    'capacity': 10,
    'projects': [
        Project(name='Solo', value=15, hours=7),
    ],
    'expected_greedy_fails': False,
    'case_num': 3,
}

# ===== CASO DE TESTE 4: CASO LIMITE - TODOS OS PROJETOS EXCEDEM CAPACIDADE =====
TEST_CASE_4_ALL_EXCEED_CAPACITY = {
    'name': 'Todos os Projetos Excedem Capacidade (Caso Limite)',
    'capacity': 10,
    'projects': [
        Project(name='Heavy1', value=20, hours=15),
        Project(name='Heavy2', value=25, hours=20),
        Project(name='Heavy3', value=30, hours=18),
    ],
    'expected_greedy_fails': False,
    'case_num': 4,
}

# ===== CASO DE TESTE 5: ESCALA MAIOR =====
TEST_CASE_5_LARGE_SCALE = {
    'name': 'Escala Maior (8 projetos)',
    'capacity': 15,
    'projects': [
        Project(name=f'P{i}', value=i*3, hours=i) for i in range(1, 9)
    ],
    'expected_greedy_fails': False,
    'case_num': 5,
}

# ===== TODOS OS CASOS DE TESTE =====
ALL_TEST_CASES = [
    TEST_CASE_1_EXAMPLE,
    TEST_CASE_2_GREEDY_FAILURE,
    TEST_CASE_3_SINGLE_PROJECT,
    TEST_CASE_4_ALL_EXCEED_CAPACITY,
    TEST_CASE_5_LARGE_SCALE,
]
