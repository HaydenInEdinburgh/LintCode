import collections


class Solution:
    """
    @param musics: the musics
    @return: calc the number of pair of music
    """
    def musicPairs(self, musics):
        # write your code here
        visited = collections.defaultdict(int)
        result = 0
        for music in musics:
            music = music % 60
            if music == 0:
                result += visited[0]
            elif 60 - music in visited:
                result += visited[60 - music]
            visited[music] += 1
        return result

if __name__ == '__main__':
    s = Solution()
    musics = [1,2,59,60, 119]
    print(s.musicPairs(musics))