"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
import collections


class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    """
    @param imput:
    @param id:
    @return: the total importance value
    """
    def getImportance(self, employees, id):
        # Write your code here.
        if not employees:
            return 0

        res = 0
        employeeObjects = self.getEmployeeObjects(employees)
        queue = collections.deque([employeeObjects[id]])
        while queue:
            node = queue.popleft()
            res += node.importance
            for sub in node.subordinates:
                queue.append(employeeObjects[sub])

        return res



    def getEmployeeObjects(self, employees):
        objects = {}
        for e in employees:
            objects[e.id] = e

        return objects