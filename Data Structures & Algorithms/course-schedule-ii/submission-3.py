class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourses
        cour_map = defaultdict(list)


        for course, pre in prerequisites:
            cour_map[pre].append(course)
            in_degree[course] += 1

        ans = []
        queue = deque()

        for index, num in enumerate(in_degree):
            if num == 0:
                queue.append(index)

        
        while queue:
            cour = queue.popleft()
            ans.append(cour)
            for avail_cour in cour_map[cour]:
                in_degree[avail_cour] -= 1
                if in_degree[avail_cour] == 0:
                    queue.append(avail_cour)

        return ans if len(ans) == numCourses else []
        