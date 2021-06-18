# Алгоритм DFS
# Стандартная реализация DFS помещает каждую вершину графа в одну из двух категорий:
#
# Посещенные.
# Не посещенные.
# Цель алгоритма - пометить каждую вершину, как посещенную, избегая циклов.
#
# Алгоритм DFS работает следующим образом:
#
# Начните с размещения любой вершины графа на вершине стека.
# Возьмите верхний элемент стека и добавьте его в список посещенных.
# Создайте список смежных узлов этой вершины. Добавьте те, которых нет в списке посещенных, в начало стека.
# Продолжайте повторять шаги 2 и 3, пока стек не станет пустым.

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {
    '0': {'1', '2'},
    '1': {'0', '3', '4'},
    '2': {'0'},
    '3': {'1'},
    '4': {'2', '3'}
}


def main():
    dfs(graph, '0')


if __name__ == '__main__':
    main()