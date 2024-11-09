class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        j = 0
        i = 0
        sLen = len(s)
        while(i < sLen):
            if(s[sLen - i - 1]==s[j]):
                j += 1
            i += 1
        if(j==sLen):
            return s
        p = s[j:]
        p = p[::-1]
        return p + self.shortestPalindrome(s[:j]) + s[j:]