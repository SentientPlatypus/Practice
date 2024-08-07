


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        result = ""
        group_index = 0

        while num > 0:
            if num % 1000 != 0:
                group_result = ""
                part = num % 1000

                if part >= 100:
                    group_result += ones[part // 100] + " Hundred "
                    part %= 100

                if part >= 20:
                    group_result += tens[part // 10] + " "
                    part %= 10

                if part > 0:
                    group_result += ones[part] + " "

                group_result += thousands[group_index] + " "
                result = group_result + result
            num //= 1000
            group_index += 1

        return result.strip()