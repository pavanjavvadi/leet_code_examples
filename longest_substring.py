def lengthOfLongestSubstring(s):
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}
        

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)                                                                                                                       
                print("i", i)

            ans = max(ans, j - i + 1)
            print("ans", ans)
            mp[s[j]] = j + 1
            print(mp)
        return ans


print(" final ans:", lengthOfLongestSubstring("pwwkew"))
