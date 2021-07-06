def anagram(strs):
    list_value = []
    for i in strs:
        a =[''.join(sorted(i)), i]
        list_value.append(a)
    print(list_value)


strs = ["eat","tea","tan","ate","nat","bat"]
anagram(strs)