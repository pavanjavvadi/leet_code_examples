def infinite_squence():
    num = 0
    while True:
        yield num
        num = num + 1

def is_palindrome(num):
    
    str_num = str(num)
    if len(str_num) == 1:
        return True
    else:
        if str_num[0] == str_num[-1]:
            return is_palindrome(str_num[1, -1])
        else:
            return False
    

def palindrome(num):
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0
    while temp != 0:
        reversed_num = (reversed_num*10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    return False


for i in infinite_squence():
    _palindrome = palindrome(i)
    if _palindrome:
        print(_palindrome)


# for x, y in [ (7, 2), (5, 8), (6, 4) ]:
#        print(x, y) -> give as x=7,5,6 y=2,8,4