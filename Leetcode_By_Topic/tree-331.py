class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        prev = None
        for char in preorder:
            if char == ",":
                slots -= 1
                if slots < 0:
                    return False

                if prev != "#":
                    slots += 2
            prev = char

        slots = slots+1 if char != "#" else slots-1
        return slots == 0