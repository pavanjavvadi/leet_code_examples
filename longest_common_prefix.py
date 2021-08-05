from typing import List


def common_prefix(words: List[str]) -> str:
    
    prefix = words[0]

    # looping all the words
    for word in words[1:]:

        # check first word with other words if words are equal return that prefix 
        while word[:len(prefix)] != prefix:
            
            # if word and prefix are not equal remove last char ad compare do until prefix = ""
            prefix = prefix[:-1]

            if not prefix:    # if prefix="" is false not false = true
                 
                 # if no pefix is found return empty
                 return ""
    
    return prefix