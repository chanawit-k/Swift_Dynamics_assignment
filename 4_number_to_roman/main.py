"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""
digit = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
roman_symbo = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]


class Solution:

    def number_to_roman(self, number: int) -> str:
        i = 12
        roman_number = ''
        while number:
            new_number = number // digit[i]
            number %= digit[i]

            while new_number:
                roman_number = f'{roman_number}{roman_symbo[i]}'
                new_number -= 1
            i -= 1
        return roman_number
