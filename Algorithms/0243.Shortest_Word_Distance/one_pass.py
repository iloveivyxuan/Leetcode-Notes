class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        size = len(words)
        index_1, index_2 = None, None
        dis = size

        for i in range(size):
            if words[i] == word1:
                index_1 = i
                if (index_2 is not None): dis = min(dis, index_1 - index_2)
            if words[i] == word2:
                index_2 = i
                if (index_1 is not None): dis = min(dis, index_2 - index_1)

        return dis
