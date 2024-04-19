class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    # Вставка новой вершины в БДП
    if root is None:
        return Node(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def delete(root, key):
    # Удаление вершины из БДП
    if root is None:
        return root

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Находим минимальное значение в правом поддереве
        root.key = minValueNode(root.right).key
        # Удаляем вершину с минимальным значением в правом поддереве
        root.right = delete(root.right, root.key)

    return root

def minValueNode(node):
    # Находим вершину с минимальным значением в БДП
    current = node
    while current.left is not None:
        current = current.left
    return current

def search(root, key):
    # Поиск вершины в БДП
    if root is None or root.key == key:
        return root

    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

def print_bst(root):
    # Вывод БДП в виде линейно-скобочной записи
    if root:
        print(f"({root.key}", end="")
        if root.left or root.right:
            print(",", end="")
            print_bst(root.left)
            if root.right:
                print(",", end="")
                print_bst(root.right)
        print(")", end="")


if __name__ == "__main__":
    # Пример ввода дерева в формате '8(3(1,6(4,7)),10(,14(13,)))'
    input_tree = '8(3(1,6(4,7)),10(,14(13,)))'

    # Преобразование входной строки в БДП
    root = None

    stack = []
    for char in input_tree:
        if char.isdigit():
            stack.append(int(char))
        elif char == '(':
            continue
        elif char == ')':
            right = stack.pop()
            left = stack.pop()
            node = Node(left)
            node.right = Node(right)
            stack.append(node)

    root = stack[0]

    while True:
        print("\nМеню:")
        print("1. Добавить вершину")
        print("2. Удалить вершину")
        print("3. Найти вершину")
        print("4. Вывести БДП")
        print("5. Выйти из программы")

        choice = int(input("Выберите операцию (1-5): "))

        if choice == 1:
            key = int(input("Введите значение вершины для добавления: "))
            root = insert(root, key)
        elif choice == 2:
            key = int(input("Введите значение вершины для удаления: "))
            root = delete(root, key)
        elif choice == 3:
            key = int(input("Введите значение вершины для поиска: "))
            result = search(root, key)
            if result:
                print(f"Вершина со значением {key} найдена в БДП.")
            else:
                print(f"Вершина со значением {key} не найдена в БДП.")
        elif choice == 4:
            print("БДП:")
            print_bst(root)
        elif choice == 5:
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите операцию от 1 до 5.")
