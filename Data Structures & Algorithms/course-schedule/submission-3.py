class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        in_degree = [0] * numCourses
        course_map = defaultdict(list)

        for course, pre in prerequisites:
            course_map[pre].append(course)
            in_degree[course] += 1

        queue = deque()

        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            c = queue.popleft()
            for avail_cour in course_map[c]:
                in_degree[avail_cour] -= 1
                if in_degree[avail_cour] == 0:
                    queue.append(avail_cour)

        for num in in_degree:
            if num != 0:
                return False
        

        return True



