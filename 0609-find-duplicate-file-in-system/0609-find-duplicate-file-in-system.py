class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contentDict = {}
        for path in paths:
            files = path.split()
            for file in files[1:]:
                mainFile = file.split('(')
                fileName = mainFile[0]
                content = mainFile[1][:-1]

                if content not in contentDict:
                    contentDict[content] = [files[0]+"/"+fileName]
                else:
                    contentDict[content].append(files[0]+"/"+fileName)
        
        res = []
        for content, dirs in contentDict.items():
            if len(dirs) > 1:
                res.append(dirs)

        return res