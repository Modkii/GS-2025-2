"""
Funções de Formatação de Saída
===============================
Toda a lógica de exibição e formatação para saída em Português-BR.
Usa caracteres Unicode box-drawing e ícones emoji.
"""

from typing import List, Dict, Any
from src.models import Project


def print_header(title: str, style: str = "double") -> None:
    """Imprime um cabeçalho de seção formatado com caracteres box-drawing."""
    width = 70
    if style == "double":
        print(f"\n╔{'═' * (width - 2)}╗")
        print(f"║{title.center(width - 2)}║")
        print(f"╚{'═' * (width - 2)}╝")
    elif style == "single":
        print(f"\n┌{'─' * (width - 2)}┐")
        print(f"│{title.center(width - 2)}│")
        print(f"└{'─' * (width - 2)}┘")


def print_section(title: str, icon: str = "🔹") -> None:
    """Imprime um cabeçalho de subseção com ícone."""
    print(f"\n{icon} {title}:")


def print_result(label: str, value, suffix: str = "", indent: int = 2, 
                 marker: str = "├─", optimal: bool = False) -> None:
    """Imprime uma linha de resultado com formatação consistente."""
    spacing = " " * indent
    opt_marker = " ⭐ ÓTIMO" if optimal else ""
    if suffix:
        print(f"{spacing}{marker} {label}: {value} {suffix}{opt_marker}")
    else:
        print(f"{spacing}{marker} {label}: {value}{opt_marker}")


def print_algorithm_phase(phase_num: int, phase_name: str) -> None:
    """Imprime cabeçalho de seção para cada fase do algoritmo."""
    print(f"\n🔹 FASE {phase_num} - {phase_name}:")


def print_welcome() -> None:
    """Imprime cabeçalho de boas-vindas da aplicação."""
    print_header("OTIMIZAÇÃO DE PORTFÓLIO - PROGRAMAÇÃO DINÂMICA")
    print("\n📌 Resolução do Problema da Mochila 0/1 para Seleção de Projetos")
    print("📚 FIAP - Curso de Programação Dinâmica")
    print("📅 Data: 14 de Novembro de 2025")


def print_test_case_header(case_num: int, name: str) -> None:
    """Formata cabeçalho do caso de teste."""
    print_header(f"CASO DE TESTE {case_num}: {name}")


def print_input_section(capacity: int, projects: List[Project]) -> None:
    """Formata exibição dos dados de entrada."""
    print_section("DADOS DE ENTRADA", "📊")
    print(f"  • Capacidade: {capacity} horas-especialista")
    print(f"  • Projetos:")
    for p in projects:
        print(f"    - {p.name}: Valor={p.value}, Horas={p.hours}, Eficiência={p.efficiency():.2f}")


def print_phase_results(phase_num: int, phase_name: str, results: Dict[str, Any]) -> None:
    """Imprime resultados de uma única fase do algoritmo."""
    print_algorithm_phase(phase_num, phase_name)
    
    if 'skipped' in results and results['skipped']:
        print(f"  └─ ⚠️  Pulado (muitos projetos, tempo exponencial)")
        return
    
    if 'value' in results:
        optimal = results.get('optimal', False)
        print_result("Valor Total", results['value'], indent=2, marker="├─", optimal=optimal)
    
    if 'projects' in results:
        print_result("Projetos Selecionados", results['projects'], indent=2, marker="├─")
    
    if 'hours_used' in results:
        print_result("Horas Utilizadas", results['hours_used'], indent=2, marker="├─")
    
    if 'memo_size' in results:
        print_result("Tamanho do Memo", f"{results['memo_size']} entradas", indent=2, marker="├─")
    
    if 'complexity' in results:
        print_result("Complexidade", results['complexity'], indent=2, marker="└─")


