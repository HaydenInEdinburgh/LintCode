import collections


class Solution:
    """
    @param commands: the commands of this program.
    @return: return is the program may be in endless loop.
    """
    def check(self, commands):
        # write your code here.
        n = len(commands)
        labelIdx = collections.defaultdict(int)
        visited = collections.defaultdict(int)
        # add label
        for i, c in enumerate(commands):
            if c[0] == 'l':
                labelIdx[c[6:]] = i

        return self.dfs(0, visited, labelIdx, commands)

    def dfs(self, index, visited, labelIdx, commands):
        if index == len(commands):
            return False

        if visited[index] == 1:
            return True

        if visited[index] == 2:
            return False

        visited[index] = 1
        flag = False

        if commands[index][0] == 'h':#halt
            visited[index] = 2
            return False

        if commands[index][0] == 'g':#g**
            params = commands[index].split(' ')
            if len(params) ==2:#goto
                flag |= self.dfs(labelIdx[params[1]], visited, labelIdx, commands)
            else:#gotorand
                flag |= self.dfs(labelIdx[params[1]], visited, labelIdx, commands)
                flag |= self.dfs(labelIdx[params[2]], visited, labelIdx, commands)
        else:#print
            flag |= self.dfs(index + 1, visited, labelIdx, commands)
        visited[index] = 2
        return flag

if __name__ == '__main__':
    c = collections.defaultdict(int)
    print(c)
