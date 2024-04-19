class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(s):
    if not s:
        return None

    # Удаляем пробелы из строки
    s = s.replace(" ", "")

    # Проверяем, является ли корень числом
    if s[0].isdigit():
        i = 0
        while i < len(s) and s[i].isdigit():
            i += 1
        root_val = int(s[:i])
        root = TreeNode(root_val)

        # Проверяем, есть ли потомки для корня
        if i < len(s) and s[i] == "(":
            j = find_matching_bracket(s[i:])
            root.left = build_tree(s[i+1:i+j])
            if i+j+1 < len(s) and s[i+j+1] == "(":
                root.right = build_tree(s[i+j+2:-1])
        return root
    else:
        return None


def find_matching_bracket(s):
    count = 0
    for i in range(len(s)):
        if s[i] == "(":
            count += 1
        elif s[i] == ")":
            count -= 1
            if count == 0:
                return i
    return -1


def preorder_traversal(root):
    if root is None:
        return []
    result = [root.val]
    result += preorder_traversal(root.left)
    result += preorder_traversal(root.right)
    return result


def inorder_traversal(root):
    if root is None:
        return []
    result = inorder_traversal(root.left)
    result.append(root.val)
    result += inorder_traversal(root.right)
    return result


def postorder_traversal(root):
    if root is None:
        return []
    result = postorder_traversal(root.left)
    result += postorder_traversal(root.right)
    result.append(root.val)
    return result


# Пример использования
input_str = "8 (3 (1, 6 (4,7)), 10 (, 14(13,)))"
tree = build_tree(input_str)

print("Прямой обход (preorder):", preorder_traversal(tree))
print("Центральный обход (inorder):", inorder_traversal(tree))
print("Концевой обход (postorder):", postorder_traversal(tree))