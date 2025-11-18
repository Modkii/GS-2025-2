# 📚 Guia de Referência de Funções

## Índice
- [main.py](#mainpy)
- [src/models.py](#srcmodelspy)
- [src/algorithms.py](#srcalgorithmspy)
- [src/utils.py](#srcutilspy)
- [src/formatter.py](#srcformatterpy)
- [src/test_cases.py](#srctest_casespy)
- [src/test_runner.py](#srctest_runnerpy)

---

## main.py

### `main()`
```python
def main()
```
**Descrição:** Função principal que orquestra a execução do programa.

**Fluxo:**
1. Exibe cabeçalho de boas-vindas
2. Executa todos os casos de teste
3. Exibe rodapé de finalização

**Parâmetros:** Nenhum

**Retorna:** Nenhum

**Uso:**
```python
if __name__ == "__main__":
    main()
```

---

## src/models.py

### Classe `Project`
```python
@dataclass
class Project:
    name: str
    value: int
    hours: int
```
**Descrição:** Representa um projeto com nome, valor estratégico e horas necessárias.

**Atributos:**
- `name` (str): Identificador único do projeto
- `value` (int): Valor estratégico ou lucro do projeto
- `hours` (int): Horas-especialista necessárias

---

### `Project.efficiency()`
```python
def efficiency(self) -> float
```
**Descrição:** Calcula a eficiência do projeto (razão valor/horas).

**Parâmetros:** Nenhum (método da instância)

**Retorna:** `float` - Razão valor/horas. Retorna 0 se horas == 0.

**Exemplo:**
```python
projeto = Project(name="Site", value=12, hours=4)
print(projeto.efficiency())  # 3.0
```

---

## src/algorithms.py

### `greedy_portfolio()`
```python
def greedy_portfolio(projects: List[Project], capacity: int) -> Tuple[int, List[str]]
```
**Descrição:** Implementa estratégia gulosa que seleciona projetos por ordem decrescente de eficiência.

**Algoritmo:**
1. Ordena projetos por eficiência (valor/horas) decrescente
2. Seleciona projetos sequencialmente enquanto couberem na capacidade
3. Retorna valor total e lista de projetos selecionados

**Parâmetros:**
- `projects` (List[Project]): Lista de projetos disponíveis
- `capacity` (int): Capacidade total de horas disponíveis

**Retorna:** 
- `Tuple[int, List[str]]`: (valor_total, lista_de_nomes_projetos)

**Complexidade:**
- Tempo: O(n log n)
- Espaço: O(n)

**Limitações:** ⚠️ NÃO garante solução ótima

**Exemplo:**
```python
projetos = [
    Project("A", 12, 4),
    Project("B", 10, 3),
]
valor, selecionados = greedy_portfolio(projetos, 10)
# valor = 22, selecionados = ['B', 'A']
```

---

### `recursive_portfolio()`
```python
def recursive_portfolio(projects: List[Project], capacity: int, index: int = 0) -> int
```
**Descrição:** Solução recursiva pura que explora todas as combinações possíveis.

**Algoritmo:**
- **Caso base:** Se não há projetos ou capacidade, retorna 0
- **Recursão:** Para cada projeto, calcula:
  - Valor excluindo o projeto
  - Valor incluindo o projeto (se couber)
  - Retorna o máximo dos dois

**Parâmetros:**
- `projects` (List[Project]): Lista de projetos disponíveis
- `capacity` (int): Capacidade restante de horas
- `index` (int, opcional): Índice do projeto atual (padrão: 0)

**Retorna:** `int` - Valor máximo alcançável

**Complexidade:**
- Tempo: O(2^n) - exponencial
- Espaço: O(n) - profundidade da pilha

**Limitações:** ⚠️ Muito lento para n > 25. Apenas fins educacionais.

**Exemplo:**
```python
projetos = [Project("A", 12, 4), Project("B", 10, 3)]
valor_max = recursive_portfolio(projetos, 10)
# valor_max = 22
```

---

### `memoization_portfolio()`
```python
def memoization_portfolio(projects: List[Project], capacity: int) -> Tuple[int, Dict]
```
**Descrição:** Programação Dinâmica Top-Down com cache (memoização) para evitar recálculos.

**Algoritmo:**
1. Cria dicionário `memo` para armazenar resultados
2. Para cada estado (índice, capacidade):
   - Verifica se já foi calculado
   - Se sim, retorna do cache
   - Se não, calcula recursivamente e armazena
3. Reconstrói solução e retorna valor ótimo

**Parâmetros:**
- `projects` (List[Project]): Lista de projetos disponíveis
- `capacity` (int): Capacidade total de horas disponíveis

**Retorna:** 
- `Tuple[int, Dict]`: (valor_ótimo, dicionário_memo)

**Complexidade:**
- Tempo: O(n × capacidade)
- Espaço: O(n × capacidade)

**Vantagens:** ✅ Garante solução ótima, muito mais rápido que recursão pura

**Exemplo:**
```python
projetos = [Project("A", 12, 4), Project("B", 10, 3)]
valor_otimo, memo = memoization_portfolio(projetos, 10)
# valor_otimo = 22, memo = {(0,10): 22, (1,7): 10, ...}
```

---

### `dynamic_programming_portfolio()`
```python
def dynamic_programming_portfolio(projects: List[Project], capacity: int) -> Tuple[int, List[str]]
```
**Descrição:** Programação Dinâmica Bottom-Up (iterativa) - abordagem mais eficiente.

**Algoritmo:**
1. Cria tabela T[n+1][capacidade+1] inicializada com zeros
2. Preenche tabela iterativamente:
   - T[i][c] = max(não incluir projeto i, incluir projeto i)
3. Valor ótimo fica em T[n][capacidade]
4. Faz backtracking para reconstruir projetos selecionados

**Parâmetros:**
- `projects` (List[Project]): Lista de projetos disponíveis
- `capacity` (int): Capacidade total de horas disponíveis

**Retorna:** 
- `Tuple[int, List[str]]`: (valor_ótimo, lista_de_nomes_projetos)

**Complexidade:**
- Tempo: O(n × capacidade)
- Espaço: O(n × capacidade)

**Vantagens:** 
- ✅ Garante solução ótima
- ✅ Sem overhead de recursão
- ✅ Melhor cache locality
- ⭐ **RECOMENDADO PARA PRODUÇÃO**

**Exemplo:**
```python
projetos = [Project("A", 12, 4), Project("B", 10, 3)]
valor_otimo, selecionados = dynamic_programming_portfolio(projetos, 10)
# valor_otimo = 22, selecionados = ['A', 'B']
```

---

## src/utils.py

### `calculate_hours_used()`
```python
def calculate_hours_used(projects: List[Project], selected_names: List[str]) -> int
```
**Descrição:** Calcula o total de horas necessárias para os projetos selecionados.

**Parâmetros:**
- `projects` (List[Project]): Lista completa de projetos
- `selected_names` (List[str]): Lista de nomes dos projetos selecionados

**Retorna:** `int` - Total de horas necessárias

**Exemplo:**
```python
projetos = [
    Project("A", 12, 4),
    Project("B", 10, 3),
]
horas = calculate_hours_used(projetos, ["A", "B"])
# horas = 7
```

---

### `reconstruct_selected_projects()`
```python
def reconstruct_selected_projects(projects: List[Project], selected_indices: List[int]) -> List[str]
```
**Descrição:** Converte lista de índices em lista de nomes de projetos.

**Parâmetros:**
- `projects` (List[Project]): Lista original de projetos
- `selected_indices` (List[int]): Índices dos projetos selecionados

**Retorna:** `List[str]` - Lista de nomes dos projetos

**Exemplo:**
```python
projetos = [
    Project("A", 12, 4),
    Project("B", 10, 3),
    Project("C", 7, 2),
]
nomes = reconstruct_selected_projects(projetos, [0, 2])
# nomes = ['A', 'C']
```

---

## src/formatter.py

### `print_header()`
```python
def print_header(title: str, style: str = "double") -> None
```
**Descrição:** Imprime cabeçalho formatado com caracteres box-drawing Unicode.

**Parâmetros:**
- `title` (str): Texto do cabeçalho
- `style` (str, opcional): "double" (═) ou "single" (─). Padrão: "double"

**Retorna:** Nenhum (imprime diretamente)

**Exemplo:**
```python
print_header("MEU TÍTULO")
# ╔══════════════════════════════════════════════════════════════════╗
# ║                           MEU TÍTULO                             ║
# ╚══════════════════════════════════════════════════════════════════╝
```

---

### `print_section()`
```python
def print_section(title: str, icon: str = "🔹") -> None
```
**Descrição:** Imprime cabeçalho de subseção com ícone emoji.

**Parâmetros:**
- `title` (str): Título da seção
- `icon` (str, opcional): Emoji ou ícone. Padrão: "🔹"

**Retorna:** Nenhum

**Exemplo:**
```python
print_section("DADOS DE ENTRADA", "📊")
# 📊 DADOS DE ENTRADA:
```

---

### `print_result()`
```python
def print_result(label: str, value, suffix: str = "", indent: int = 2, 
                 marker: str = "├─", optimal: bool = False) -> None
```
**Descrição:** Imprime linha de resultado formatada com indentação e marcadores.

**Parâmetros:**
- `label` (str): Rótulo do resultado
- `value`: Valor a ser exibido
- `suffix` (str, opcional): Texto adicional após o valor
- `indent` (int, opcional): Nível de indentação. Padrão: 2
- `marker` (str, opcional): Marcador de árvore. Padrão: "├─"
- `optimal` (bool, opcional): Se True, adiciona "⭐ ÓTIMO". Padrão: False

**Retorna:** Nenhum

**Exemplo:**
```python
print_result("Valor Total", 29, indent=2, marker="├─", optimal=True)
#   ├─ Valor Total: 29 ⭐ ÓTIMO
```

---

### `print_algorithm_phase()`
```python
def print_algorithm_phase(phase_num: int, phase_name: str) -> None
```
**Descrição:** Imprime cabeçalho de fase do algoritmo.

**Parâmetros:**
- `phase_num` (int): Número da fase (1-4)
- `phase_name` (str): Nome da fase

**Retorna:** Nenhum

**Exemplo:**
```python
print_algorithm_phase(1, "ESTRATÉGIA GULOSA")
# 🔹 FASE 1 - ESTRATÉGIA GULOSA:
```

---

### `print_welcome()`
```python
def print_welcome() -> None
```
**Descrição:** Exibe cabeçalho de boas-vindas com informações do projeto.

**Parâmetros:** Nenhum

**Retorna:** Nenhum

**Saída:**
```
╔══════════════════════════════════════════════════════════════════╗
║      OTIMIZAÇÃO DE PORTFÓLIO - PROGRAMAÇÃO DINÂMICA             ║
╚══════════════════════════════════════════════════════════════════╝

📌 Resolução do Problema da Mochila 0/1 para Seleção de Projetos
📚 FIAP - Curso de Programação Dinâmica
📅 Data: 14 de Novembro de 2025
```

---

### `print_test_case_header()`
```python
def print_test_case_header(case_num: int, name: str) -> None
```
**Descrição:** Imprime cabeçalho de caso de teste.

**Parâmetros:**
- `case_num` (int): Número do caso de teste
- `name` (str): Nome descritivo do teste

**Retorna:** Nenhum

---

### `print_input_section()`
```python
def print_input_section(capacity: int, projects: List[Project]) -> None
```
**Descrição:** Exibe dados de entrada do caso de teste (capacidade e projetos).

**Parâmetros:**
- `capacity` (int): Capacidade de horas disponíveis
- `projects` (List[Project]): Lista de projetos do teste

**Retorna:** Nenhum

---

### `print_phase_results()`
```python
def print_phase_results(phase_num: int, phase_name: str, results: Dict[str, Any]) -> None
```
**Descrição:** Exibe resultados de uma fase algorítmica.

**Parâmetros:**
- `phase_num` (int): Número da fase (1-4)
- `phase_name` (str): Nome da fase
- `results` (Dict[str, Any]): Dicionário com resultados contendo:
  - `value` (int, opcional): Valor total alcançado
  - `projects` (List[str], opcional): Projetos selecionados
  - `hours_used` (str, opcional): Horas utilizadas
  - `memo_size` (int, opcional): Tamanho do dicionário memo
  - `complexity` (str, opcional): Complexidade algorítmica
  - `optimal` (bool, opcional): Se é solução ótima
  - `skipped` (bool, opcional): Se a fase foi pulada

**Retorna:** Nenhum

---

### `print_comparison_section()`
```python
def print_comparison_section(greedy_value: int, recursive_value: int, 
                             memo_value: int, dp_value: int) -> None
```
**Descrição:** Compara resultados de todos os algoritmos.

**Parâmetros:**
- `greedy_value` (int): Valor da estratégia gulosa
- `recursive_value` (int): Valor da recursão pura (ou None se pulada)
- `memo_value` (int): Valor da memoização
- `dp_value` (int): Valor do DP Bottom-Up

**Retorna:** Nenhum

---

### `print_analysis_section()`
```python
def print_analysis_section(greedy_value: int, dp_value: int, expected_fail: bool) -> None
```
**Descrição:** Analisa se a estratégia gulosa falhou ou encontrou solução ótima.

**Parâmetros:**
- `greedy_value` (int): Valor obtido pela gulosa
- `dp_value` (int): Valor ótimo (DP)
- `expected_fail` (bool): Se era esperado que a gulosa falhasse

**Retorna:** Nenhum

**Comportamento:**
- Se `greedy_value < dp_value`: Exibe análise de falha com percentual de perda
- Se `greedy_value == dp_value`: Confirma que todos encontraram solução ótima

---

### `print_summary_table()`
```python
def print_summary_table() -> None
```
**Descrição:** Exibe tabela resumo comparativa de todos os algoritmos.

**Parâmetros:** Nenhum

**Retorna:** Nenhum

**Conteúdo:**
- Comparação de complexidades
- Observações-chave sobre cada algoritmo
- Recomendações de uso

---

### `print_execution_stats()`
```python
def print_execution_stats(total_tests: int, greedy_failures: int) -> None
```
**Descrição:** Exibe estatísticas de execução dos testes.

**Parâmetros:**
- `total_tests` (int): Número total de casos de teste executados
- `greedy_failures` (int): Quantidade de vezes que a gulosa falhou

**Retorna:** Nenhum

---

### `print_footer()`
```python
def print_footer() -> None
```
**Descrição:** Exibe rodapé de finalização.

**Parâmetros:** Nenhum

**Retorna:** Nenhum

---

## src/test_cases.py

### Constantes Globais

#### `TEST_CASE_1_EXAMPLE`
```python
TEST_CASE_1_EXAMPLE: Dict[str, Any]
```
**Descrição:** Caso de teste padrão com 4 projetos.

**Estrutura:**
- `name`: "Exemplo Padrão"
- `capacity`: 10 horas
- `projects`: 4 projetos (A, B, C, D)
- `expected_greedy_fails`: False
- `case_num`: 1

---

#### `TEST_CASE_2_GREEDY_FAILURE`
```python
TEST_CASE_2_GREEDY_FAILURE: Dict[str, Any]
```
**Descrição:** Caso projetado para demonstrar falha da estratégia gulosa.

**Estrutura:**
- `name`: "Demonstração de Falha da Greedy"
- `capacity`: 10 horas
- `projects`: 3 projetos (X, Y, Z)
- `expected_greedy_fails`: True
- `case_num`: 2

**Observação:** Gulosa seleciona X+Y=13, mas ótimo é Y+Z=16 (perda de 18.8%)

---

#### `TEST_CASE_3_SINGLE_PROJECT`
```python
TEST_CASE_3_SINGLE_PROJECT: Dict[str, Any]
```
**Descrição:** Caso limite com apenas um projeto.

**Estrutura:**
- `name`: "Projeto Único (Caso Limite)"
- `capacity`: 10 horas
- `projects`: 1 projeto (Solo)
- `expected_greedy_fails`: False
- `case_num`: 3

---

#### `TEST_CASE_4_ALL_EXCEED_CAPACITY`
```python
TEST_CASE_4_ALL_EXCEED_CAPACITY: Dict[str, Any]
```
**Descrição:** Caso limite onde todos os projetos excedem a capacidade.

**Estrutura:**
- `name`: "Todos os Projetos Excedem Capacidade (Caso Limite)"
- `capacity`: 10 horas
- `projects`: 3 projetos pesados (Heavy1, Heavy2, Heavy3)
- `expected_greedy_fails`: False
- `case_num`: 4

**Resultado esperado:** Todos os algoritmos retornam valor = 0

---

#### `TEST_CASE_5_LARGE_SCALE`
```python
TEST_CASE_5_LARGE_SCALE: Dict[str, Any]
```
**Descrição:** Caso de escala maior com 8 projetos.

**Estrutura:**
- `name`: "Escala Maior (8 projetos)"
- `capacity`: 15 horas
- `projects`: 8 projetos (P1 a P8)
- `expected_greedy_fails`: False
- `case_num`: 5

---

#### `ALL_TEST_CASES`
```python
ALL_TEST_CASES: List[Dict[str, Any]]
```
**Descrição:** Lista contendo todos os casos de teste definidos.

**Conteúdo:**
```python
[
    TEST_CASE_1_EXAMPLE,
    TEST_CASE_2_GREEDY_FAILURE,
    TEST_CASE_3_SINGLE_PROJECT,
    TEST_CASE_4_ALL_EXCEED_CAPACITY,
    TEST_CASE_5_LARGE_SCALE,
]
```

---

## src/test_runner.py

### `run_test_case()`
```python
def run_test_case(test_case: Dict[str, Any]) -> Dict[str, int]
```
**Descrição:** Executa um único caso de teste através dos quatro algoritmos.

**Fluxo de Execução:**
1. Extrai dados do caso de teste
2. Exibe cabeçalho e entrada
3. Executa Fase 1 (Gulosa)
4. Executa Fase 2 (Recursiva) - pula se n > 10
5. Executa Fase 3 (Memoização)
6. Executa Fase 4 (DP Bottom-Up)
7. Exibe comparação e análise

**Parâmetros:**
- `test_case` (Dict[str, Any]): Dicionário com dados do teste contendo:
  - `name` (str): Nome do caso
  - `capacity` (int): Capacidade disponível
  - `projects` (List[Project]): Lista de projetos
  - `expected_greedy_fails` (bool): Se espera falha da gulosa
  - `case_num` (int): Número do caso

**Retorna:** 
- `Dict[str, int]`: Dicionário com resultados de cada algoritmo:
  ```python
  {
      'greedy': valor_gulosa,
      'recursive': valor_recursiva (ou None),
      'memoization': valor_memoizacao,
      'dp': valor_dp
  }
  ```

**Exemplo:**
```python
resultado = run_test_case(TEST_CASE_1_EXAMPLE)
# resultado = {'greedy': 29, 'recursive': 29, 'memoization': 29, 'dp': 29}
```

---

### `run_all_tests()`
```python
def run_all_tests(test_cases: List[Dict[str, Any]]) -> List[Dict[str, int]]
```
**Descrição:** Executa todos os casos de teste e exibe resumo consolidado.

**Fluxo:**
1. Loop através de todos os casos de teste
2. Executa cada caso com `run_test_case()`
3. Coleta resultados
4. Exibe tabela resumo
5. Calcula e exibe estatísticas

**Parâmetros:**
- `test_cases` (List[Dict[str, Any]]): Lista de casos de teste

**Retorna:** 
- `List[Dict[str, int]]`: Lista com resultados de todos os testes

**Exemplo:**
```python
resultados = run_all_tests(ALL_TEST_CASES)
# Executa todos os 5 casos de teste e retorna lista de resultados
```

---

## 📊 Resumo de Complexidades

| Função | Complexidade Tempo | Complexidade Espaço |
|--------|-------------------|---------------------|
| `greedy_portfolio()` | O(n log n) | O(n) |
| `recursive_portfolio()` | O(2^n) | O(n) |
| `memoization_portfolio()` | O(n × c) | O(n × c) |
| `dynamic_programming_portfolio()` | O(n × c) | O(n × c) |
| `calculate_hours_used()` | O(n) | O(1) |
| `reconstruct_selected_projects()` | O(k) | O(k) |

*Legenda: n = número de projetos, c = capacidade, k = projetos selecionados*

---

## 🎯 Guia Rápido de Uso

### Executar Programa Completo
```bash
python main.py
```

### Usar Algoritmo Individual
```python
from src.models import Project
from src.algorithms import dynamic_programming_portfolio

projetos = [
    Project("A", 12, 4),
    Project("B", 10, 3),
]
valor, selecionados = dynamic_programming_portfolio(projetos, 10)
```

### Adicionar Novo Caso de Teste
```python
# Em src/test_cases.py
MEU_TESTE = {
    'name': 'Meu Teste',
    'capacity': 20,
    'projects': [
        Project('P1', 25, 10),
        Project('P2', 18, 8),
    ],
    'expected_greedy_fails': False,
    'case_num': 6,
}

ALL_TEST_CASES.append(MEU_TESTE)
```

---

**Documentação de Funções elaborada pela equipe FIAP 2025**

**Versão:** 1.0  
**Data:** Novembro 2025  
**Autores:** Gabriel Matias Simões, Leonardo Rocha Scarpitta, Murilo Justi Rodrigues

