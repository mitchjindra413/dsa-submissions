class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_req = defaultdict(list)

        for a, b in prerequisites:
            pre_req[a].append(b)
        
        seen = set()

        def explore(node):
            if node in seen:
                return False
            
            seen.add(node)
            for pr in pre_req[node]:
                if not explore(pr):
                    return False
            seen.remove(node)
            # pre_req[node] = []
            return True

        for c in range(numCourses):
            if not explore(c):
                return False
        return True