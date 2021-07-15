import collections


class Solution:
    """
    @param pid: the process id
    @param ppid: the parent process id
    @param kill: a PID you want to kill
    @return: a list of PIDs of processes that will be killed in the end
    """

    def killProcess(self, pid, ppid, kill):
        # Write your code here
        if not pid or not ppid:
            return

        children_map = self.get_child(pid, ppid)
        print(children_map)
        killed = {kill}
        queue = collections.deque([kill])

        while queue:
            process = queue.popleft()
            if process not in children_map:
                continue
            for child in children_map[process]:
                if child in killed:
                    continue
                queue.append(child)
                killed.add(child)

        return list(killed)


    def get_child(self, pid, ppid):
        children_map = {}
        for i, id in enumerate(pid):

            if ppid[i] not in children_map:
                children_map[ppid[i]] = []
            children_map[ppid[i]].append(id)
        return children_map

if __name__ == '__main__':
    s = Solution()
    PID = [1, 3, 10, 5]
    PPID = [3, 0, 5, 3]
    killID = 5
    print(s.killProcess(PID, PPID, killID))