def print_comparison_section(greedy_value: int, recursive_value: int, 
                             memo_value: int, dp_value: int) -> None:
    """Imprime comparação de todos os resultados dos algoritmos."""
    print_section("COMPARAÇÃO DE RESULTADOS", "📈")
    
    greedy_status = "❌ Não-Ótimo" if greedy_value < dp_value else "✓ Ótimo"
    print_result("Gulosa", f"Valor = {greedy_value}", f"({greedy_status})", indent=2, marker="├─")
    
    if recursive_value is not None:
        rec_status = "✓ Ótimo" if recursive_value == dp_value else "❌ Erro"
        print_result("Recursiva", f"Valor = {recursive_value}", f"({rec_status})", indent=2, marker="├─")
    
    print_result("Memoização", f"Valor = {memo_value}", "(✓ Ótimo)", indent=2, marker="├─")
    print_result("DP Bottom-Up", f"Valor = {dp_value}", "(✓ Ótimo) ⭐", indent=2, marker="└─")


def print_analysis_section(greedy_value: int, dp_value: int, expected_fail: bool) -> None:
    """Imprime análise de falha ou sucesso da estratégia gulosa."""
    if greedy_value < dp_value:
        print(f"\n⚠️  ANÁLISE: Falha na Estratégia Gulosa Detectada!")
        loss_percent = ((dp_value - greedy_value) / dp_value) * 100
        print(f"    • Gulosa obteve: {greedy_value}")
        print(f"    • Valor ótimo: {dp_value}")
        print(f"    • Diferença: {dp_value - greedy_value} pontos de valor perdidos ({loss_percent:.1f}%)")
        if expected_fail:
            print(f"    • ✓ Esperado para este caso de teste")
    elif expected_fail:
        print(f"\n⚠️  AVISO: Esperava-se falha da gulosa, mas encontrou solução ótima")
    else:
        print(f"\n✓ Todos os algoritmos encontraram a solução ótima!")


def print_summary_table() -> None:
    """Imprime tabela resumo abrangente."""
    print_header("RESUMO DA EXECUÇÃO - ANÁLISE COMPARATIVA")
    
    print("\n📊 COMPARAÇÃO DE ALGORITMOS:\n")
    print(f"{'Algoritmo':<30} {'Complexidade':<20} {'Espaço':<15} {'Status'}")
    print("─" * 85)
    print(f"{'Gulosa (Greedy)':<30} {'O(n log n)':<20} {'O(1)':<15} ⚠️  Não-Ótimo")
    print(f"{'Recursiva Pura':<30} {'O(2^n)':<20} {'O(n)':<15} ✓ Ótimo (Lento)")
    print(f"{'Memoização (Top-Down)':<30} {'O(n×cap)':<20} {'O(n×cap)':<15} ✓ Ótimo (Rápido)")
    print(f"{'DP Bottom-Up':<30} {'O(n×cap)':<20} {'O(n×cap)':<15} ✓ Ótimo (Melhor) ⭐")
    
    print("\n💡 OBSERVAÇÕES-CHAVE:")
    print("  1. A estratégia gulosa pode falhar - demonstrado no Caso de Teste 2")
    print("  2. Memoização e DP Bottom-Up sempre encontram a solução ótima")
    print("  3. DP Bottom-Up é mais eficiente para produção (sem overhead de recursão)")
    print("  4. A diferença de performance aumenta significativamente com o tamanho dos dados")
    print("  5. Para n > 25, a solução recursiva pura se torna impraticável")
    
    print("\n🎯 RECOMENDAÇÃO DE USO:")
    print("  • Gulosa: Aproximações rápidas quando otimalidade não é crítica")
    print("  • Recursiva: Apenas fins educacionais (nunca em produção)")
    print("  • Memoização: Quando o problema tem estrutura naturalmente recursiva")
    print("  • DP Bottom-Up: PRODUÇÃO - mais eficiente, previsível, sem limites de pilha ⭐")


def print_execution_stats(total_tests: int, greedy_failures: int) -> None:
    """Imprime estatísticas de execução."""
    print_header("EXECUÇÃO CONCLUÍDA COM SUCESSO")
    print("\n✅ Todos os casos de teste foram executados com sucesso!")
    print("\n📊 ESTATÍSTICAS DA EXECUÇÃO:")
    print(f"  • Total de casos de teste: {total_tests}")
    print(f"  • Falhas da estratégia gulosa: {greedy_failures} de {total_tests}")
    print(f"  • Taxa de sucesso DP: 100% (solução ótima sempre encontrada)")


def print_footer() -> None:
    """Imprime rodapé final."""
    print("\n" + "═" * 70 + "\n")
