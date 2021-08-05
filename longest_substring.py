def lengthOfLongestSubstring(s):
        
        i = 0
        num = 0
        _dict = {} 

        for j in range(len(s)):
            if s[j] in _dict:
                i = max(_dict[s[j]], i)
            
            num = max(num, j - i + 1)
            _dict[s[j]] = j + 1
        return num


print(" final ans:", lengthOfLongestSubstring("pwwkew"))
