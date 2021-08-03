class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # two pointer
        # O(N) time and O(1) space
        slots, prev = 1, None

        for char in preorder:
            if char == ",":
                slots -= 1
                
                if slots < 0:
                    return False
                if prev != "#":
                    slots += 2

            prev = char

        # the last node
        slots = slots + 1 if char != "#" else slots - 1

        return slots == 0

        """
        O(N) time, O(N) space because we split the array
        slots = 1

        for node in preorder.split(','):
            slots -= 1
            
            if slots < 0:
                return False

            if node != "#":
                slots += 2

        return slots == 0
        """