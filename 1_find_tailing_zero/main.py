"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        if number < 0:
            return "number can not be negative"
        factorial_number = number
        number -= 1
        count_zero = 0

        while number > 1:
            factorial_number *= number
            number -= 1

        for number in str(factorial_number)[::-1]:
            if int(number) == 0:
                count_zero += 1
            else:
                break
        return count_zero
