class ThroneInheritance:

    def __init__(self, kingName: str):
        self.children=defaultdict(list)
        self.dead=set()
        self.kingName=kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)
    def getInheritanceOrder(self) -> List[str]:
        ans=[]
        def dfs(root):
            if root not in self.dead:
                ans.append(root)
                
            for child in self.children[root]:
                dfs(child)
        dfs(self.kingName)
        return ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()