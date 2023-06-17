class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostKDistinct(nums, k):
            niceSubarray = 0
            hashmap = {}
            left, right = 0, 0
            
            while right < len(nums):
                if nums[right] in hashmap:
                    hashmap[nums[right]] += 1
                else:
                    hashmap[nums[right]] = 1
            
                while len(hashmap) > k:
                    hashmap[nums[left]] -= 1
                    if hashmap[nums[left]] == 0:
                        del hashmap[nums[left]]
                    left += 1
                
                niceSubarray += right - left + 1
                right += 1
                
            return niceSubarray
        
        return atMostKDistinct(nums, k) - atMostKDistinct(nums, k - 1)