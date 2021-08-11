class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # if i and j overlaps, return the overlap duration
        # if js > ie, i += 1
        # if je < is, j += 1
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])

        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            if slots2[j][0] > slots1[i][1]:
                i += 1
            elif slots2[j][1] < slots1[i][0]:
                j += 1
            else:
                start = max(slots1[i][0], slots2[j][0])
                end = min(slots1[i][1], slots2[j][1])

                if end - start >= duration:
                    return [start, start+duration]

                else:
                    if slots2[j][1] < slots1[i][1]:
                        j += 1
                    else:
                        i+= 1

        return []