class TreeNode:
    def __init__(self, name, isFile):
        self.name = name
        self.kids = {}
        self.isFile = isFile
        self.content = ""

class FileSystem:

    def __init__(self):
        self.root = TreeNode("", isFile=False)

    @staticmethod
    def pathToList(path:str) -> List[str]:
        "turns the path string into a list of names ini the tree to check for"
        if path == "/":
            return []
        else:
            return path.split("/")[1:]

    def ls(self, path: str) -> List[str]:
        nodepath = FileSystem.pathToList(path)

        cur:TreeNode = self.root
        for node in nodepath:
            cur = cur.kids[node]

        if not cur.isFile:
            return sorted(list(cur.kids.keys()))
        else:
            return [cur.name]

    def mkdir(self, path: str) -> None:
        nodepath = FileSystem.pathToList(path)

        cur:TreeNode = self.root
        for node in nodepath:
            if node not in cur.kids:
                cur.kids[node] = TreeNode(node, isFile=False)
            cur = cur.kids[node]

    def addContentToFile(self, filePath: str, content: str) -> None:
        nodepath = FileSystem.pathToList(filePath)

        cur = self.root
        for node in nodepath[:-1]:
            cur = cur.kids[node]
        
        filename = nodepath[-1]
        
        if filename not in cur.kids:
            cur.kids[filename] = TreeNode(filename, isFile=True)

        cur.kids[filename].content += content

    def readContentFromFile(self, filePath: str) -> str:
        nodepath = FileSystem.pathToList(filePath)
        cur = self.root
        for node in nodepath:
            cur = cur.kids[node]
        
        return cur.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
