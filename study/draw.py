class Solution():
    def romanToInt(self, number_str):
        """
        :type s: str
        :rtype: int
        """
        RELATES = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        last = 0
        for i in number_str:
            current = RELATES[i]
            if current > last:
                last = current - last * 2
                total += last
            else:
                last = current
                total += current
        print(total)
        return total


solution = Solution()
solution.romanToInt(input())

