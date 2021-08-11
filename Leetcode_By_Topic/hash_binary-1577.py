class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        cnt1 = collections.defaultdict(int)
        cnt2 = collections.defaultdict(int)
        for n in nums1:
            cnt1[n] += 1
        for n in nums2:
            cnt2[n] += 1

        def triplets(dict_a, dict_b):
            ans = 0
            for n1, value in dict_a.items():
                k = dict_b.get(n1, 0)
                tmp = k * (k - 1) // 2

                sq = n1 * n1
                
                for n2 in dict_b:
                    if n2 < n1 and sq % n2 == 0:
                        tmp += dict_b.get(n2, 0) * dict_b.get(sq // n2, 0)
                ans += tmp * value
            return ans
        
        return triplets(cnt1, cnt2) + triplets(cnt2, cnt1)
        
        """
        def count(list_a, list_b):
            table = collections.defaultdict(int)
            
            # [j] * [k]
            for i in range(len(list_a) - 1):
                for j in range(i + 1, len(list_a)):
                    table[list_a[i] * list_a[j]] += 1

            count = 0
            
            # if nums[i] ^ 2 is in table, add
            for num in list_b:
                count += table[num * num]
            return count
        
        return count(nums1, nums2) + count(nums2, nums1)
        """