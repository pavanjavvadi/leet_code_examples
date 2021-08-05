# convert from roman number to numerical number using the python script


def convert_roman_to_num(s: str) -> int:
    roman_set = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    num = 0
    for i in range(len(s)):
        if i > 0 and roman_set[s[i]] > roman_set[s[i-1]]:
            num = num + roman_set[s[i]] - 2*roman_set[s[i-1]]
        else:
            num = num + roman_set[s[i]]
    return num

print(convert_roman_to_num("XII")
)