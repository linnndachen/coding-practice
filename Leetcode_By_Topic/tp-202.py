class Solution:
    def isHappy(self, n: int) -> bool:
        def _getnext(num):
            total = 0
            while num > 0:
                num, digit = divmod(num, 10)
                total += digit ** 2

            return total

        slow = n
        fast = _getnext(n)
        while fast != 1 and slow != fast:
            slow = _getnext(slow)
            fast = _getnext(_getnext(fast))

        return fast == 1

    """
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)

        while n != 1:
            char = str(n)
            length = len(char)
            new_n = 0
            for i in range(length):
                new_n += pow(int(char[i]), 2)

            if new_n in seen:
                return False

            seen.add(new_n)
            n = new_n

        return True
    """