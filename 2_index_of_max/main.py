"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 4

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> int | str:
        if len(numbers) < 1:
            print('list can not blank')

        max_value = numbers[0]
        index_max_value = 0
        for idx, value in enumerate(numbers[1:]):
            if value > max_value:
                max_value = value
                index_max_value = idx + 1
        return index_max_value
