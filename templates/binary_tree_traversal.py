class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# iterative BFS
def iterativeBFS(root):
    from collections import deque
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return

# iterative inorder DFS
def iterativeInorderDFS(root):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        print(root.val)
        root = root.right
    return

# iterative preorder DFS
def iterativePreorderDFS(root):
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return

# iterative postorder DFS
def iterativePostorderDFS(root):
    #TODO
    return

# recursive inorder DFS
def recursiveInorderDFS(root):
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        print(node.val)
        dfs(node.right)
        return
    return dfs(root)

# recursive preorder DFS
def recursivePreorderDFS(root):
    def dfs(node):
        if not node:
            return
        print(node.val)
        dfs(node.left)
        dfs(node.right)
        return
    return dfs(root)

# recursive postorder DFS
def recursivePostorderDFS(root):
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        print(node.val)
        return
    return dfs(root)