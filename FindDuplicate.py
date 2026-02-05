class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        pathdict = defaultdict(list)
        result = []
        for path in paths:
            parts = path.split(" ")
            directory = parts[0]
            for fileinfo in parts[1:]:
                txtname, content = fileinfo.split("(")
                fullpath = directory + "/" + txtname
                pathdict[content].append(fullpath)
        for key, value in pathdict.items():
            if len(pathdict[key]) > 1:
                result.append(pathdict[key])

        return result
