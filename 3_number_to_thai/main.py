"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""
number_to_thai = {
    '0': 'ศูนย์',
    '1': 'หนึ่ง',
    '2': 'สอง',
    '3': 'สาม',
    '4': 'สี่',
    '5': 'ห้า',
    '6': 'หก',
    '7': 'เจ็ด',
    '8': 'แปด',
    '9': 'เก้า'
}

number_to_digit = {
    '2': 'สิบ',
    '3': 'ร้อย',
    '4': 'พัน',
    '5': 'หมื่น',
    '6': 'แสน',
    '7': 'ล้าน',
    '8': 'สิบ',

}


class Solution:

    def number_to_thai(self, number: int) -> str:
        digit_lenght = len(str(number))
        list_number = list(str(number))
        thai_number = ''
        for number in list_number:
            if int(number) >= 1:
                # handdle 2
                if ((digit_lenght == 2 or digit_lenght == 8) and int(number) == 2):
                    thai_number = f'{thai_number}ยี่'
                # handdle 1
                elif ((digit_lenght == 1 or digit_lenght == 7) and int(number) == 1):
                    if not thai_number == '' and thai_number[-3:] == 'สิบ':
                        thai_number = f'{thai_number}เอ็ด'
                    else:
                        thai_number = f'{thai_number}{number_to_thai[number]}'
                else:
                    thai_number = f'{thai_number}{number_to_thai[number]}'
                # handdle
                # elif digit_lenght != 8 and int(number) != 1:
                #     thai_number = f'{thai_number}{number_to_thai[number]}'
                # elif (int(number) != 1) or (digit_lenght == 1 and int(number) == 1):
                #     thai_number = f'{thai_number}{number_to_thai[number]}'

            if (digit_lenght >= 2 and int(number) != 0) or digit_lenght == 7:
                thai_number = f'{thai_number}{number_to_digit[str(digit_lenght)]}'

            digit_lenght -= 1
        print(thai_number)

Solution().number_to_thai()
