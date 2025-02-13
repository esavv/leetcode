'''
files = [
  "/webapp/assets/html/a.html",
"/webapp/assets/html/b.html",
"/webapp/assets/js/c.js",
"/webapp/entrypoint.txt",
]

Write a program which intakes these filepaths, and prints them out in a hierarchial filesystem fashion. 

-- webapp
  -- assets
    -- html
      -- a.html
      -- b.html
    -- js
      -- c.js
  -- entrypoint.txt
'''

files = [
  "/webapp/assets/html/a.html",
"/webapp/assets/html/b.html",
"/webapp/assets/js/c.js",
"/webapp/entrypoint.txt",
]

# The solution I submitted

class TreeNode():
    def __init__(self, name="", children={}): 
        self.name = name
        self.children = children

def soln1(files):
    def parseFile(file, root):
        filenames = file.split("/")
        for name in filenames:
            if name not in root.children:
                root.children[name] = TreeNode(name=name)
            root = root.children[name]
        return

    root = TreeNode()
    for file in files:
        parseFile(file, root)

    def dfs(root, level):
        if not root:
            return
        extra_space = ""
        for _ in range(level):
            extra_space += "  "
        print(extra_space + "-- " + root.name)
        for child in root.children:
            dfs(child, level+1)
        return

    for child in root.children:
        dfs(child, 0)
    return

# The solution I submitted, but with bug fixes

class TreeNode():
    def __init__(self, name=""):
        self.name = name
        self.children = {}

def soln1_bugfix(files):
    def parseFile(file, root):
        filenames = file.split("/")[1:]
        for name in filenames:
            if name not in root.children:
                root.children[name] = TreeNode(name=name)
            root = root.children[name]
        return

    root = TreeNode()
    for file in files:
        parseFile(file, root)

    def dfs(root, level):
        extra_space = ""
        for _ in range(level):
            extra_space += "  "
        print(extra_space + "-- " + root.name)
        for child in root.children:
            dfs(root.children[child], level+1)
        return

    for child in root.children:
        dfs(root.children[child], 0)
    return

# Attempting an approach with just dictionaries, no tree class, and some cleanup

def soln2(files):
    root = {}
    for file in files:
        node = root
        filenames = file.split("/")
        if filenames[0] == "":
            filenames = filenames[1:]
        for name in filenames:
            if name not in node:
                node[name] = {}
            node = node[name]

    def dfs(name, root, level):
        extra_space = "".join(["  " for _ in range(level)])
        print(extra_space + "-- " + name)
        for child in root:
            dfs(child, root[child], level+1)
        return

    for child in root:
        dfs(child, root[child], 0)
    return

print('soln1_bugfix() output:\n')
soln1_bugfix(files)
print('\nsoln2() output:\n')
soln2(files)
