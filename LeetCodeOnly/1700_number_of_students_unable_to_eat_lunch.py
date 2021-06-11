class Solution:
    def countStudents(self, students, sandwiches) -> int:
        if not students:
            return 0 

        while sandwiches:
            if sandwiches[0] in students:
                students.remove(sandwiches[0])
                sandwiches.pop(0)
            else:
                break

        return len(sandwiches)

