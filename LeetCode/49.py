# Solved on 2022. 2. 1.
# 49. Group Anagrams

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        words = collections.defaultdict(list)
        for string in strs:
            words[''.join(sorted(string))].append(string)
        return list(words.values())
        