def intToRoman(num):
        """
        :type num: int
        :rtype: str
        """
        roman = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        rep = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        
        output = ""
        i = 0
        while num > 0:
            for _ in range(num//roman[i]):
                output = output + rep[i]
                num = num-roman[i]
            i = i + 1
        return output

number = 3
print(intToRoman(number))