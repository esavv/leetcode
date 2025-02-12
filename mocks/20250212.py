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

class TreeNode():
    # def __init__(self, name="", children={}): 
    def __init__(self, name=""):
        self.name = name
        # self.children = children
        self.children = {}

def soln1(files):
    def parseFile(file, root):
        # filenames = file.split("/")
        filenames = file.split("/")[1:]
        for name in filenames:
            if name not in root.children:
                root.children[name] = TreeNode(name=name)
            root = root.children[name]
        return

    root = TreeNode()
    for file in files:
        parseFile(file, root)

    # def dfs(root, level):
    def dfs(root, level):
        # if not root:
        #     return
        extra_space = ""
        for _ in range(level):
            extra_space += "  "
        print(extra_space + "-- " + root.name)
        for child in root.children:
            dfs(root.children[child], level+1)
            # dfs(child, level+1)
        return

    for child in root.children:
        dfs(root.children[child], 0)
        # dfs(child, 0)
    return

soln1(files)
