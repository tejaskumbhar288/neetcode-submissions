class FileSystem:

    def __init__(self):
        self.root = {'dirs': {}, 'files': {}}

    def _get_node(self, path: str):
        curr = self.root
        if path == "/":
            return curr
        parts = path.split("/")[1:]
        for part in parts:
            if part in curr['dirs']:
                curr = curr['dirs'][part]
            elif part in curr['files']:
                return curr['files'][part]
        return curr

    def ls(self, path: str) -> List[str]:
        if path == "/":
            res = list(self.root['dirs'].keys()) + list(self.root['files'].keys())
            return sorted(res)
        parts = path.split("/")
        curr = self.root
        for i in range(1, len(parts) - 1):
            curr = curr['dirs'][parts[i]]
        
        last = parts[-1]
        if last in curr['files']:
            return [last]
        
        node = curr['dirs'][last]
        res = list(node['dirs'].keys()) + list(node['files'].keys())
        return sorted(res)

    def mkdir(self, path: str) -> None:
        curr = self.root
        parts = path.split("/")[1:]
        for part in parts:
            if part not in curr['dirs']:
                curr['dirs'][part] = {'dirs': {}, 'files': {}}
            curr = curr['dirs'][part]

    def addContentToFile(self, filePath: str, content: str) -> None:
        parts = filePath.split("/")
        curr = self.root
        for i in range(1, len(parts) - 1):
            curr = curr['dirs'][parts[i]]
        
        filename = parts[-1]
        if filename not in curr['files']:
            curr['files'][filename] = ""
        curr['files'][filename] += content

    def readContentFromFile(self, filePath: str) -> str:
        parts = filePath.split("/")
        curr = self.root
        for i in range(1, len(parts) - 1):
            curr = curr['dirs'][parts[i]]
        return curr['files'][parts[-1]]