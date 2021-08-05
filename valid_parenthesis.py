""" def valid_parenthesis(string):

    _valid_parenthesis = ["()", "{}", "[]"]
    while any(parenthesis in string for parenthesis in _valid_parenthesis):

        
        for parenthesis in _valid_parenthesis:
            string = string.replace(parenthesis, "")
    
    return not string

string = "{{}[]()}"
print(True if valid_parenthesis(string) else False)
 """

def valid_parenthesis(string):

    open_list = ["(", "[", "{"]
    close_list = [")", "]", "}"]

    temp = []
    for i in string:

        if i in open_list:
            temp.append(i)
        
        elif i in close_list:

            index = close_list.index(i)

            if len(temp) > 0 and temp[len(temp) - 1] == open_list[index]:
                temp.pop()
            else:
                return False
    return True

string = "{{}[]()}"
print(True if valid_parenthesis(string) else False)

string = "{{}[]()}}"
print(True if valid_parenthesis(string) else False)