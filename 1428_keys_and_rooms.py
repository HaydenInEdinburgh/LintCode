class Solution:
    """
    @param rooms: a list of keys rooms[i]
    @return: can you enter every room
    """
    def canVisitAllRooms(self, rooms):
        # Write your code here
        if not rooms:
            return True

        visited = {0}
        n = len(rooms)

        self.dfs(0, visited, rooms)
        return len(visited) == n
    def dfs(self, curRoom, visited, rooms):
        if len(visited) == len(rooms):
            return

        for nextRoom in rooms[curRoom]:
            if nextRoom in visited:
                continue
            visited.add(nextRoom)
            self.dfs(nextRoom, visited, rooms)

if __name__ == '__main__':
    s = Solution()
    rooms = [[1],[2],[3],[]]
    print(s.canVisitAllRooms(rooms))