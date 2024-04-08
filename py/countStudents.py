class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c = Counter(students)

        for sandwich in sandwiches:
            if c[sandwich] > 0:
                c[sandwich] -=1
            else:
                return c.total()
        
        return 0
        